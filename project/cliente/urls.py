
from django.contrib import admin
from django.urls import path, include

from . import views

app_name= "cliente"

urlpatterns = [
    path("", views.index, name="index"),
    path("crear/", views.crear, name="crear"),
]