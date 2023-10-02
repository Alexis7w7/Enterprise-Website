from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name="title")
    content = RichTextField(verbose_name="content")
    created = models.DateTimeField(auto_now_add=True, verbose_name="created")
    updated = models.DateTimeField(auto_now=True, verbose_name="updated")

    class Meta:
        verbose_name = "page"
        verbose_name_plural = "pages"

    def __str__(self):
        return self.title
