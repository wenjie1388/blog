import re
from django.db import IntegrityError
import django_redis

from rest_framework import serializers
from django.contrib.auth.hashers import check_password, make_password

from consumer.models import Consumer as User

cache0 = django_redis.get_redis_connection("default")


class UserLoginSerializer(serializers.Serializer):
    # account = serializers.RegexField("(@[\w]+.com)|([0-9]{11})")
    cellphone = serializers.RegexField("[0-9]{11}")
    password = serializers.CharField()
    # auth_code = serializers.CharField()

    def validate(self, data):
        cellphone = data["cellphone"]
        password = data["password"]

        user = User.objects.filter(cellphone=cellphone)

        if user.count() != 1:
            raise serializers.ValidationError({"msg": "账号或密码错误"})

        if not check_password(password, user.get().password):
            raise serializers.ValidationError({"msg": "账号或密码错误"})
        return data

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
    cellphone = serializers.RegexField("[0-9]{11}")
    password = serializers.CharField()
    check_password = serializers.CharField()
    # auth_code = serializers.CharField()

    def validate_cellphone(self, value):
        if User.objects.filter(cellphone=value).count() != 0:
            raise serializers.ValidationError("用户已注册")
        return value

    # def validate_auth_code(self, value):
    #     if cache0.get(value) == -2:
    #         raise serializers.ValidationError("验证码失效")
    #     return value

    def validate(self, data):
        cellphone = data["cellphone"]
        password = data["password"]
        check_password = data["check_password"]
        # auth_code = data["auth_code"]

        if password != check_password:
            raise serializers.ValidationError("请输入正确的密码")

        # if cache0.get(cellphone).decode() != auth_code:
        #     raise serializers.ValidationError("验证码错误")
        return data

    def create(self, validated_data):
        cellphone = validated_data.get("cellphone")
        password = validated_data.get("password")

        data = {
            "username": cellphone,
            "password": make_password(password),
            "cellphone": cellphone,
        }
        return User.objects.create(**data)


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("password", "last_login", "is_staff", "is_active")

        # fields = "__all__"
