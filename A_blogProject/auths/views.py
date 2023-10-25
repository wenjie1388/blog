from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.db.models.query import QuerySet

from rest_framework import fields
from rest_framework.response import Response
from rest_framework import generics, mixins, views
from rest_framework.viewsets import GenericViewSet

from .serializer import (
    AuthModelSerializer,
    OneAuthSerializer,
)
from .models import AuthCode
import django_redis


cache0 = django_redis.get_redis_connection("default")
from rest_framework import status


class AuthsViewset(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = AuthCode.objects.all()
    # permission_classes = (IsOwnerOrReadOnly,)
    # pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"msg": instance.value}, status=status.HTTP_201_CREATED, headers=headers
        )

    def get_serializer_class(self):
        # if self.request.thox.difference(y)
        if self.request.method == "POST":
            if self.request.data["type"] == "one":
                return OneAuthSerializer
        elif self.request.method == "GET":
            return AuthModelSerializer

    def get_queryset(self):
        if self.request.query_params is not None:
            type = self.request.query_params.get("type")
            queryset = AuthCode.objects.filter(type=type)
        else:
            queryset = self.queryset

        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()
        return queryset

    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset)

    def perform_create(self, serializer):
        return serializer.save()
      
  

# X 校对验证码 
def auth_check_captcha(key,value,redis_con) -> bool:
    if redis_con.ttl(key) == -2:
      return  False
    
    if redis_con.get(key).decode() != value:
      return False

    return True

   
