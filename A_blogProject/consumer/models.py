from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone

from A_blogProject.utils import get_RandomString


def user_img_path(instance, filename):
    return "users/{0}/{1}{2}".format(instance.course.id, get_RandomString(24), filename)


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
    email = models.EmailField(_("email address"), unique=True, blank=True, null=True)
    avarte = models.ImageField(
        _("avarte"),
        upload_to=user_img_path,
        default="image/default/E23A1F.jpg",
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        db_table = "t_cosumer"
        ordering = ("id", "date_joined")
        verbose_name = "t_cosumer"
        verbose_name_plural = "t_cosumers"
