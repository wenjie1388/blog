from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^v1/articles/", include("article.urls")),
    re_path(r"^v1/users/", include("consumer.urls")),
    re_path(r"^v1/auths/", include("auths.urls")),
]
