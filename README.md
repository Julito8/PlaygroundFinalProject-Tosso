## Crear una carpeta

- Tener Python y pylance instalados

## Crear un entorno virtual

```bash
python -m venv .venv
```
lo activas cerrando y volviendo abrir la terminal o
.venv\Scripts\activate

##  Crear la estructura del proyecto

- Crear la carpeta `project` (mkdir project) 
- Crear un archivo `.gitignore` poner aca lo que quiera ignorar para subir a github
- Crear un archivo `README.md` para anotar todo el proyecto
- Posicionarse en project

## Instalar django // requirements

```bash
pip install django
```
```bash
pip install -r requirements.txt
```

## Crear el proyecto Django y ejecutar el servidor Django

```bash
cd project
django-admin startproject config .
python manage.py runserver
```

- Abrir el navegador y ejecutar el servidor Django en la dirección `127.0.0.1:8000`

## Iniciar Git

Posicionarse en la raiz del projecto (pre_entrega3)

```bash
git init
```
- Para pasar al stage 
(pasa todo)

```bash
git add .
```
o ir al control del cogigo y pasarlo ahi.

- Buena practica colocar mensaje orientador y separar commits por tema, no mezclar

- Para hacer un commit

```bash
git commit -m "mensaje"
```
o desde control de codigo.

- Para ver todos los commits

```bash
git log
```
o para verlo mas corto

```bash
git log --oneline
```

## Para subir a git

- Tocar en control de codigo o
```bash
git push
```

## Para bajar de git

- Copiar la URL y utilizar en una carpeta en terminal

```bash
git clone URL
```

## Agregar los paquetes que se necesitan para este proyecto

```bash
pip freeze >> requirements .txt
```

- Al clonar se debe instalar

```bash
pip install -r requirements.txt 
```


## DJANGO

- Crear una carpeta views.py dentro de config

```bash
ni views.py 
```
e impotamos 

```bash
from django.http import HttpResponse
```

- Creamos una funcion

```bash
def saludo(request):
    return HttpResponse("Hola desde Django")
```
- En urls.py importar todo el paquete

```bash
from . import views
```
Crear un path para esa funcion

```bash
path('saludo/', views.saludo)
```

## Ramas o Branch

Al inicia se crea la rama master. Buena practica crear otra branch para hacer cambios, luego unirla a la rama principal

- Para motrar las ramas

```bash
git branch
```
- Para crear 
```bash
git branch nombre
```
## git
- Para traer un commit
```bash
git pull
```

## APLICACIONES

- Dentro de project

```bash
django-admin startapp nombre
```
Luego ir a config, settings.py y agregar el nombre de la app a INSTALLED_APPS

- Dentro de la app crear(o copiar) un archivo urls.py
Donde van a crearse las urls dentro de la app
Creaciones que se hacen en views.py de la app

- Avisar a urls.py de project sobre las urls de las apps:
En urls.py de project

```bash
from django.urls import path, include
urlpatterns += [
    path("", include(prueba.urls))
]
```
- Agregar templates(abajo)
## Templates

- Crear una carpeta templates en la app y dentro de esta una carpeta llamada como la app. Dentro de la ultima crear un archivo index.html

dentro de index.html poner ! y apretar Tab. Armar la pagina.

- Crear una funcion con render y dirigirlo "nombre de la app"/"archivo"

```bash
def index(request):
    return render(request, "prueba/index.html")
```

- Podemos enviar valores a traves de contexto (diccionarios)

```bash
def index(request):
    contexto = {"nombre": "Juli"}
    return render(request, "prueba/index.html", contexto)
```
y en index.htlm

```bash
    <h1> {{ nombre }} </h1>
    <p>es un template</p>
```

## nombrar la aplicacion

en urls.py agregar

app_name = "nombre_de_la_app

## MODELOS

- En models.py crear clases y utilizar models.
ejemplo
```bash
class Pais(models.Model):
    nombre = models.CharField(max_length=100) #Charfield es que es un str, y el max_length es obligatorio

    def __str__(self) -> str:
        return self.nombre
```
- Para crearlo 
```bash
python manage.py makemigrations
```
En migrations se crea el modelo 0001.initial.py

## BASE DE DATOS

- Para crear una base de datos

```bash
python manage.py migrate
```
En migrations se crea el modelo 0001.initial.py

ver en db.sqlite3 los modelos y la base de datos

## Crear un superusuario

- Para poder entrar a admin se necesita crear uno

```bash
python manage.py createsuperuser
```

## Panel de usuario en admin

- Agregar el modelo creado al panel
en modelo_creado/admin.py
1. importas el modelo 
```bash
from . import models
```
2. pones
```bash
admin.site.register(models.modelo_creado)
```
Ahora se pueden agregar modelos de tipo clase a la base de datos desde el panel de usuario de admin


## aplicacion home

- crear una aplicacion o home, sacarle el admin y models, copiarle un url y nombrarla en este archivo
En este archivo va a conetner un solo html central. base.html que contiene bloques y extenderlos en los otros html

base.html :
```bash
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Caja de pandora</title>
</head>
<body>
    
    <h1> Caja de pandora </h1>
    {% block title %}
    {% endblock title %}

    {% block content %}
    {% endblock content %}


</body>
</html>
```

y para usarlo en otra parte
por ej index.hmtl

```bash
{% extends 'home/base.html' %}
   
{% block title %}
    <h2> Home </h2>
{% endblock title %}

{% block content %}
    <p> <a href="{% url 'cliente:index' %}">Clientes</a> </p>
    <p> <a href="{% url 'home:about' %}">About</a> </p> 
{% endblock content %}

```

## PLANTILLAS

- Crear un archiv forms.py en la app ( cliente)
```bash

from django import forms
from . import models

class ClienteForm(forms.ModelForm): #Una fora de crear formularios
    class Meta: #sub clase q permite ponerle nombre etc
        model = models.Cliente 
        fields = ["nombre", "apellido", "nacimiento", "pais_origen_id"]
```

- Crear una funcion en views importando el formiulario

```bash
from . import forms
from django.shortcuts import render, redirect

def crear(request):
    if request.method == "POST":
        form = forms.ClienteForm(request.POST) #Formulario lleno    
        if form.is_valid():
            form.save()   # guarda los datos
            return redirect("cliente:index")
        
    else
        form = forms.ClienteForm()  #Formulario vacio
    return render(request, "cliente/crear.html", {"form":form})

```

- Crear un html en cliente/templates llamado crear.html

```bash
{% extends 'home/base.html' %}

{% block title %}
    <h2>Crear cliente</h2>
{% endblock title %}

{% block content %}
    
    <form action="" method="post">
        {% csrf_token %}  #proteccion
        {{ form.as_p }}
        <button type="submit">Guardar</button>
    </form>

    <p><a href="{% url 'home:index' %}">Ir al incio</a></p>

{% endblock content %}
```

- Agregar el path al url de la app
```bash
urlpatterns = [
    path("", views.index, name="index"),
    path("crear/", views.crear, name="crear"),
]
```
## TEMAS

- Crear una carpeta en home static con otra carpeta home

- ir a bootstrap y descargar un tema, extraerlo y arrastrar las 3 carpteas (assets, css, js) dentro de home/static/home y el index.html, renombralo y arrastrarlo en templates de home
