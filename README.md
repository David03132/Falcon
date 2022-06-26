# Instrucciones de ejecución

## Requisitos previos: 
+ *Python 3.7.0 o superior*
    + Link descarga: https://www.python.org/downloads/
+ *Xampp* 
    + Link descarga: https://www.apachefriends.org/es/index.html

## Creación de la base de datos: 
+ Abrir Xampp e iniciar los modulos Apache y MySQL como se ven en la [imágen](https://imgur.com/a/43jqosS).
+ Clic en el botón Admin de MySQL como se ve en la [imágen](https://imgur.com/a/gp6mNR4).
+ Crear una base de datos llamada falcon.
    + Paso 1, clic en el boton nueva [imágen](https://imgur.com/a/uaxREpc).
    + Paso 2, nombrar base de datos "falcon" y clic en crear [imágen](https://imgur.com/a/NnNkxBI).
+ No detener los procesos ni cerrar Xampp para los siguientes pasos. 


## Instalación de modulos necesarios:
+ Abrir una consola y situarse dentro de la carpeta del proyecto.
    + Paso 1, en el buscador de windows escribir "cmd" y abrir la consola [imágen](https://imgur.com/a/kiHNtee). 
    + Paso 2, situarse en la carpeta del proyecto y ejecutar los comandos del siguiente paso
+ Instalar los requisitos del proyecto con los siguientes comandos:
    + python -m pip install --upgrade pip --user
    + pip install -r requirements.txt --user
+ No cerrar la consola para el siguiente paso.

## Carga de datos y ejecución del proyecto:
+ Ejecutar los siguientes comandos:
    + python manage.py migrate
    + python manage.py loaddata data
+ Ejecutar el proyecto con el siguiente comando:
    + python manage.py runserver (Al ejecutar este comando, copia y pega el puerto que se genera en tu navegador) [imágen](https://imgur.com/a/9tzaxa2). 

## Usuarios:
+ Uuario administrador:
    + David y contraseña Kappa123
+ Usuario cliente:
    + Cliente y contraseña Kappa123
