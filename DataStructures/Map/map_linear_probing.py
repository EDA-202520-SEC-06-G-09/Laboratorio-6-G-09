from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as mpe
from DataStructures.List import array_list as arl
import random


def new_map(num_elements, load_factor, prime=109345121):
    llave = None
    valor = None
    capacidad =  mf.next_prime(int(num_elements/ load_factor))   
    scale = random.randint(1, prime)
    shift = random.randint(0, prime)
    
    tabla = arl.new_list()
    
    for i in range(capacidad):
        entradas = mpe.new_map_entry(llave, valor)
        arl.add_last(tabla, entradas)
    
    mapa = {
        "prime":prime,
        "capacity": capacidad, 
        "scale": scale, 
        "shift": shift,
        "table": tabla,
        "current factor": 0, 
        "limit factor" : load_factor, 
        "size": 0 
        
    }
    
    return mapa

def put(my_map, key, value):
    
    capacidad = my_map["capacity"]
    pos = mf.hash_value(my_map, key)
    
    for i in range(0, capacidad):
        casilla = (pos + i) % capacidad
        entradas = my_map["table"]["elements"][casilla]
        
        if entradas["key"] == key:
            mpe.set_value(entradas, value)
            return my_map
        
        if entradas["key"] == None:
            n_entrada = mpe.new_map_entry(key, value)
            my_map["table"]["elements"][casilla] = n_entrada
            my_map["size"] += 1
            my_map["current factor"] = my_map["size"] / capacidad
            
            return my_map
        

def contains():
    pass

def get():
    pass

def remove():
    pass

def size ():
    pass

