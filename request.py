import requests
from getmac import get_mac_address
import sys

valor = 0
name = "Rodrigo"
data = {
            "mac" : get_mac_address(),
            "valor" : valor,
            "name" : name
        }

def post():
    url = "http://localhost:5000/post"
    response = requests.post(url, json=data)
    print ("Response from server:", response.text)

def get():
    url = "http://localhost:5000/get"
    response = requests.get(url)
    print("Response from server:", response.text)

if __name__ == "__main__":
    try:
        if sys.argv[1] == "post":
            post()
        elif sys.argv[1] == "get":
            get()
        else:
            sys.exit("Inserta un argumento valido: \"get\" o \"post\"")
    except IndexError:
        sys.exit("Inserta un argumento valido: \"get()\" o \"post()\"")