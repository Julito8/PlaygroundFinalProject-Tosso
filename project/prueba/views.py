from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    contexto = {"nombre": "Juli"}
    return render(request, "prueba/index.html", contexto)
