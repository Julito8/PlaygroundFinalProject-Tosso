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



def perfil(request):
    return 

def crear_perfil(request):
    if request.method == "POST":
        form = forms.PerfilForm(request.POST) #Formulario lleno    
        if form.is_valid():
            form.save()   # guarda los datos
            return redirect("cliente:index")
    else:
        form = forms.PerfilForm()  #Formulario vacio
    return render(request, "cliente/crear_perfil.html", {"form":form})


def crear_usuario(request):
    if request.method == "POST":
        form = forms.UsuarioForm(request.POST) #Formulario lleno    
        if form.is_valid():
            form.save()   # guarda los datos
            return redirect("cliente:index")
    else:
        form = forms.UsuarioForm()  #Formulario vacio
    return render(request, "cliente/crear_usuario.html", {"form":form})


def crear_blog(request):
    if request.method == "POST":
        form = forms.BlogForm(request.POST) #Formulario lleno    
        if form.is_valid():
            form.save()   # guarda los datos
            return redirect("cliente:index")
    else:
        form = forms.BlogForm()  #Formulario vacio
    return render(request, "cliente/crear_blog.html", {"form":form})


def iniciar_sesion(request):
    return
