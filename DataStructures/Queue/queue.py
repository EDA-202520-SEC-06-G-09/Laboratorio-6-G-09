from DataStructures.List import single_linked_list as sll

def new_queue():
    return sll.new_list()

def enqueue(my_queue, element):
    sll.add_last(my_queue, element)

def dequeue(my_queue):
    if sll.is_empty(my_queue):
        return None
    # remove_first YA devuelve el valor (no el nodo)
    return sll.remove_first(my_queue)

def peek(my_queue):
    if sll.is_empty(my_queue):
        return None
    # first_element devuelve el NODO, por eso meto el info
    return sll.first_element(my_queue)["info"]

def size(my_queue):
    return sll.size(my_queue)

def is_empty(my_queue):
    return sll.is_empty(my_queue)
