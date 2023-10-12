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