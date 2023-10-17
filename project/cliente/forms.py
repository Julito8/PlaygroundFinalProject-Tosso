from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields = ["nombre", "apellido", "nacimiento", "mail", "biografia", "usuario"]


class CustomUserCreationForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
        