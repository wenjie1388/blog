from django.contrib import admin
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from .views import UserModelViewSet, UserLoginView

urlpatterns = [
    # re_path(r"^/logging$", UserLoginView.as_view()),
    # re_path(r"^logout/(?P<id>.+)$", UserLogoutView.as_view()),
    # re_path(r"^logout", UserLogoutView.as_view()),
    re_path(r"^$", UserModelViewSet.as_view({"get": "list", "post": "create"})),
    re_path(
        r"^/(?P<id>[0-9]{1,})$",
        UserModelViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
    ),
]

# router = DefaultRouter()
# router.register(r"", UserModelViewSet)
# urlpatterns = router.urls
