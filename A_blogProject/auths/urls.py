from django.contrib import admin
from django.urls import path, include, re_path

from .views import AuthsViewset

urlpatterns = [
    re_path(r"^$", AuthsViewset.as_view({"get": "list", "post": "create"})),
]
