
from django.contrib import admin
from django.urls import path, include

from . import views

app_name= "cliente"

urlpatterns = [
    path("", views.perfil, name="perfil"),
    path("crear_perfil/", views.crear_perfil, name="crear_perfil"),
    path("crear_usuario/", views.crear_usuario, name="crear_usuario"),
    path("crear_blog/", views.crear_blog, name="crear_blog"),
    path("mostrar_blogs/", views.mostrar_blogs, name="mostrar_blogs"),
]