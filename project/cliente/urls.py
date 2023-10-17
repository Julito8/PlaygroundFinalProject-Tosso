
from django.contrib import admin
from django.urls import path, include

from . import views

app_name= "cliente"

urlpatterns = [
    path("", views.perfil, name="perfil"),
    path("aboutme/", views.aboutme, name="aboutme"),
    path("registro/", views.registro, name="registro"),
    path("perfil_list/", views.PeriflList.as_view(), name="perfil_list"),

]
