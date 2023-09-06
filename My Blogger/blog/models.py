from django.db import models
from django.contrib.auth.models import User
import time


def image_path(instance, filename):
    name, extension = str(filename).split(".")
    ts = int(time.time())
    return f"blogs/{ts}_{instance.pk}.{extension}"


# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Blog Author",
        related_name="author_blogs",
    )
    title = models.CharField(max_length=200, verbose_name="Blog Title")
    description = models.TextField(max_length=4000, verbose_name="Blog Description")
    image = models.ImageField(upload_to=image_path, blank=True, null=True)
    published_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Blog Category",
        related_name="category_blogs",
    )

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
