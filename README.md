## Crear una carpeta

- Tener Python y pylance instalados

## Crear un entorno virtual

```bash
python -m venv .venv
```

##  Crear la estructura del proyecto

- Crear la carpeta `project` (mkdir project) 
- Crear un archivo `.gitignore` poner aca lo que quiera ignorar para subir a github
- Crear un archivo `README.md` para anotar todo el proyecto
- Posicionarse en project

## Instalar django // requirements

```bash
pip install django
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

- Dentro de la app crear un archivo urls.py
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
