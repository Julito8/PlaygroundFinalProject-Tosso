from django.shortcuts import render
from . import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.


def index(request):
    return render(request, "home/index.html")

def about(request):
    return render(request, "home/about.html")
