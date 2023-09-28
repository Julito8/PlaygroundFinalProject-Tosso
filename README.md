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
    path("", include("prueba.urls"))
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


actualizar

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

- Ir a urls.py dentro de home e importar 
```bash
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
```
Luego agregar
```bash
urlpatterns += staticfiles_urlpatterns()
```

- cambiar el nombre de nuestro index.html por otro y el archivo bajado de bootstrap ponerle index.html

en index.html:
ponerlo en español y
```bash
{% load static %}

        <title>La caja de Pandora</title>
        <!-- Favicon-->
        <link rel="icon" type="image/x-icon" href="{% static 'home/asstes/favicon.ico' %}" />
        <!-- Core theme CSS (includes Bootstrap)-->
        <link href="{% static 'home/css/styles.css' %}" rel="stylesheet" />
```
- Cambia index.html por base.html y base.html por otro nombre(base2.html)
e index_viejo.html lo vuelve a index.html
borra base2.html

- En base.html encierra con bloques creados en index.html de esta manera

```bash
        <!-- Page Content-->
        <div class="container px-4 px-lg-5">
            {% block title %}
                
            {% endblock title %}
            <!-- Heading Row-->
            <div class="row gx-4 gx-lg-5 align-items-center my-5">
                <div class="col-lg-7"><img class="img-fluid rounded mb-4 mb-lg-0" src="https://dummyimage.com/900x400/dee2e6/6c757d.jpg" alt="..." /></div>
                <div class="col-lg-5">
                    <h1 class="font-weight-light">Business Name or Tagline</h1>
                    <p>This is a template that is great for small businesses. It doesn't have too much fancy flare to it, but it makes a great use of the standard Bootstrap core components. Feel free to use this template for any project you want!</p>
                    <a class="btn btn-primary" href="#!">Call to Action!</a>
                </div>
            </div>
            {% block content %}
             <!-- Call to Action-->
                    <div class="card text-white bg-secondary my-5 py-4 text-center">
                        <div class="card-body"><p class="text-white m-0">This call to action card is a great place to showcase some important information or display a clever tagline!</p></div>
                    </div>
                    <!-- Content Row-->
                    <div class="row gx-4 gx-lg-5">
                        <div class="col-md-4 mb-5">
                            <div class="card h-100">
                                <div class="card-body">
                                    <h2 class="card-title">Card One</h2>
                                    <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Rem magni quas ex numquam, maxime minus quam molestias corporis quod, ea minima accusamus.</p>
                                </div>
                                <div class="card-footer"><a class="btn btn-primary btn-sm" href="#!">More Info</a></div>
                            </div>
                        </div>
                        <div class="col-md-4 mb-5">
                            <div class="card h-100">
                                <div class="card-body">
                                    <h2 class="card-title">Card Two</h2>
                                    <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quod tenetur ex natus at dolorem enim! Nesciunt pariatur voluptatem sunt quam eaque, vel, non in id dolore voluptates quos eligendi labore.</p>
                                </div>
                                <div class="card-footer"><a class="btn btn-primary btn-sm" href="#!">More Info</a></div>
                            </div>
                        </div>
                        <div class="col-md-4 mb-5">
                            <div class="card h-100">
                                <div class="card-body">
                                    <h2 class="card-title">Card Three</h2>
                                    <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Rem magni quas ex numquam, maxime minus quam molestias corporis quod, ea minima accusamus.</p>
                                </div>
                                <div class="card-footer"><a class="btn btn-primary btn-sm" href="#!">More Info</a></div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Footer-->
                <footer class="py-5 bg-dark">
                    <div class="container px-4 px-lg-5"><p class="m-0 text-center text-white">Copyright &copy; Your Website 2023</p></div>
                </footer>
            {% endblock content %}
```

-Para agregar imagenes, ubico la imagen en static creando una caprta llamada imagenes, de ahi la ubico

```bash
            <!-- Heading Row-->
            <div class="row gx-4 gx-lg-5 align-items-center my-5">
                <div class="col-lg-7"><img class="img-fluid rounded mb-4 mb-lg-0" src="{% static 'home/imagenes/caja.jpg' %}" alt="..." /></div>
```

- Saca codigo lo guarda en otro archivo html y luego lo llama

```bash 
        <nav>
            {% include 'home/navbar.html' %}
        </nav>
```