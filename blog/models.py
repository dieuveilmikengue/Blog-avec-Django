from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.name

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=300, blank=False)
    slug = models.SlugField()
    published = models.BooleanField(default=False)
    description = models.TextField()
    date = models.DateField(blank=True)

    def __str__(self) -> str:
        return self.title