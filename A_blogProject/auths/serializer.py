import random
import string
from django.utils import timezone
from rest_framework import serializers

from .models import AuthCode


AUTH_TYPE = [("one", "one")]


class AuthBaseSerializer(serializers.Serializer):
    type = serializers.ChoiceField(AUTH_TYPE)


class OneAuthSerializer(AuthBaseSerializer):
    key = serializers.CharField()

    def save(self, **kwargs):
        type = self.validated_data.get("type", "")
        key = self.validated_data.get("key", "")
        value = self.get_auth_code()
        # date_expiry = (timezone.now() + timezone.timedelta(minutes=10)).strftime(
        #     "%Y-%m-%d %H:%M:%S"
        # )
        validated_data = {
            "type": type,
            "key": key,
            "value": value,
            # "date_expiry": date_expiry,
        }
        self.instance = self.create(validated_data)

        return self.instance

    def create(self, validated_data):
        return AuthCode.objects.create(**validated_data)

    def get_auth_code(self, length=6):
        return "".join([random.choice(string.ascii_letters) for a in range(length)])


# model


class AuthModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthCode
        fields = "__all__"
