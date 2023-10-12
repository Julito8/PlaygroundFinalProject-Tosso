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
