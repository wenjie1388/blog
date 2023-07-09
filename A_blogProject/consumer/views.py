from django.shortcuts import render
from django.http import JsonResponse

# from django.t
from django.views import View
from rest_framework.decorators import api_view


@api_view(["get"])
def UserLoginView(request):
    """Any用户登录"""
    # 获取请求数据，判断登录方式。若无用户信息，则进行注册
    req_params = request.query_params.dict()


from .models import Consumer as User
from django.core import serializers


class UserView(View):
    def get(self, request, id=None, *args, **kwargs):
        # req_params = request.query_params

        user = User.objects.get(id=id)

        data = {"username": user.username, "email": user.email}

        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        req_data = request.data
        return JsonResponse({"msg": req_data})
