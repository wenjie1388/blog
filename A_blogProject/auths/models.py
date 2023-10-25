from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models
from django.contrib.auth.base_user import BaseUserManager

import os
import binascii

# Create your models here.
from rest_framework.authtoken.models import Token as Token_


class Token(Token_):
    key = models.CharField(_("Key"), max_length=40, primary_key=True)
    user = models.OneToOneField(
        User,
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


class AuthCode(models.Model):
    TYPE_CHOICES = [("one", "one")]
    type = models.CharField("类型", max_length=16, choices=TYPE_CHOICES, default="one")
    key = models.CharField("键", max_length=255)
    value = models.CharField("值", max_length=255)
    date_expiry = models.DateTimeField(
        "失效时间",
        # default=(timezone.now() + timezone.timedelta(minutes=10)).strftime(
        #     "%Y-%m-%d %H:%M:%S"
        # ),
        default=timezone.now() + timezone.timedelta(seconds=60 * 10),
    )

    class Meta:
        db_table = "t_authcode"
        ordering = ("id", "date_expiry")
        verbose_name = _("t_authcode")
        verbose_name_plural = _("t_authcodes")


# class UserManager(BaseUserManager):
#     use_in_migrations = True

#     def _create_user(self, username, email, password, **extra_fields):
#         """
#         Create and save a user with the given username, email, and password.
#         """
#         if not username:
#             raise ValueError("The given username must be set")
#         email = self.normalize_email(email)
#         # Lookup the real model class from the global app registry so this
#         # manager method can be used in migrations. This is fine because
#         # managers are by definition working on the real model.
#         GlobalUserModel = apps.get_model(
#             self.model._meta.app_label, self.model._meta.object_name
#         )
#         username = GlobalUserModel.normalize_username(username)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.password = make_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, username, email=None, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", False)
#         extra_fields.setdefault("is_superuser", False)
#         return self._create_user(username, email, password, **extra_fields)

#     def create_superuser(self, username, email=None, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)

#         if extra_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must have is_staff=True.")
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must have is_superuser=True.")

#         return self._create_user(username, email, password, **extra_fields)


class captcha(models.Model):
  
  key = models.CharField(max_length=100)
  value = models.CharField(max_length=200)
  date_expire = models.DateTimeField()
  
  