from django.db.models import Q
from django.conf import settings
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Article
from .serializer import ArticleModelSerializer
from A_blogProject.utils import Timmer

from auths.authentication import SessionAuthentication
from auths.permissions import IsOwnerOrReadOnly
from auths.pagination import PageNumberPagination


class ArticleModelViewset(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer
    authentication_classes = (SessionAuthentication,)
    pagination_class = PageNumberPagination
    permission_classes = (IsOwnerOrReadOnly,)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_queryset(self):
        queryset = self.queryset
        search = self.request.query_params.get("search", None)
        # tags = self.request.query_params.get("tags", None)
        status = self.request.query_params.get("status", None)
        # author = self.request.query_params.get("author", None)
        # page = int(self.request.query_params.get("page", 1))
        # PAGE_SIZE = settings.REST_FRAMEWORK["PAGE_SIZE"]
        order1 = self.request.query_params.get("order", "pageviews")

        if search is not None:
            queryset = queryset.filter(
                Q(title__icontains=search)
                | Q(digest__icontains=search)
                | Q(body__icontains=search)
            )
        if status is not None:
            queryset = queryset.filter(status__exact=status)
        return queryset.order_by(order1)

    def get_permissions(self):
        return super().get_permissions()

    def get_serializer_class(self):
        return super().get_serializer_class()
