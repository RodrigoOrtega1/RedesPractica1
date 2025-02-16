# 4 servidores, conectados en ciclo, cada computadora corre en localhost puerto 5000
# Exponer el puerto con ngrok
# 2 rutas, con una recibes y con otra mandas informacion
# Debemos usar metodos tipo get y post
# 1. Usar flask para inicializar un servidor <- aqui se escribe el codigo y se establecen las rutas
# 2. Usar ngrok para exponer el puerto 5000 a otras computadoras.
# ngrok http 5000 --url verbally-intent-boar.ngrok-free.app 
from flask import Flask, request, jsonify

stored_data = {}

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/post', methods=['POST'])
def handle_post():
    global stored_data
    input_json = request.get_json(force=True)
    print ("Data from client: ", input_json)
    stored_data = input_json
    dictToReturn = {"answer" : "Recibido"}
    return jsonify(dictToReturn)
    
@app.route('/get', methods=['GET'])
def handle_get():
    return jsonify(stored_data)
