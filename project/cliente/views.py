from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    contexto = {"nombre": "Cliente"}
    return render(request, "cliente/index.html", contexto)
