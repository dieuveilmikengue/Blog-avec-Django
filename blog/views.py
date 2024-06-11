from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import BlogPost
from .models import Category
from .forms import Formulaire

# Create your views here.

def index(request):
    try:
        populaire = BlogPost.objects.all().order_by('-nbre_vues')[:1]
        context = {
                "post": BlogPost.objects.all(),
                "pop": populaire,
                "catego": Category.objects.all()
                }
    except:
        context = {
                    "message": "La page que vous cherchez n'existe pas"
                    }
    return render(request, "blog/index.html", context)

def managearticle(request):
    try:
        context = {
                "post": BlogPost.objects.all(),
                "catego": Category.objects.all()
                }
    except:
        context = {
                    "message": "La page que vous cherchez n'existe pas"
                    }
    return render(request, "blog/managearticle.html", context)

def show(request, slug):
    try:
        post = get_object_or_404(BlogPost, slug=slug)
        post.nbre_vues += 1
        post.save()
        populaire = BlogPost.objects.all().order_by('-nbre_vues')[:5]
        context = {
                    "artic": post,
                    "pop": populaire,
                    "catego": Category.objects.all()
                    }
    except:
        context = {
                    "message": "La page que vous cherchez n'existe"
                    }
    return render(request, "blog/show.html", context)

def creation(request):
    form = Formulaire(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        form = Formulaire()

    context = {
                "form": form
                }
    return render(request, "blog/creation.html", context)


# def modification(request, slug):
#     try:
#         post = get_object_or_404(BlogPost, slug=slug)
#         if request.method == "POST":
#             form = Formulaire(request.POST, request.FILES, instance=post)
#             if form.is_valid():
#                 form.save()
#                 return redirect("show", slug=slug)
#         else:
#             form = Formulaire(instance=post)

#         context = {
#                     "artic": post,
#                     "catego": Category.objects.all()
#                     }
#     except:
#         context = {
#                     "message": "La page que vous cherchez n'existe"
#                     }
#     return render(request, "blog/modification.html", {
#                     "artic": post,
#                     "catego": Category.objects.all()
#                     })


def modification(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == "POST":
            form = Formulaire(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect("managearticle")
    else:
        form = Formulaire(instance=post)

    return render(request, "blog/modification.html", {"post": post, "catego": Category.objects.all(), "form": form})

def supprime(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    post.delete()
    return redirect("managearticle")