from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as mpe
from DataStructures.List import array_list as arl
from DataStructures.List import single_linked_list as sl
import random

def new_map(num_elements, load_factor, prime=109345121):
    
    capacidad =  mf.next_prime(int(num_elements/ load_factor))   
    scale = random.randint(1, prime - 1)
    shift = random.randint(0, prime - 1)
    
    tabla = arl.new_list()
    
    for i in range(capacidad):
        cont_casilla = sl.new_list()
        arl.add_last(tabla, cont_casilla)
    
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


def put(my_map, key, value):
    
    capacidad = my_map["capacity"]
    pos = mf.hash_value(my_map, key)
    
    cont_casilla = my_map["table"]["elements"][pos]
    current = cont_casilla["first"]
    encontrado =  False

    
    while current is not None:
        entradas = current["info"]
        
        if entradas["key"] == key:
            mpe.set_value(entradas, value)
            encontrado = True
        
        
        current = current["next"]
        
    if encontrado == False:
        n_entrada = mpe.new_map_entry(key, value)
        sl.add_last(cont_casilla, n_entrada)
        my_map["size"] += 1
        my_map["current factor"] = my_map["size"] / capacidad
        
    return my_map

    
"""
def contains():
    pass
"""
def get(my_map,key):
    index = mf.hash_value(my_map,key)
    
    lista = arl.get_element(my_map["table"],index)
    if lista["first"] is not None:
    
        nodo = lista["first"]
        while nodo is not None:
            if mpe.get_key(nodo["info"]) == key:
                return mpe.get_value(nodo["info"])
            nodo = nodo["next"]
            
    return None
            
"""
def remove():
    pass
""" 

def size(my_map):
    return my_map["size"]

"""
def is_empty():
    pass
"""


def key_set(my_map):
    llaves = arl.new_list()
    capacidad = my_map["capacity"]
    tabla = my_map["table"]
    
    for i in range(capacidad):
        entrada = arl.get_element(tabla,i)
        if not sl.is_empty(entrada):
            nodo = entrada["first"]
            while nodo is not None:
                llave = mpe.get_key(nodo["info"])
                if llave is not None:
                    arl.add_last(llaves,llave)
                nodo = nodo["next"]
            
    return llaves

          
def value_set(my_map):
    
    valores = arl.new_list()
    capacidad = my_map["capacity"]
    tabla = my_map["table"]["elements"]
    
    for pos in range(capacidad):
        casilla = tabla[pos]
        if casilla is not None:
            siz = sl.size(casilla)
            for i in range(0, siz):
                llave = sl.get_element(casilla, i)
                valor = mpe.get_value(llave)
                arl.add_last(valores, valor)
            
    return valores


def rehash(my_map):
    tabla_antigua = my_map["table"]
    capacidad_antigua = my_map["capacity"]
    
    capacidad_nueva =  mf.next_prime(capacidad_antigua)  
    tabla_nueva = arl.new_list()
    
    for _ in range(capacidad_nueva):
        arl.add_last(tabla_nueva, sl.new_list())
        
    my_map["table"] = tabla_nueva
    my_map["capacity"] = capacidad_nueva
    my_map["size"] = 0
    
    for entrada in tabla_antigua["elements"]:
        if not sl.is_empty(entrada):
            nodo = entrada["first"]
            
            while nodo is not None:
                info = nodo["info"]
                llave = mpe.get_key(info)
                valor = mpe.get_value(info)
                if llave is not None:
                    put(my_map, llave, valor)
                nodo = nodo["next"]
    return my_map

