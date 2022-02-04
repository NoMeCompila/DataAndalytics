import requests #importar librerias necesarias en este caso solo requests

      #que se usa el jsonplaceholder que genera posts ficticios
url = "https://jsonplaceholder.typicode.com/posts" #direccion a al que se ahce la peticion

r = requests.get(url) #variable que contiene la peticion

data  = r.json()

for d in data:
    print(d.keys())
    print('-------------------------')

