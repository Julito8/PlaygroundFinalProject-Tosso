
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name= "home"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),

]

urlpatterns += staticfiles_urlpatterns()