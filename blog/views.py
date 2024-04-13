from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import BlogPost
from .models import Category

# Create your views here.

def index(request):
    context = {
                "post": BlogPost.objects.all(),
                "catego": Category.objects.all(),
               "age": 25}
    return render(request, "blog/index.html", context)

def show(request, id):
    context = {
                "artic": get_object_or_404(BlogPost, pk=id)
    }
    return render(request, "blog/show.html", context)
