from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

from A_blogProject.utils import get_RandomString


def article_img_path(instance, filename):
    return "article/{0}/{1}{2}".format(instance.author, get_RandomString(24), filename)


# from users.models import AnyUser as User

from django.contrib.auth.models import User
from consumer.models import Consumer as Author
from django.contrib.auth.hashers import make_password, check_password

# Author.objects.create_superuser


# 文章
class Article(models.Model):
    STATUS = [
        ("original", "原创"),
        ("draft", "草稿"),
        ("reship", "转载"),
    ]
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
        db_table = "article"
        ordering = ("id", "author", "date_create")
        verbose_name = "article"
        verbose_name_plural = "articles"

    def __str__(self):
        return f"{self.id}:{self.title}:{self.user}"


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
        db_table = "Original"
        ordering = ("id", "author")
        verbose_name = "Original"
        verbose_name_plural = "Originals"

    def __str__(self):
        return f"{self.title}:{self.author}"


class Draft(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, to_field="username")
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "t_draft"
        ordering = ("id", "author", "date_create")
        verbose_name = "t_draft"
        verbose_name_plural = "t_drafts"
