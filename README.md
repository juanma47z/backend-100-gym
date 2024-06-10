# Proyecto Gimnasio con Django

## Descripción

Proyecto que brinda una web funcional que contiene:
- La presentacion del negocio
- Informacion de la empresa como ubicacion, redes, sociales y sus servicios.

## Arquitectura
- Paginas dinamicas:  Servicios. Contacto
- Paginas estaticas: Home, Historia, Visitanos, Registro, Ingreso

- Gestión de servicios
- Información de contacto
- Registro e inicio de sesión de usuarios

## Instalación
1- Clonar el repo:
  git clone [https://github.com/tuusuario/gimnasio-django.git](https://github.com/juanma47z/backend-100-gym.git)

2- Navegar el directorio del proyecto:
  cd gimnasio-django

3- Instalar las dependencias:
  pip install -r requirements.txt

4- Configur la base de datos:
  python manage.py migrate

5- Ejecuta el servidor
 python manage.py runserver

 ## Uso
- Accede a la página principal en http://localhost:8000
- Regístrate o inicia sesión para acceder a funciones adicionales.
- Ejecutar los test para registro y login:
  - Navega al directorio del proyecto -> cd gimnasio-django
  - Ejecuta los tests -> python manage.py test registrationN.tests.AuthTest

 ## Tecnologias
 - Lenguaje Programacion: Python
 - Framework backend: Django
 - Base de datos: SQLite

