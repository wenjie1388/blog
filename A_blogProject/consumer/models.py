from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone

from A_blogProject.utils import get_RandomString


def user_img_path(instance, filename):
    return "image/{0}/{1}{2}".format(instance.course.id, get_RandomString(24), filename)


class Consumer(AbstractBaseUser):
    username_validator = UnicodeUsernameValidator()
    cellphone = models.CharField(_("cellphone"), max_length=150, unique=True)
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), unique=True, blank=True)
    avarte = models.ImageField(
        _("avarte"),
        upload_to=user_img_path,
        default="image/default/E23A1F.jpg",
    )
    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_("是否激活"),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    abstract = models.TextField(_("abstract"), max_length=50, blank=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        db_table = "t_cosumer"
        ordering = ("id", "date_joined")
        verbose_name = "t_cosumer"
        verbose_name_plural = "t_cosumers"
