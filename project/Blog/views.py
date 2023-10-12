from django.shortcuts import render
from . import models
from django.views.generic import ListView, DetailView
# Create your views here.

class BlogCategoriaList(ListView):
    model = models.BlogCategoria

class BlogCategoriaDetail(DetailView):
    model = models.BlogCategoria