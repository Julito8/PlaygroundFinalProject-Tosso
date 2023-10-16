
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name= "home"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("login/", LogoutView.as_view(template_name="home/logout.html"), name="login"),

]

urlpatterns += staticfiles_urlpatterns()

"""     path("login/", views.loginrequest, name="login"), """