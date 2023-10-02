from django.db import models
from django.utils.timezone import now


# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Service Title")
    subtitle = models.CharField(max_length=200, verbose_name="subtitle")
    content = models.TextField(verbose_name="content")
    image = models.ImageField(verbose_name="image", upload_to="services")
    published = models.DateTimeField(default=now, verbose_name="published")
    created = models.DateTimeField(auto_now_add=True, verbose_name="created")
    updated = models.DateTimeField(auto_now=True, verbose_name="updated")

    class Meta:
        verbose_name = "service"
        verbose_name_plural = "services"
        ordering = ['-created']

    def __str__(self):
        return self.title
