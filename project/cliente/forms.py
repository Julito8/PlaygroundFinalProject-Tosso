from django import forms
from . import models

class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields = ["nombre", "apellido", "nacimiento", "mail", "usuario"]

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = ["usuario"]


""" class BlogForm(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = ["titulo", "contenido",] """