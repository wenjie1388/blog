from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth import authenticate, login, logout

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    # AllowAny,
    IsAuthenticatedOrReadOnly,
)
from rest_framework import status as status_

import django_redis
import logging

from auths.permissions import IsAnonymousUser, AllowAny, IsAuthenticated
from auths.authentication import SessionAuthentication, TokenAuthentication
from auths.models import Token
from .models import Consumer as User
from .serializer import UserLoginSerializer, UserModelSerializer, UserCreateSerializer

cache0 = django_redis.get_redis_connection("default")
logger = logging.getLogger("django.request")


@receiver(post_save, sender=User)
def create_token(sender, instance, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    lookup_field = "id"

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        auth_code = request.data.pop("auth_code", None)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # if cache0.get(cellphone).decode() != auth_code:
        cellphone = serializer.data.get("cellphone")
        if cache0.get(auth_code) or cache0.get(cellphone).decode() != auth_code:
            return Response({"auth_code": "验证码错误"})

        if cache0.ttl(auth_code) == -2:
            return Response({"auth_code": "验证码失效"})

        self.perform_create(serializer)
        print(serializer.data)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status_.HTTP_201_CREATED, headers=headers
        )

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status_.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserCreateSerializer
        return super().get_serializer_class()

    def get_authenticators(self):
        return super().get_authenticators()

    def get_permissions(self):
        if self.request.method in ["POST", "GET"]:
            return AllowAny
        else:
            return IsAuthenticated


class UserLoginView(APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAnonymousUser,)

    def get(self, request, *args, **kwargs):
        query_params = request.query_params.dict()
        auth_code = query_params.pop("auth_code", None)
        serializer = UserLoginSerializer(data=query_params)
        serializer.is_valid(raise_exception=True)

        # 获取用户数据
        cellphone = serializer.validated_data.get("cellphone")
        password = serializer.validated_data.get("password")
        user = User.objects.get(cellphone=cellphone)

        if cache0.ttl(cellphone) == -2:
            return Response({"msg": "验证码失效"}, status_.HTTP_400_BAD_REQUEST)
        if cache0.get(cellphone) != auth_code.encode():
            return Response({"msg": "验证码错误"}, status_.HTTP_400_BAD_REQUEST)

        request.session["id"] = user.id
        request.session["username"] = user.username
        request.user = user.username

        try:
            token = Token.objects.get(user=user.id)
        except Token.DoesNotExist:
            token = Token.objects.create(user=user)

        return Response(
            data={
                "uid": user.id,
                "username": user.username,
                "token": token.key,
            }
        )


class UserLogoutView(APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, id=None, *args, **kwargs):
        request.session.flush()
        return Response(status=status_.HTTP_204_NO_CONTENT)
