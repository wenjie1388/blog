from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin", admin.site.urls),
    re_path(r"^articles", include("article.urls")),
    re_path(r"^users", include("consumer.urls")),
    re_path(r"^auths", include("auths.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
