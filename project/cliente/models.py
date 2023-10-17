from django.db import models
from django.contrib.auth.models import User


    
class Perfil(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    nacimiento = models.CharField(max_length=50)
    biografia= models.CharField(max_length=1000, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}" 

