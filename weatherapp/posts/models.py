from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Django will authomatically add an s to the class name in dashboard
class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default="fallback.png", blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None
    )  # if user deleted, delete posts

    def __str__(self):
        return self.title
