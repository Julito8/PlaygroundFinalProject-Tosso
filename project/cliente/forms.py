from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm

class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields = ["nombre", "apellido", "nacimiento", "mail", "usuario", "biografia"]

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = ["usuario"]


""" class BlogForm(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = ["titulo", "contenido",] """

class CustomUserCreationForm(UserCreationForm):
    pass