from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from . import models, forms
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Blog

# Create your views here.
class BlogCategoriaList(ListView):
    model = models.BlogCategoria

    def get_queryset(self):
        if self.request.GET.get("buscar"):
            consulta = self.request.GET.get("buscar")
            object_list = models.BlogCategoria.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.BlogCategoria.objects.all()
        return object_list

class BlogCategoriaDetail(DetailView):
    model = models.BlogCategoria

#import CreateView

class BlogCategoriaCreate(CreateView):
    model = models.BlogCategoria
    form_class = forms.BlogCategoriaForm
    success_url = reverse_lazy("blog:blogcategoria_list")

class BlogCategoriaUpdate(UpdateView):
    model = models.BlogCategoria
    form_class = forms.BlogCategoriaForm
    success_url = reverse_lazy("blog:blogcategoria_list")

class BlogCategoriaDelete(DeleteView):
    model = models.BlogCategoria
    success_url = reverse_lazy("blog:blogcategoria_list")



class BlogList(ListView):
    model = models.Blog

    def get_queryset(self):
        if self.request.GET.get("buscar"):
            consulta = self.request.GET.get("buscar")
            object_list = models.Blog.objects.filter(titulo__icontains=consulta)
        else:
            object_list = models.Blog.objects.all()
        return object_list
    
class BlogDetail(DetailView):
    model = models.Blog


class BlogCreate(CreateView):
    model = models.Blog
    form_class = forms.BlogForm
    success_url = reverse_lazy("blog:blog_list")


class BlogUpdate(UpdateView):
    model = models.Blog
    form_class = forms.BlogForm
    success_url = reverse_lazy("blog:blog_list")


class BlogDelete(DeleteView):
    model = models.Blog
    success_url = reverse_lazy("blog:blog_list")



from django.shortcuts import render
from .models import Blog  # Asegúrate de importar tu modelo correspondiente

def leer_blog(request, pk):
    # Aquí, pk contiene el valor pasado en la URL
    # Debes usar pk para recuperar el objeto del modelo apropiado
    # y luego pasarlo al contexto en tu función render
    blog = Blog.objects.get(pk=pk)  # Reemplaza "TuModelo" con el nombre de tu modelo
    return render(request, "blog/leer_blog.html", {'object_list': blog})
