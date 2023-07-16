from django.contrib import admin
from django.urls import path, include, re_path

from .views import AuthsCode

urlpatterns = [
    path("", AuthsCode.as_view()),
]
