from django.contrib import admin
from django.urls import path, re_path

# from rest_framework.routers import DefaultRouter

from .views import (
    ArticleModelViewset,
)

urlpatterns = [
    re_path(r"^$", ArticleModelViewset.as_view({"get": "list", "post": "create"})),
    re_path(
        r"^(?P<id>[0-9].+)$",
        ArticleModelViewset.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
    ),
]
