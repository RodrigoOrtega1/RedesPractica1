import requests
from getmac import get_mac_address
import sys

def post(name:str):
    server_data = get()
    valor = 0
    name = name
    if len(server_data) != 0:
        if server_data.get("valor") == 50:
            print(server_data.get("name") + " hizo que el valor fuera de 50! Felicidades!")
        valor = server_data.get("valor") + 1
    post_data = {
            "mac" : get_mac_address(),
            "valor" : valor,
            "name" : name
        }
    url = "http://localhost:5000/post"
    response = requests.post(url, json=post_data)
    print ("Respuesta del servidor:", response.text)

def get():
    url = "http://localhost:5000/get"
    response = requests.get(url)
    print("Respuesta del servidor:", response.text)
    return response.json()

if __name__ == "__main__":
    try:
        if sys.argv[1] == "post":
            post(sys.argv[2])
        elif sys.argv[1] == "get":
            get()
        else:
            sys.exit("Inserta un argumento valido: \"get\" o \"post\"")
    except IndexError:
        sys.exit("Inserta un argumento valido: \"get\" o \"post\", para recordar como escribir un post request checa el README")