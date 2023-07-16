from rest_framework.serializers import Serializer, ModelSerializer

from .models import Article


class ArticleModelSerializer(ModelSerializer):
    class Meta:
        model = Article
        # exclude = ('')
        # fields = ("id", "title", "author", "date_create", "status")
        fields = "__all__"


# class Article
