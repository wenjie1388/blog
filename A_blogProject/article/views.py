from django.db.models import Q
from django.conf import settings
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import Article
from .serializer import ArticleModelSerializer
from A_blogProject.utils import Timmer
from auths.permissions import AllowAny, IsAuthenticated
from auths.authentication import SessionAuthentication


class ArticleModelViewset(ModelViewSet):
    # queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer
    authentication_classes = [SessionAuthentication]
    # authentication_classes = [BasicAuthentication, SessionAuthentication]
    # permission_classes = (IsAuthenticated,)

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
        queryset = Article.objects.all()
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
        # return queryset[page * PAGE_SIZE - PAGE_SIZE : page * PAGE_SIZE]
        return queryset.order_by(order1)

    def get_permissions(self):
        if self.request.method in ["get", "post"]:
            return AllowAny
        else:
            return IsAuthenticated

        # return super().get_permissions()

    def get_serializer_class(self):
        return super().get_serializer_class()

    # @Timmer
    # def get_action(self):
    #     action_dict = {
    #         "020101": {
    #             "queryset": Article.objects.all,
    #             "serializer_class": ArticleModelSerializer,
    #             # permission_classes = (IsAdminUser,)
    #         },
    #         "020102": {
    #             "queryset": Article.objects.all,
    #             "serializer_class": ArticleModelSerializer,
    #             # permission_classes = (IsAdminUser,)
    #         }
    #     }
