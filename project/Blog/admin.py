from django.contrib import admin
from . import models

# Register your models here.

admin.site.site_title = "Blogs"
admin.site.site_header = "Blogging"

@admin.register(models.BlogCategoria)
class BlogCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre",)


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("titulo", "contenido", "fecha_actualizacion", "descripcion_corta", "usuario_origen_id")
    list_display_links = ("titulo",)
    search_fields = ("titulo",)
    ordering = ("categoria", "titulo")
    list_filter = ("categoria",)
    date_hierarchy = ("fecha_actualizacion")
