from django.contrib import admin
from .models import BlogPost
from .models import Category

# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ["title", "date", "published", "author"]

class CategorytAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category, CategorytAdmin)