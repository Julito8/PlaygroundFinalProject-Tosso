from django.db import models
from cliente.models import Perfil
from django.utils import timezone

# Create your models here.

class BlogCategoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000, null=True, blank=True, verbose_name="descripción")

    class Meta:
        verbose_name = "categoria de blogs"
        verbose_name_plural = "categorias de blogs"
        
    def __str__(self) -> str:
        return self.nombre
    

class Blog(models.Model):
    #blogs q pertenecen a una categoria
    categoria = models.ForeignKey(BlogCategoria, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="categoría")
    titulo = models.CharField(max_length=100)
    descripcion_corta = models.CharField(max_length=200, null=True, blank=True, verbose_name="descripción corta")
    contenido = models.CharField(max_length=10000)
    usuario_origen_id = models.ForeignKey(Perfil, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="usuario")
    fecha_actualizacion = models.DateField(default=timezone.now, editable=False, verbose_name="fecha de actualización")

    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs"

    def __str__(self) -> str:
        return f"{self.titulo} {self.descripcion_corta} {self.usuario_origen_id}"