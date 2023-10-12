from django.shortcuts import render
from . import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.


def index(request):
    return render(request, "home/index.html")

def about(request):
    return render(request, "home/about.html")

def loginrequest(request):
    form = forms.CustomAuthenticationForm(request, data=request.POST)
    if form.is_valid():
        usuario = form.cleaned_data.get("username")
        contraseña = form.cleaned_data.get("password")
        user = authenticate(username=usuario, password=contraseña)
        if user is not None:
            login(request, user)
            return render(request, "home/index.html", {"form": form})
    else:
        form = AuthenticationForm()
    return render(request, "home/login.html", {"form": form})