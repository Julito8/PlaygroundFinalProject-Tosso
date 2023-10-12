from django import forms
from . import models

class BlogCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.BlogCategoria
        fields = "__all__"

        widgets= {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }


class BlogForm(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = "__all__"

        widgets= {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion_corta": forms.TextInput(attrs={"class": "form-control"}),
            "contenido": forms.TextInput(attrs={"class": "form-control"}),
        }
