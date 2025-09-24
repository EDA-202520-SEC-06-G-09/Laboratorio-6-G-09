def new_list():
     newlist = {
         'elements': [] ,
         'size': 0, 
    }
     return newlist

def get_element(my_list, index):
  
     return my_list["elements"][index]

def is_present(my_list, element, cmp_function):

    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(my_list,element):

     my_list['elements'].insert(0,element)
     my_list['size']+=1
     return my_list
     
def add_last(my_list,element):
     
     my_list['elements'].append(element)
     my_list['size']+=1
     return my_list

def size (my_list):

    return my_list['size']

    

def first_element(my_list):
     
     return my_list['elements'][0]

     

def is_empty(my_list):
     
     if  my_list['size']==0:
          
          return True
     
     else:
          return False
  
     
def last_element(my_list):
     
     size=my_list['size']
     
     return my_list['elements'][size-1]

def delete_element(my_list,pos):
     
     my_list['elements'].pop(pos)
     my_list['size']-=1  
     
     return my_list

def remove_first(my_list):
     
     
     
     elemento=my_list['elements'].pop(0)
     
     my_list['size']-=1  
     
     return elemento
     
def remove_last(my_list):
     
     size=my_list['size']
     
     elemento=my_list['elements'].pop(size-1)
     
     my_list['size']-=1  
     
     return elemento
     
     
def insert_element(my_list,element,pos):
     
     my_list['elements'].insert(0,element)
      
     my_list['size']+=1  
     
     return my_list
          
def change_info (my_list,pos,new_info):
     
     my_list['elements'][pos]=new_info
     
     return my_list

def exchange (my_list,pos_1,pos_2):
     
     variable1=get_element(my_list,pos_1)
     variable2=get_element(my_list,pos_2)
     
     change_info(my_list,pos_1,variable2)
     change_info(my_list,pos_2,variable1)

     return my_list

def sub_list(my_list,posi,num_elements):
     
     sublista=new_list()
     
     if posi<my_list['size']:
         
          i=0 
          while i<num_elements:
          
               elemento=get_element(my_list,posi)
               
               sublista=add_last(sublista,elemento)
               
               posi+=1
               
               i+=1
               
          return sublista
     else:  
          return "IndexError: list index out of range"
     
     
def default_sort_criteria(element_1, element_2):
     is_sorted = False
     if element_1 < element_2:
          is_sorted = True
     return is_sorted


def selection_sort(my_list,sort_crit):
     n  = size(my_list)
     
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
    MergeSort para ArrayList.
    Retorna una NUEVA lista ordenada (no modifica la original).
    """
    n = size(my_list)
    if n <= 1:
        return my_list

    mid = n // 2

    # Construir mitades con TAD
    left = new_list()
    for i in range(mid):
        add_last(left, get_element(my_list, i))

    right = new_list()
    for i in range(mid, n):
        add_last(right, get_element(my_list, i))

    # Recursión
    left_ord = merge_sort(left, sort_crit)
    right_ord = merge_sort(right, sort_crit)

    return merge_lists(left_ord, right_ord, sort_crit)


def merge_lists(a, b, sort_crit):
    """
    Une dos ArrayList ordenados en uno solo ordenado.
    """
    i, j = 0, 0
    na, nb = size(a), size(b)
    result = new_list()

    while i < na and j < nb:
        ea, eb = get_element(a, i), get_element(b, j)
        if sort_crit(ea, eb):
            add_last(result, ea); i += 1
        else:
            add_last(result, eb); j += 1

    while i < na:
        add_last(result, get_element(a, i)); i += 1
    while j < nb:
        add_last(result, get_element(b, j)); j += 1

    return result
   
def quick_sort(my_list, sort_crit):

    def _partition(lst, low, high):
        pivot = get_element(lst, high)
        i = low - 1
        for j in range(low, high):
            if sort_crit(get_element(lst, j), pivot):
                i += 1
                exchange(lst, i, j)
        exchange(lst, i + 1, high)
        return i + 1

    def _quick_sort(lst, low, high):
        if low < high:
            p = _partition(lst, low, high)
            _quick_sort(lst, low, p - 1)
            _quick_sort(lst, p + 1, high)

    n = size(my_list)
    if n > 1:
        _quick_sort(my_list, 0, n - 1)
    return my_list


          
   
   


     

