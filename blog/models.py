from django.db import models
from django.contrib.auth.models import User
from datetime import date
# from ckeditor.fields import RichTextField


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
    date = models.DateField(default=date.today,blank=True)
    image = models.ImageField(upload_to="images/", default="images/blog-1.jpg")
    nbre_vues = models.IntegerField(default=0)


    def __str__(self) -> str:
        return self.title