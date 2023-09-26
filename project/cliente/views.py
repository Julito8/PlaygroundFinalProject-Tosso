from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from . import models
from . import forms

def index(request):
    clientes = models.Cliente.objects.all()

    return render(request, "cliente/index.html", {"clientes":clientes})

def crear(request):
    if request.method == "POST":
        form = forms.ClienteForm(request.POST) #Formulario lleno    
        if form.is_valid():
            form.save()   # guarda los datos
            return redirect("cliente:index")
    else:
        form = forms.ClienteForm()  #Formulario vacio
    return render(request, "cliente/crear.html", {"form":form})
