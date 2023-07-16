from django.contrib import admin
from django.urls import path, re_path

from .views import UserModelViewSet, UserLoginView, UserLogoutView

urlpatterns = [
    re_path(r"^login$", UserLoginView.as_view()),
    # re_path(r"^logout/(?P<id>.+)$", UserLogoutView.as_view()),
    re_path(r"^logout", UserLogoutView.as_view()),
    re_path(r"^$", UserModelViewSet.as_view({"get": "list", "post": "create"})),
    re_path(
        r"^(?P<id>.+)$",
        UserModelViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
    ),
]
