import re
from rest_framework import serializers

from django.db import IntegrityError
from django_redis import get_redis_connection
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.fields import empty

from consumer.models import Consumer as User
from auths.views import (
  auth_check_captcha,
)

class LoginBase(serializers.Serializer):
    password = serializers.CharField()
    authcode = serializers.CharField()


class LoginEmail(LoginBase):
    account = serializers.EmailField()


class LoginPhone(LoginBase):
    account = serializers.RegexField("[0-9]{11}")


class LoginName(LoginBase):
    account = serializers.RegexField("[0-9a-zA-Z]{8}")


class UserLoginSerializer(serializers.Serializer):
    account = serializers.CharField()
    password = serializers.CharField()
    authcode = serializers.CharField()

    # def __new__(cls, *args, **kwargs):
    #     import re

    #     if re.search("@", kwargs["data"].get("account")):
    #         cls.account = serializers.EmailField()

    #     return super().__new__(cls, *args, **kwargs)

    # def validate(self, data):
    #     cellphone = data["cellphone"]
    #     password = data["password"]
    #     user = User.objects.filter(cellphone=cellphone)
    #     if user.count() != 1:
    #         raise serializers.ValidationError({"msg": "账号或密码错误"})

    #     if not check_password(password, user.get().password):
    #         raise serializers.ValidationError({"msg": "账号或密码错误"})
    #     return data

    # def validate_account(self, value):
    #     if re.search("", value):
    #         User_ = User.objects.filter(email=value)
    #     elif re.search("", value):
    #         User_ = User.objects.filter(cellphone=value)
    #     else:
    #         raise serializers.ValidationError(f"账号或密码错误。")

    #     if len(User_) != 1:
    #         raise serializers.ValidationError(f"账号或密码错误。")
    #     # self.user = User_[0]
    #     return value

    # 验证码校验
    # def validate_auth_code(self, value):
    #     if cache0.get(value):
    #         raise serializers.ValidationError({"msg": "验证码错误"})
    #     return value

    # def validate_password(self, value):
    #     if not self.user.check_password(value):
    #         raise serializers.ValidationError({"账号或密码错误"})
    #     return value



class UserCreateSerializer(serializers.Serializer):
    account = serializers.RegexField("[0-9]{11}")
    pwd = serializers.CharField()
    check_pwd = serializers.CharField()
    captcha = serializers.CharField()

    def save(self, **kwargs):
        validated_data = {**self.validated_data, **kwargs}
        if self.instance is None:
            self.instance = self.create(validated_data)
        return self.instance

    def validate(self, data):
        pwd = data["pwd"]
        check_pwd = data["check_pwd"]

        # 校对 密码 和 重复密码
        if pwd != check_pwd:
            raise serializers.ValidationError("请输入正确的密码")
      
        # 校对 验证码
        captcha = data["captcha"]
        account = data['account']
        redis_con = get_redis_connection("captcha")
        if not auth_check_captcha(account,captcha,redis_con):
            raise serializers.ValidationError("验证码错误或已失效")

        return data

    def create(self, validated_data):
        account = validated_data.get("cellphone")
        password = validated_data.get("password")
        
        data = {"password" :make_password(password)}        
        if re.search('@',account):
          # 邮箱注册 业务
          data['username'] = 'email_'+ account
          data['email'] = account
        else:
          data['username'] = 'phone_'+ account
          data['cellphone'] = account
          
        return User.objects.create(**data)


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            # "last_login",
            # "is_staff",
            # "is_active",
            # "is_superuser",
            # "groups",
            # "user_permissions",
        )

        # fields = "__all__"
