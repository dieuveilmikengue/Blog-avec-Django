from django import forms
from .models import User
from .models import BlogPost, Category
from datetime import date

class Formulaire(forms.ModelForm):
    title = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Titre de l'article"}), label="Titre de l'article" )
    slug = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Slug de l'article"}), label="Slug de l'article")
    author = forms.ModelChoiceField(queryset = User.objects.all(), label="Auteur", widget=forms.Select(attrs={"class": "form-control"}))
    date = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}), initial=date.today(), label="Date de Publication")
    category = forms.ModelMultipleChoiceField(label="Catégories", queryset=Category.objects.all(), widget=forms.SelectMultiple(attrs={"class": "form-control"}))

    class Meta:
        model = BlogPost
        fields = ["title", "slug", "author", "description", "category", "date", "published"]
        # widgets = {
        #     "title": forms.TextInput(),
        #     "slug": forms.TextInput(),
        #     "author": forms.CheckboxInput(choice=User),
        #     "description": forms.Textarea()
        # }
