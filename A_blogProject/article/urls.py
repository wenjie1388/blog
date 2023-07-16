from django.contrib import admin
from django.urls import path, re_path

from .views import (
    ArticleModelViewset,
)

urlpatterns = [
    re_path(r"^$", ArticleModelViewset.as_view({"get": "list", "post": "create"})),
    re_path(
        r"^(?P<id>.+)$/", ArticleModelViewset.as_view({"get": "list", "post": "create"})
    ),
]
