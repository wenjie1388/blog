from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models.query import QuerySet
from django.utils import timezone

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from rest_framework import status as status_

import django_redis
import logging

from auths.permissions import IsAnonymousUser, IsOwnerOrReadOnly
from auths.authentication import SessionAuthentication, TokenAuthentication
from auths.pagination import PageNumberPagination
from auths.models import Token

from .models import Consumer as User
from auths.models import AuthCode
from .serializer import (
  UserCreateSerializer,
  UserLoginSerializer, 
  UserModelSerializer, 
  
  ) 

cache0 = django_redis.get_redis_connection("default")
logger = logging.getLogger("django.request")


# @receiver(post_save, sender=User)
# def create_token(sender, instance, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = PageNumberPagination
    lookup_field = "id"

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
      
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        print(f"kwargs:{kwargs}")
        return super().retrieve(request, *args, **kwargs)

    # def get_queryset(self):
    #     queryset = self.queryset
    #     if isinstance(queryset, QuerySet):
    #         # Ensure queryset is re-evaluated on each request.
    #         queryset = queryset.all()
    #     query_params = self.request.query_params.dict()
    #     query = {key + "__icontains": value for key, value in query_params.items()}
    #     if query_params:
    #         queryset = queryset.filter(**query)
    #     return queryset

    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserCreateSerializer
        return super().get_serializer_class()

    # def get_authenticators(self):
    #     return super().get_authenticators()

    # def get_permissions(self):
    #     return super().get_permissions()


class UserLoginView(APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAnonymousUser,)

    def get(self, request, *args, **kwargs):
        # print(f"request.user:{request.user}")
        # query_params = request.query_params.dict()
        serializer = UserLoginSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        account = serializer.validated_data.get("account")
        password = serializer.validated_data.get("password")
        authcode = serializer.validated_data.get("authcode")

        if "@" in account:
            user = User.objects.get(email=account)
        else:
            user = User.objects.get(username=account)

        if not user.check_password(password):
            return Response({"msg": "用户名或密码错误"}, status=status_.HTTP_400_BAD_REQUEST)

        authobj = AuthCode.objects.filter(type="one", key=account).order_by(
            "-date_expiry"
        )

        if len(authcode) == 0 and authobj.value != authcode:
            return Response({"msg": "验证码错误"}, status=status_.HTTP_400_BAD_REQUEST)

        now = timezone.now()
        date_expiry = authobj[1].date_expiry
        totalseconds = (now - date_expiry).total_seconds()
        logger.info(
            {"now": now, "date_expiry": date_expiry, "totalseconds": totalseconds}
        )

        if totalseconds > 0:
            return Response({"msg": "验证码失效"}, status=status_.HTTP_400_BAD_REQUEST)

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
    permission_classes = (IsOwnerOrReadOnly,)

    def get(self, request, id=None, *args, **kwargs):
        request.session.flush()
        return Response(status=status_.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def AnyUserRegisterView(request):
    ''' 注册 Any用户 '''
    import django_redis
    req_data = request.data
    method = request.query_params.get("method",None)
    if method is None:
       return Response({'msg':['缺少 method 参数']},status=status_.HTTP_400_BAD_REQUEST)

    if method == 'cell':
      #  手机注册
      serializer = AnyUserRegisterCellSerializer(data=req_data)
      serializer.is_valid(raise_exception=True)

    elif method == 'email':
      #  邮箱注册
      serializer = AnyUserRegisterEmailSerializer(data=req_data)
      serializer.is_valid(raise_exception=True)

    else:
       return Response({"msg":["method 参数错误，只能是 'Cell' 或 'Email'."]},status_.HTTP_400_BAD_REQUEST)

    verify_code = serializer.validated_data['code']
    # 获取 redis.conn 的 verify_code 中 key 为 code 的信息
    redis_con = django_redis.get_redis_connection('verify_code') 
    verify_method = serializer.validated_data[method]
    # 2. 检验 verify_filter 是否过期。
    if redis_con.ttl(verify_method) == -2:
      return Response({'msg':['验证码错误或已失效']},status=status_.HTTP_400_BAD_REQUEST)

    # 3. 检验验证码是否匹配。
    if  redis_con.get(verify_method).decode() != verify_code:
        return Response({'msg':['验证码错误']},status=status_.HTTP_400_BAD_REQUEST)
    
    # 4. 检验完成创建用户
    user_info = serializer.create()
    if not user_info:
      return Response({'msg':["用户已存在"]},status=status_.HTTP_400_BAD_REQUEST)
    return Response(status=status_.HTTP_201_CREATED)