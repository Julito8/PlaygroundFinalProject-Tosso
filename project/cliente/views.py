from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from . import models
from .forms import CustomUserCreationForm
from . import forms
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def perfil(request):
    perfiles = models.Perfil.objects.all()

    return render(request, "cliente/perfil.html", {"perfiles":perfiles})

@login_required
def crear_perfil(request):
    if request.method == "POST":
        form = forms.PerfilForm(request.POST) #Formulario lleno    
        if form.is_valid():
            form.save()   # guarda los datos
            return redirect("cliente:perfil")
    else:
        form = forms.PerfilForm()  #Formulario vacio
    return render(request, "cliente/crear_perfil.html", {"form":form})


def crear_usuario(request):
    if request.method == "POST":
        form = forms.UsuarioForm(request.POST) #Formulario lleno    
        if form.is_valid():
            form.save()   # guarda los datos
            return redirect("cliente:perfil")
    else:
        form = forms.UsuarioForm()  #Formulario vacio
    return render(request, "cliente/crear_usuario.html", {"form":form})


def aboutme(request):
    return render(request, "cliente/aboutme.html")

def registro(request):
    data = {
        "form": CustomUserCreationForm
    }

    if request.method == "POST":
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user= authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
            authenticated_user = login(request, user)
            if authenticated_user:
                messages.success(request, "Usuario creado correctamente")
            return redirect(to="home:index")

        data["form"] = form

    return render(request, "registration/registro.html", data)


def tu_perfil(request):
    perfiles = models.Perfil.objects.all()

    return render(request, "cliente/tu_perfil.html", {"perfiles":perfiles})




""" def crear_blog(request):
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
 """
