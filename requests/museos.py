#importar librerias necesarias en este caso requests, json y datetime
import requests 
import json 
from datetime import datetime

#variable para obtener la fecha actual
hoy = str(datetime.today().date()) #se parsea la fecha a un formato string

def get_cinema_data():
    """
        esta funcion guarda toda la informacion de los cines con una peticion get  
        y la guarda en una variable que luego reorna como resultado. para obtener 
        los datos se utiliza la api de datos abiertos
    """
    url = "http://datos.gob.ar/api/3/action/datastore_search?resource_id=cultura_4207def0-2ff7-41d5-9095-d42ae8207a5d"
    r = requests.get(url)
    cinema_data  = r.json()
    return cinema_data 

def get_museum_data():
    """
        esta funcion guarda toda la informacion de los museos con una peticion get  
        y la guarda en una variable que luego reorna como resultado. para obtener 
        los datos se utiliza la api de datos abiertos
    """
    url = "http://datos.gob.ar/api/3/action/datastore_search?resource_id=cultura_392ce1a8-ef11-4776-b280-6f1c7fae16ae"
    r = requests.get(url)
    museum_data  = r.json()
    return museum_data

def get_library_data():
    """
        esta funcion guarda toda la informacion de las bibliotecas con una peticion get  
        y la guarda en una variable que luego reorna como resultado. para obtener 
        los datos se utiliza la api de datos abiertos
    """
    url = "http://datos.gob.ar/api/3/action/datastore_search?resource_id=cultura_01c6c048-dbeb-44e0-8efa-6944f73715d7"
    r = requests.get(url)
    library_data  = r.json()
    return library_data

def get_all_data():
    """
        Esta funcion se encarga de ejecutar las 3 funcioneswur obtiernen los datos
        de cada categoria
    """
    get_cinema_data()
    get_museum_data()
    get_library_data()

def save_museum_data():
    """
        Esta función crea un archivo json y con ayuda de la libreria con el mismo nombre 
        escribe dentro del fichero la informacion obtenida por la peticion get
    """
    with open('data/2022-febrero/museos-'+hoy+'.json','w') as f1:
        json.dump(get_cinema_data(), f1)

def save_cinema_data():
    """
        Esta función crea un archivo json y con ayuda de la libreria con el mismo nombre 
        escribe dentro del fichero la informacion obtenida por la peticion get
    """
    with open('data/2022-febrero/cines-'+hoy+'.json','w') as f2:
        json.dump(get_museum_data(), f2)

def save_library_data():
    """
        Esta función crea un archivo json y con ayuda de la libreria con el mismo nombre 
        escribe dentro del fichero la informacion obtenida por la peticion get
    """
    with open('data/2022-febrero/bibliotecas-'+hoy+'.json','w') as f3:
        json.dump(get_library_data(), f3)

def save_all_data():
    """
        Esta función ejecuta todas las rutinas que se encargan de guardar los datos localmente 
        en archivos json    
    """
    save_cinema_data()
    save_museum_data()
    save_library_data()

def main():
    """
        funcion principal que
    """
    get_all_data()
    save_all_data()

main() #ejecución final