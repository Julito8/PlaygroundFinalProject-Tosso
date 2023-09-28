from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from . import models
from . import forms

def index(request):
    perfiles = models.Perfil.objects.all()

    return render(request, "cliente/perfil.html", {"perfiles":perfiles})


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

def mostrar_blogs(request):
    blogs = models.Blog.objects.all()

    return render(request, "cliente/mostrar_blogs.html", {"blogs":blogs})

