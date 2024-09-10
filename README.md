# Repositorio de prueba de docker

Este respositorio contien una aplicación web sencilla que se va a desplegar dentro de un contenedor de docker.

## 1. Instalar paquetes

Para instalar 1 paquete en python3 se ejecuta el siguiente comando:

````bash
$ pip3 install web.py
````

## 2. Visualizar lista de paqutes

Para visualizar la lista de paquete instalados se ejecuta el siguiente comando:

````bash
$ pip freeze
````

## 3. Instalar todos los paquetes necesarios

Para instalar todos los paquetes necesarios se crear una lista en el archivo requirements.txt y se ejecuta el siguiente comando:

````bash
$ pip3 install -r requirements.txt
````

## 4. Generar el archivo requirements.txt

Para generar el archivo requirements.txt se redirecciona la salida del comando freeze al archivo.

````bash
$ pip3 freeze > requirements.txt
````

## 5. Ejecutar la aplicación web

En este ejemplo se instala [web.py](https://webpy.org/), se utiliza el código de ejemplo y se ejecuta.

````bash
$ python3 app.py
````

