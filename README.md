# Practica 1
## Bibliotecas
Requiere las siguientes bibliotecas que no son parte de la sdtlib de python:
* FLASK stable : ```pip install Flask```
* GETMAC 0.9.5  : ```pip install getmac```  

## Funcionamiento
Este es el flujo de la práctica:
* Correr la aplicación de flask: ```flask --app idk run```
* (Opcional) Si se quiere usar ngrok para abrir el puerto a otros dispositivos: ```ngrok http http://localhost:5000```
* (Opcional) Si se tiene un dominio permanente de ngrok: ```ngrok http 5000 --url "dominioPermanente"```
* Para enviar o recivir informacion del servidor, en otra terminal usar los comandos:
    * El comando get lleva el siguiente formato: ```python3 request.py "get"```
    * El comando post lleva el siguiente formato: ```python3 request.py "post" "nombre"```
