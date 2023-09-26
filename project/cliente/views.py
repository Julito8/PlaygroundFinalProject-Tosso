from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . import models

def index(request):
    clientes = models.Cliente.objects.all()

    return render(request, "cliente/index.html", {"clientes":clientes})
