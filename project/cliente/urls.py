
from django.contrib import admin
from django.urls import path, include

from . import views

app_name= "cliente"

urlpatterns = [
    path("", views.perfil, name="perfil"),
    path("crear_perfil/", views.crear_perfil, name="crear_perfil"),
    path("aboutme/", views.aboutme, name="aboutme"),
    path("registro/", views.registro, name="registro"),
    path("perfil_list/", views.PeriflList.as_view(), name="perfil_list"),

]
