from django import forms
from . import models

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = ["nombre", "apellido", "nacimiento", "pais_origen_id"]


class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields = ["nombre", "apellido", "nacimiento", "mail", "usuario"]

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = ["usuario"]


class BlogForm(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = ["titulo", "contenido", "usuario_origen_id"]