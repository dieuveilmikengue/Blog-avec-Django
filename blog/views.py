from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import BlogPost
from .models import Category
from .forms import Formulaire

# Create your views here.

def index(request):
    try:
        context = {
                "post": BlogPost.objects.all(),
                "catego": Category.objects.all()
                }
    except:
        context = {
                    "message": "La page que vous cherchez n'existe"
                    }
    return render(request, "blog/index.html", context)

def show(request, slug):
    try:
        context = {
                    "artic": get_object_or_404(BlogPost, slug=slug),
                    "catego": Category.objects.all()
                    }
    except:
        context = {
                    "message": "La page que vous cherchez n'existe"
                    }
    return render(request, "blog/show.html", context)

def creation(request):
    form = Formulaire(request.POST or None)
    if form.is_valid():
        form.save()
        

    context = {
                "form": form
                }
    return render(request, "blog/creation.html", context)