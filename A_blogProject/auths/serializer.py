from rest_framework import serializers


class AuthCodeSerializer(serializers.Serializer):
    account = serializers.CharField()
