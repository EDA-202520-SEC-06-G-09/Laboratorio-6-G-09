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
        "current_factor": 0, 
        "limit_factor" : load_factor, 
        "size": 0 
        
    }
    
    return mapa

def put():
    
    pass

def contains():
    pass

def get(my_map, key):
    n = my_map["capacity"]
    index = mf.hash_value(my_map,key)
    for i in range(n):
        entrada = arl.get_element(my_map["table"], index)
        llave = entrada["key"]
        if llave is None:
            return None
        
        if key == llave:
            return entrada["value"]
        
        index = (index +1) %n
        
    return None
    

def remove():
    pass

def size(my_map):
    return my_map["size"]

