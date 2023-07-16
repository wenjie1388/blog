from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.db import models
import os
import binascii

# Create your models here.
from rest_framework.authtoken.models import Token as Token_
from consumer.models import Consumer as User


class Token(Token_):
    key = models.CharField(_("Key"), max_length=40, primary_key=True)
    user = models.OneToOneField(
        User,
        # related_name="auth_token",
        on_delete=models.CASCADE,
        verbose_name=_("User"),
    )
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        db_table = "t_token"
        ordering = ("user", "created")
        verbose_name = _("t_token")
        verbose_name_plural = _("t_tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key(self.user_id)
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(
        cls,
        user_id,
    ):
        import jwt, datetime

        salt = settings.SECRET_KEY
        # 构造Header，默认如下
        headers = {"typ": "jwt", "alg": "HS256"}
        # 构造Payload
        payload = {
            "id": user_id,  # 自定义用户ID
            "exp": datetime.datetime.utcnow()
            + datetime.timedelta(days=7),  # 设置超时时间，7 天内
        }
        token = jwt.encode(
            headers=headers, payload=payload, key=salt, algorithm="HS256"
        )

        # return binascii.hexlify(os.urandom(20)).decode()
        return token.decode()

    def __str__(self):
        return self.key
