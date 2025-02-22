# 4 servidores, conectados en ciclo, cada computadora corre en localhost puerto 5000
# Exponer el puerto con ngrok
# 2 rutas, con una recibes y con otra mandas informacion
# Debemos usar metodos tipo get y post
# 1. Usar flask para inicializar un servidor <- aqui se escribe el codigo y se establecen las rutas
# 2. Usar ngrok para exponer el puerto 5000 a otras computadoras.
# flask --app idk run -> corre la aplicacion
# ngrok http http://localhost:5000
# ngrok http 5000 --url verbally-intent-boar.ngrok-free.app -> en otra terminal una vez la aplicacion esta corriendo, cerrar esta terminal cierra ngrok
from flask import Flask, request, jsonify
import requests

valor = 0
next_node = "http://localhost:5002"
name = "Rodrigo 1"

stored_data = {}

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def received_data():
    global valor
    data = request.get_json()

    if "valor" in data:
        valor = data["valor"] + 1
        print(f"Servidor: {name} recibe el valor {valor}")
        if valor >= 50:
            return jsonify({"message":f"Se ha llegado al valor {valor}, terminando la ejecucion"}), 200
        else:
            send_data(next_node)
            return jsonify({"message":f"Dato recibido, enviando al siguiente servidor"}), 200
    return jsonify({"message":"Error al recibir el valor"}, 400)

def send_data(next_node):
    global valor

    payload = {
        "valor": valor,
        "name": name
    }
    
    try:
        response = requests.post(next_node + "/data", json=payload)
        if response.status_code == 200:
            print(f"El servidor {name} ha enviado el valor: {valor} al servidor {next_node}")
        else:
            print(f"Error al enviar el dato al servidor {next_node}")
    except Exception as e:
        print(f"Error al enviar el valor al servidor {next_node}")

@app.route('/start', methods=['POST'])
def start():
    global valor
    print(f"{name} - empezara la ejecucion")
    send_data(next_node)
    return jsonify({"message":"ok"}, 200)

if __name__ == '__main__':
    app.run(port=5001)