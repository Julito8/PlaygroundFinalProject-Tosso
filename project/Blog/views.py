from django.shortcuts import render
from . import models, forms
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class BlogCategoriaList(ListView):
    model = models.BlogCategoria

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
