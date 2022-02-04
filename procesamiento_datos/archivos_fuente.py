#importar librerias necesarias en este caso requests, json y datetime
import requests 
import json 
from datetime import datetime

#variable para obtener la fecha actual
hoy = str(datetime.today().date()) #se parsea la fecha a un formato string

def get_cinema_data():
    """hace un get a la api de datos abiertos y lo guarda en un archivo json"""
    url = "http://datos.gob.ar/api/3/action/datastore_search?resource_id=cultura_392ce1a8-ef11-4776-b280-6f1c7fae16ae"
    r = requests.get(url)
    cinema_data  = r.json()
    return cinema_data 

def get_museum_data():
    """hace un get a la api de datos abiertos y lo guarda en un archivo json"""
    url = "http://datos.gob.ar/api/3/action/datastore_search?resource_id=cultura_4207def0-2ff7-41d5-9095-d42ae8207a5d"
    r = requests.get(url)
    museum_data  = r.json()
    return museum_data

def get_library_data():
    """hace un get a la api de datos abiertos y lo guarda en un archivo json"""
    url = "http://datos.gob.ar/api/3/action/datastore_search?resource_id=cultura_01c6c048-dbeb-44e0-8efa-6944f73715d7"
    r = requests.get(url)
    library_data  = r.json()
    return library_data

def get_all_data():
    """ejecuta todas las funciones que obtienen los datos de la api"""
    get_cinema_data()
    get_museum_data()
    get_library_data()

def save_cinema_data():
    """crea un archivo json y graba en el fichero la informacion de la peticion get"""
    with open('data/cine/2022-febrero/cines-'+hoy+'.json','w') as f1:
        json.dump(get_cinema_data(), f1)

def save_museum_data():
    """crea un archivo json y graba en el fichero la informacion de la peticion get"""
    with open('data/museo/2022-febrero/museos-'+hoy+'.json','w') as f2:
        json.dump(get_museum_data(), f2)

def save_library_data():
    """crea un archivo json y graba en el fichero la informacion de la peticion get"""
    with open('data/biblioteca/2022-febrero/bibliotecas-'+hoy+'.json','w') as f3:
        json.dump(get_library_data(), f3)

def save_all_data():
    """ejecuta todas las funciones que crean un archivo de cada categoria"""
    save_cinema_data()
    save_museum_data()
    save_library_data()

def get_source_files():
    """funcion principal que ejecuta la obtencion y creacion de archivos json"""
    get_all_data()
    save_all_data()

get_source_files() #ejecución final