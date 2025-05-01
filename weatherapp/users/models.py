from django.db import models


# Create your models here.
class User(models.Model):
    slug = models.SlugField()
