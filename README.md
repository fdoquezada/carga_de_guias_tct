# Proyecto Transporte

Este proyecto es una aplicación web desarrollada con Django para gestionar reguistro de tct.

## Requisitos

- Python 3.x
- Django

## crea entorno virtual
python -m venv env
source env/bin/activate  # En Windows usa `env\Scripts\activate`

## Instalación

1. Clona el repositorio a tu máquina local:

  git clone https://github.com/fdoquezada/carga_de_guias_tct.git
   cd proyecto_transporte

"# crea el proyecto" 
django-admin startproject proyecto_transporte .

"# crea la app del proyecto " 
python manage.py startapp app_transporte

"#Instala las dependencias"
pip install -r requirements.txt


2 ## corre el comando "
python manage.py runserver
Abre tu navegador web y ve a http://127.0.0.1:8000/ para ver la aplicación en funcionamiento.

"#crea las tablas de la base de datos"
python manage.py makemigrations

"#Corre las Migraciones "
python manage.py migrate

"#crea el super user para administrar desde plataforma"
python manage.py createsuperuser

## Estructura del Proyecto
proyecto_transporte/
    ├── app_transporte/
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── proyecto_transporte/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    ├── .env
    ├── .gitignore
    └── requirements.txt
