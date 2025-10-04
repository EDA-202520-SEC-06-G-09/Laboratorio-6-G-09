from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as mpe
from DataStructures.List import array_list as arl
from DataStructures.List import single_linked_list as sl
import random

def new_map():
    pass

def put():
    pass

def contains():
    pass

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
            

def remove():
    pass

def size(my_map):
    return my_map["size"]

def is_empty():
    pass

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
            
def value_set():
    pass

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
    