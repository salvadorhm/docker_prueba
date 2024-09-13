# Repositorio de prueba de docker

Este respositorio contien una aplicación web sencilla que se va a desplegar dentro de un contenedor de docker.

## 1. Instalar paquetes

Para instalar 1 paquete en python3 se ejecuta el siguiente comando:

````bash
pip3 install web.py
````

## 2. Visualizar lista de paqutes

Para visualizar la lista de paquete instalados se ejecuta el siguiente comando:

````bash
pip freeze
````

## 3. Instalar todos los paquetes necesarios

Para instalar todos los paquetes necesarios se crear una lista en el archivo requirements.txt y se ejecuta el siguiente comando:

````bash
pip3 install -r requirements.txt
````

## 4. Generar el archivo requirements.txt

Para generar el archivo requirements.txt se redirecciona la salida del comando freeze al archivo.

````bash
pip3 freeze > requirements.txt
````

## 5. Ejecutar la aplicación web

En este ejemplo se instala [web.py](https://webpy.org/), se utiliza el código de ejemplo y se ejecuta.

````bash
python3 app.py
````

## 6. Actualizar el repositorio

Después de verificar que funciona la aplicación web se generá un commit y se actualiza el repositorio en la rama main.

````bash
git add .
git commit -m "CREATED hola mundo"
git push -u origin main
````

## 7. Iniciar sesión en DockerHub

Permite iniciar una sesión en Docker Hub para subir imagenes

````bash
docker login
````

## 8. Configurar la imagen con el nombre de usuario

Cambiar el nombre de la imagen con el nombre del usuario para poder subir la imagen al usuario con el que se inicio sesión.

````bash
docker tag salvador:v1 salvadorhm/salvador:latest
````

## 9. Subir la imagnen a DockerHub

Una vez renombrada la imagen se sube a DockerHub para tener un respaldo

````bash
docker image push salvadorhm/salvador:latest
````

## 10. Unittest a la webapp

Ejecutar las pruebas unitarias

````bash
python3 -m unittest test_web.py
````

## 11. Comandos docker

### 11.1 Listar contenedores activos

````bash
docker ps
````

### 11.2 Listar contenedores inactivos

````bash
docker ps -a
````

### 11.3 Detener contenedores activos

````bash
docker kill container_name
````

### 11.4 Crear y ejecutar un contenedor

````bash
docker run -it -p 8080:8080 image:tag
````

### 11.5 Iniciar un contenedor inactivo

````bash
docker start -i container
````
