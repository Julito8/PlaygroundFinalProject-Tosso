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

## Instalar django

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
