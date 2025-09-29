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
        

def contains(my_map, key):
    """
    Retorna True si 'key' está en la tabla; False en caso contrario.
    Estrategia: sonda lineal desde el índice hash hasta hallar la llave
    o toparse con una celda nunca usada (key == None).
    """
    capacidad = my_map["capacity"]
    pos = mf.hash_value(my_map, key)

    for i in range(capacidad):
        casilla = (pos + i) % capacidad
        entrada = my_map["table"]["elements"][casilla]
        k = entrada["key"]

        # Celda nunca usada: ya no puede estar más adelante
        if k is None:
            return False

        if k == key:
            return True

    # Se revisó toda la tabla sin hallarla
    return False


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
    

def remove(my_map, key):
    """
    Elimina una llave del mapa (linear probing).
    En vez de dejar el cajón en None, lo marca como "__EMPTY__"
    para que la búsqueda linear siga funcionando.
    """
    capacidad = my_map["capacity"]
    pos = mf.hash_value(my_map, key)

    for i in range(capacidad):
        casilla = (pos + i) % capacidad
        entrada = my_map["table"]["elements"][casilla]

        # cajon nunca usado -> la llave no está
        if entrada["key"] is None:
            return my_map

        # encontramos la llave -> marcar como __EMPTY__
        if entrada["key"] == key:
            entrada["key"] = "__EMPTY__"
            entrada["value"] = "__EMPTY__"
            my_map["size"] -= 1
            my_map["current factor"] = my_map["size"] / capacidad
            return my_map

    return my_map


def size(my_map):
    return my_map["size"]

