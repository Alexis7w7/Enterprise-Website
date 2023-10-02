from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="name")
    created = models.DateTimeField(auto_now_add=True, verbose_name="created")
    updated = models.DateTimeField(auto_now=True, verbose_name="updated")

    class Meta:
        verbose_name = ('category')
        verbose_name_plural = ('categories')
        ordering = ['-created']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="title")
    content = models.TextField(verbose_name="content")
    published = models.DateTimeField(verbose_name="published", default=now)
    image = models.ImageField(
        verbose_name="image",
        upload_to="blog",
        null=True,
        blank=True
        )
    author = models.ForeignKey(
        User,
        verbose_name="author",
        on_delete=models.CASCADE
        )
    categories = models.ManyToManyField(Category, verbose_name="categories")

    created = models.DateTimeField(auto_now_add=True, verbose_name="created")
    updated = models.DateTimeField(auto_now=True, verbose_name="updated")

    class Meta:
        verbose_name = 'enter'
        verbose_name_plural = 'enters'
        ordering = ['-created']

    def __str__(self):
        return self.title
