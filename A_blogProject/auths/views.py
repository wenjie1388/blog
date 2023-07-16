import random
import string

string.ascii_letters
random.choices
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import fields
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import AuthCodeSerializer
import django_redis


cache0 = django_redis.get_redis_connection("default")


class AuthsCode(APIView):
    def post(self, request, *args, **kwargs):
        req_data = request.data
        serializer = AuthCodeSerializer(data=req_data)
        serializer.is_valid(raise_exception=True)
        auth_code = self.get_auth_code()
        account = req_data.get("account")
        cache0.set(account, auth_code)  # 十分钟
        # cache0.set(account, auth_code, 60 * 10)  # 十分钟
        content = {**req_data, "auth_code": auth_code}
        return Response(content)

    def get_auth_code(self, length=4):
        return "".join([random.choice(string.ascii_letters) for a in range(length)])
