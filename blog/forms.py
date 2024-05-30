from django import forms
from .models import User
from .models import BlogPost, Category
from datetime import date
# from ckeditor.widgets import CKEditorWidget

class Formulaire(forms.ModelForm):
    title = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Titre de l'article"}), label="Titre de l'article" )
    slug = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Slug de l'article"}), label="Slug de l'article")
    # description = forms.CharField(widget=CKEditorWidget())
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Description de l'article"}), label="Description de l'article")
    author = forms.ModelChoiceField(queryset = User.objects.all(), label="Auteur", widget=forms.Select(attrs={"class": "form-control"}))
    date = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}), initial=date.today(), label="Date de Publication")
    category = forms.ModelMultipleChoiceField(label="Catégories", queryset=Category.objects.all(), widget=forms.SelectMultiple(attrs={"class": "form-control"}))
    image = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control-file"}))

    class Meta:
        model = BlogPost
        fields = ["title", "slug", "author", "description", "category", "date", "published", "image"]
