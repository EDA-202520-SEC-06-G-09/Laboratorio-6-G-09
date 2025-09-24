from DataStructures.List import list_node as ln

def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0
    }

    return newlist


def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1

    if not is_in_array:
        count = -1
    return count

def add_first(my_list, element):

    nodo = ln.new_single_node(element)
    if is_empty(my_list):
        my_list["first"] = nodo
        my_list["last"] = nodo

    else:
        nodo["next"] = my_list["first"]
        my_list["first"] = nodo

    my_list["size"] += 1

    return my_list



def add_last(my_list, element):

    nodo = ln.new_single_node(element)
    if is_empty(my_list):
        my_list["first"] = nodo
        my_list["last"] = nodo

    else:
        my_list["last"]["next"] = nodo
        my_list["last"] = nodo

    my_list["size"] += 1

    return my_list

def size(my_list):

    return my_list["size"]


def first_element(my_list):

    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')

    return my_list["first"]["info"]

def is_empty(my_list):
    vacia = False
    if my_list["first"] is None:
        vacia = True
    return vacia


def last_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')

    return my_list["last"]["info"]

def delete_element(my_list,pos):

    anterior = my_list["first"]

    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')

    if pos == 0:
        my_list["first"] = anterior["next"]
        if my_list["first"] is None:
            my_list["last"] = None
        my_list["size"] -= 1
        return my_list

    anterior = my_list["first"]
    for i in range(pos - 1):
        anterior= anterior["next"] #por que quiero el anterior a pos
    eliminar = anterior["next"]
    nuevo = eliminar["next"]
    anterior["next"] = nuevo
    eliminar["next"] = None

    if nuevo is None:
        my_list["last"] = anterior

    my_list["size"] -=1

    return my_list

def remove_first(my_list):


    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')

    primero = my_list["first"]
    my_list["size"] -= 1
    my_list["first"] = primero["next"]
    if primero["next"] is None:
        my_list["last"] = None
    primero["next"] = None
    return primero["info"]

def remove_last(my_list):

    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')

    if size(my_list) == 1:
        eliminado = my_list["first"]
        my_list["first"] = None
        my_list["last"] = None

    else:
        temp = my_list["first"]
        for i in range(size(my_list)-2):
            temp = temp["next"]

        eliminado = temp["next"]
        my_list["last"] = temp
        temp["next"] = None

    my_list ["size"] -=1

    return eliminado["info"]

def insert_element(my_list,element,pos):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    anterior = my_list["first"]
    nodo = ln.new_single_node(element)

    if pos == 0:
        nodo["next"] = anterior
        my_list["first"] = nodo
        my_list["size"] += 1
        if my_list["last"] is None:
            my_list["last"] = nodo
    else:
        for i in range(pos - 1):
            anterior = anterior["next"]

        nodo["next"] = anterior["next"]
        if anterior["next"] is None:
            my_list["last"] = nodo
        anterior["next"] = nodo
        my_list["size"] += 1


    return my_list

def change_info(my_list, pos, new_info):

    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')

    nodo = my_list["first"]
    for i in range(pos):
        nodo = nodo["next"]

    nodo["info"] = new_info

    return my_list

def exchange(my_list, pos_1, pos_2):
    if pos_1 < 0 or pos_1 >= size(my_list) or pos_2 < 0 or pos_2 >= size(my_list):
        raise Exception('IndexError: list index out of range')
    nodo1 = my_list["first"]
    nodo2 = my_list["first"]
    for i in range(pos_1):
        nodo1 = nodo1["next"]

    for i in range(pos_2):
        nodo2 = nodo2["next"]

    info1 = nodo1["info"]
    info2 = nodo2["info"]

    nodo1["info"] = info2
    nodo2["info"] = info1

    return my_list

def sub_list(my_list, pos, num_elements):
    if pos < 0 or pos >= size(my_list) or num_elements < 0 or pos + num_elements > size(my_list):
        raise Exception('IndexError: list index out of range')
    sublista = new_list()
    nodo = my_list["first"]

    for i in range(pos):
        nodo = nodo["next"]

    nuevo_nodo = ln.new_single_node(nodo["info"])
    sublista["first"] = nuevo_nodo
    sublista["last"] = nuevo_nodo
    sublista["size"] +=1


    for i in range(num_elements-1):
        nodo = nodo["next"]
        nuevo_nodo = ln.new_single_node(nodo["info"])

        sublista["last"]["next"] = nuevo_nodo
        sublista["last"] = nuevo_nodo
        sublista["size"] += 1


    return sublista


def default_sort_criteria(element1, element2):

    is_sorted = False

    if element1<element2:
        is_sorted = True

    return is_sorted

def selection_sort(my_list, sort_crit):
    n = size(my_list)
    for i in range(n-1):
        indice_minimo = i
        j = i+1

        while j < n:
            elemento1 = get_element(my_list,j)
            elemento2 = get_element(my_list,indice_minimo)
            if sort_crit(elemento1,elemento2):
               indice_minimo = j

            j += 1
        if indice_minimo != i:
            exchange(my_list, i, indice_minimo)

    return my_list

def insertion_sort (my_list, sort_crit):
    n = size(my_list)
    indice_ordenado = 1
    while indice_ordenado < n:
        j = indice_ordenado
        orden = False
        while j > 0 and not orden:
            elemento1 = get_element(my_list, j) #actual
            elemento2 = get_element(my_list, j -1)

            if sort_crit(elemento1,elemento2):
                exchange(my_list, j, j-1)
                j -= 1
            else:
                orden = True

        indice_ordenado += 1

    return my_list

def shell_sort(my_list, sort_crit):
    n = size(my_list)

    if n == 0 or n == 1:
        return my_list


    gap = n // 2

    while gap > 0:
        i = gap
        while i < n:
            j = i
            orden = False
            while j >= gap and not orden:
                a = get_element(my_list, j)
                b = get_element(my_list, j - gap)
                if sort_crit(a, b):
                    exchange(my_list, j, j - gap)
                    j -= gap
                else:
                    orden = True
            i += 1
        gap //= 2
    return my_list

def merge_sort(my_list, sort_crit):
    """
    MergeSort para SingleLinkedList.
    Retorna una NUEVA lista ordenada.
    """
    n = size(my_list)
    if n <= 1:
        return my_list

    # dividir en mitad 
    mid = n // 2
    left = new_list()
    right = new_list()

    node = my_list['first']
    k = 0
    while node is not None:
        if k < mid:
            add_last(left, node['info'])
        else:
            add_last(right, node['info'])
        node = node['next']
        k += 1

    # recursion
    left_ord = merge_sort(left, sort_crit)
    right_ord = merge_sort(right, sort_crit)

    return merge_lists_sll(left_ord, right_ord, sort_crit)


def merge_lists_sll(a, b, sort_crit):
    
    #une dos listas enlazadas simples ordenadas en una nueva lista ordenada.
    
    result = new_list()
    na, nb = size(a), size(b)

    node_a, node_b = a['first'], b['first']

    while node_a is not None and node_b is not None:
        if sort_crit(node_a['info'], node_b['info']):
            add_last(result, node_a['info'])
            node_a = node_a['next']
        else:
            add_last(result, node_b['info'])
            node_b = node_b['next']

    while node_a is not None:
        add_last(result, node_a['info'])
        node_a = node_a['next']

    while node_b is not None:
        add_last(result, node_b['info'])
        node_b = node_b['next']

    return result



import sys
sys.setrecursionlimit(10000)   # para evita RecursionError

def quick_sort(my_list, sort_crit):
    """
    QuickSort para SingleLinkedList.
    Retorna una nueva lista ordenada.
    """
    n = size(my_list)
    if n <= 1:
        return my_list

    # pivote = primer nodo
    pivot = my_list['first']['info']

    menores = new_list()
    mayores = new_list()

    node = my_list['first']['next']  # arranca en el 2do nodo
    while node is not None:
        x = node['info']
        if sort_crit(x, pivot):
            add_last(menores, x)
        else:
            add_last(mayores, x)
        node = node['next']

    # ordenar recursivamente
    menores_ord = quick_sort(menores, sort_crit)
    mayores_ord = quick_sort(mayores, sort_crit)

    # resultado final: menores + pivot + mayores
    result = new_list()

    node = menores_ord['first']
    while node is not None:
        add_last(result, node['info'])
        node = node['next']

    add_last(result, pivot)

    node = mayores_ord['first']
    while node is not None:
        add_last(result, node['info'])
        node = node['next']

    return result

