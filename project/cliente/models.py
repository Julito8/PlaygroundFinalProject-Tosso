from django.db import models

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField(null=True)
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}" 
    

class Usuario(models.Model):
    usuario = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.usuario} {self.contraseña}" 
    
class Perfil(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    nacimiento = models.DateField(null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}" 

class Blog(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=10000)

    def __str__(self) -> str:
        return f"{self.titulo}"
    