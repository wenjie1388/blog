from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

from A_blogProject.utils import get_RandomString


def article_img_path(instance, filename):
    return "/image/article/{0}/{1}{2}".format(
        instance.id, get_RandomString(24), filename
    )


# from users.models import AnyUser as User

from django.contrib.auth.models import User
from consumer.models import Consumer as Author
from django.contrib.auth.hashers import make_password, check_password

# Author.objects.create_superuser


# 文章
class Article(models.Model):
    STATUS = [
        ("or", "原创"),
        ("dr", "草稿"),
    ]
    title = models.CharField(max_length=64, default="无标题")
    digest = models.TextField(max_length=128)
    cover = models.ImageField(
        upload_to=article_img_path, default="article/default/default.png"
    )
    body = models.TextField()
    author = models.ForeignKey(
        Author,
        verbose_name="username",
        on_delete=models.CASCADE,
        to_field="username",
        db_column="author",
    )
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    tags = models.JSONField(
        "标签",
    )
    status = models.CharField(
        _("status"), choices=STATUS, max_length=50, default="draft"
    )

    upvote = models.PositiveIntegerField(help_text="点赞量", default=0)
    collect = models.PositiveIntegerField(help_text="收藏量", default=0)
    pageviews = models.PositiveIntegerField(help_text="阅读量", default=0)
    # modified_date = models.DateTimeField('修改时间', auto_now=True)
    # category1 = models.ManyToManyField(Nav1)
    # category2 = models.ManyToManyField(Nav2)
    # 使用外键关联分类表与分类是一对多关系
    # tags = models.ManyToManyField(Tag, blank=True)
    # 使用外键关联标签表与标签是多对多关系
    # views = models.PositiveIntegerField('阅读量', default=0)
    # tui = models.ForeignKey(Tui, on_delete=models.DO_NOTHING, verbose_name='推荐位', blank=True, null=True)

    class Meta:
        db_table = "t_article"
        ordering = ("id", "author", "date_create")
        verbose_name = "t_article"
        verbose_name_plural = "t_articles"

    def __str__(self) -> str:
        return super().__str__()


class Original(models.Model):
    title = models.CharField(max_length=64)
    digest = models.TextField(max_length=128)
    cover = models.ImageField(
        upload_to=article_img_path, default="article/default/default.png"
    )
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, to_field="username")
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    tags = models.JSONField(
        "标签",
    )
    upvote = models.PositiveIntegerField(help_text="点赞量", default=0)
    collect = models.PositiveIntegerField(help_text="收藏量", default=0)
    pageviews = models.PositiveIntegerField(help_text="阅读量", default=0)
    # modified_date = models.DateTimeField('修改时间', auto_now=True)
    # category1 = models.ManyToManyField(Nav1)
    # category2 = models.ManyToManyField(Nav2)
    # 使用外键关联分类表与分类是一对多关系
    # tags = models.ManyToManyField(Tag, blank=True)
    # 使用外键关联标签表与标签是多对多关系
    # views = models.PositiveIntegerField('阅读量', default=0)
    # tui = models.ForeignKey(Tui, on_delete=models.DO_NOTHING, verbose_name='推荐位', blank=True, null=True)

    class Meta:
        db_table = "t_original"
        ordering = ("id", "author")
        verbose_name = "t_original"
        verbose_name_plural = "t_originals"

    def __str__(self):
        return f"{self.title}:{self.author}"
