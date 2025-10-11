"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones
 *
 * Dario Correal
 """

import os
import csv
import time
import tracemalloc
from DataStructures.List import array_list as al
from DataStructures.Map import map_linear_probing as lp
from DataStructures.Map import map_separate_chaining as sc


# TODO LISTO Realice la importación del mapa linear probing
# TODO lISTO Realice la importación de ArrayList como estructura de datos auxiliar para sus requerimientos
# TODO LISTO Realice la importación del mapa separate chaining


data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Data')

def new_logic():
    """
    Inicializa el catálogo de libros. Crea una lista vacía para guardar
    los libros y utiliza tablas de hash para almacenar los datos restantes con diferentes índices
    utilizando linear probing como tipo de tabla de hash
    """
    catalog = {"books": None,
               "books_by_id": None,
               "books_by_year_author":None,
               "books_by_authors": None,
               "tags": None,
               "book_tags": None}

    #Lista que contiene la totalidad de los libros cargados
    catalog['books'] = al.new_list()

    #Tabla de Hash que contiene los libros indexados por good_reads_book_id  
    #(good_read_id -> book)
    catalog['books_by_id'] = lp.new_map(1000,0.7) #TODO LISTO completar la creación del mapa

    #Tabla de Hash con la siguiente pareja llave valor: (author_name -> List(books))
    catalog['books_by_authors'] = lp.new_map(1000,0.7) #TODO LISTO completar la creación del mapa

    #Tabla de Hash con la siguiente pareja llave valor: (tag_name -> tag)
    catalog['tags'] = lp.new_map(1000,0.7) #TODO LISTO completar la creación del mapa

    #Tabla de Hash con la siguiente pareja llave valor: (tag_id -> book_tags)
    catalog['book_tags'] = lp.new_map(1000,0.7)

    #Tabla de Hash principal que contiene sub-mapas dentro de los valores
    #con la siguiente representación de la pareja llave valor: (author_name -> (original_publication_year -> list(books)))
    catalog['books_by_year_author'] = lp.new_map(1000,0.7) #TODO completar la creación del mapa
    
    return catalog

#  -------------------------------------------------------------
# Funciones para la carga de datos
#  -------------------------------------------------------------

#TODO LISTO incorporar las funciones para toma de tiempo y memoria
    

def load_data(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    books, authors = load_books(catalog)
    tag_size = load_tags(catalog)
    book_tag_size = load_books_tags(catalog)
    return books, authors,tag_size,book_tag_size


def load_books(catalog):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    booksfile = os.path.join(data_dir, 'books.csv')
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for book in input_file:
        add_book(catalog, book)
    return book_size(catalog), author_size(catalog)


def load_tags(catalog):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    tagsfile = os.path.join(data_dir, 'tags.csv')
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for tag in input_file:
        add_tag(catalog, tag)
    return tag_size(catalog)


def load_books_tags(catalog):
    """
    Carga la información que asocia tags con libros.
    """
    bookstagsfile = os.path.join(data_dir, 'book_tags-small.csv')
    input_file = csv.DictReader(open(bookstagsfile, encoding='utf-8'))
    for booktag in input_file:
        add_book_tag(catalog, booktag)
    return book_tag_size(catalog)


def new_tag(name, id):
    """
    Esta estructura almancena los tags utilizados para marcar libros.
    """
    tag = {"name": "", "tag_id": ""}
    tag['name'] = name
    tag['tag_id'] = id
    return tag


def new_book_tag(tag_id, book_id, count):
    """
    Esta estructura crea una relación entre un tag y
    los libros que han sido marcados con dicho tag.
    """
    book_tag = {'tag_id': tag_id, 'book_id': book_id,'count':count}
    return book_tag

#  -----------------------------------------------   
#  Funciones para agregar informacion al catalogo
#  -----------------------------------------------

def add_book(catalog, book):
    """
    Adiciona un libro al mapa de libros.
    Además, guarda la información de los autores en las tablas de hash correspondientes
    """
    # Se adiciona el libro a la lista general de libros
    al.add_last(catalog['books'], book)
    # Se adiciona el libro a la tabla de hash indexada por goodreads_book_id
    lp.put(catalog['books_by_id'],book['goodreads_book_id'], book)
    # Se obtienen los autores del libro
    authors = book['authors'].split(",")
    # Para cada autor, se agrega en la tabla de hash indexada por autores y 
    # en las tablas de hash indexadas por autor y por año de publicación
    for author in authors:
        add_book_author(catalog, author.strip(), book)
        add_book_author_and_year(catalog,author.strip(), book)
    return catalog


def add_book_author(catalog, author_name, book):
    """
    Adiciona un autor al mapa de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    authors = catalog['books_by_authors']
    author_value = lp.get(authors,author_name)
    if author_value:
        #Si el autor ya se había agregado al mapa, se obtiene la lista que contiene sus libros y se agrega el nuevo elemento.
        al.add_last(author_value,book)
    else:
        #Si es un autor nuevo, se agrega al mapa teniendo como llave el nombre del autor 
        # y como valor una lista que contiene los libros asociados al autor.
        authors_books = al.new_list()
        al.add_last(authors_books,book)
        lp.put(authors,author_name,authors_books)
    return catalog


def add_book_author_and_year(catalog, author_name, book):
    """
    Adiciona un autor a los mapas indexados por autor y por año de publicación.
    Si el autor ya se había agregado: 
        - Si el año de publicación también se había agregado, se obtiene la lista en el tercer nivel y se agrega el libro.
        - Si el año de publicación no se había agregado, se agrega un nuevo mapa dentro del indice del autor y dentro de 
        este mapa se agrega una lista con el libro asociado.
    Si el autor no se había agregado:
        - Se crea el indice del nuevo autor, se crea dentro del valor el mapa asociado al nuevo año de publicación y 
        en el tercer nivel se agrega una lista como valor de este ultimo mapa con el libro asociado
    """
    books_by_year_author = catalog['books_by_year_author']
    pub_year = book['original_publication_year']
    #Si el año de publicación está vacío se reemplaza por un valor simbolico
    #TODO Completar manejo de los escenarios donde el año de publicación es vacío.
    author_value = lp.get(books_by_year_author,author_name)
    if author_value:
        pub_year_value = lp.get(author_value,pub_year)
        if pub_year_value:
            al.add_last(pub_year_value,book)
        else:
            books = al.new_list()
            al.add_last(books, book)
            pub_year_map = lp.new_map(1000,0.7)
            lp.put(pub_year_map,pub_year,book)
    else:
        # Autor nuevo: crear submapa y su lista por año
        author_map = lp.new_map(1000, 0.7)
        new_list = al.new_list()
        al.add_last(new_list, book)
        lp.put(author_map, pub_year, new_list)
        lp.put(books_by_year_author, author_name, author_map)

    return catalog


def add_tag(catalog, tag):
    """
    Adiciona un tag al mapa de tags indexado por nombre del tag
    """
    name = (tag['tag_name'] or '').strip()
    tid  = (tag['tag_id'] or '').strip()
    t = new_tag(name, tid)
    lp.put(catalog['tags'], name, t)
    return catalog


def add_book_tag(catalog, book_tag):
    """
    Adiciona un tag a la lista de tags.
    Si el book_tag ya había sido agregado:
        - Se obtiene la lista asociada al valor del indice y se agrega el book_yag
    Si el book_tag no había sido agregado:
        - Se crea el nuevo indice en el mapa y como valor se agrega una nueva lista con el book_tag asociado.
    """
    t = new_book_tag(book_tag['tag_id'], book_tag['goodreads_book_id'], book_tag['count'])
    book_tag_value = lp.contains(catalog['book_tags'],t['tag_id'])
    if book_tag_value:
        book_tag_list = lp.get(catalog['book_tags'],t['tag_id'])
        al.add_last(book_tag_list,book_tag)
    else:
        new_list = al.new_list() #TODO
        al.add_last(new_list, book_tag)
        lp.put(catalog['book_tags'], t['tag_id'], new_list)   
    return catalog

#  -------------------------------------------------------------
# Funciones de consulta
#  -------------------------------------------------------------

def get_book_info_by_book_id(catalog, good_reads_book_id):
    """
    Retorna toda la informacion que se tenga almacenada de un libro según su good_reads_id.
    """ #TODO
    start_time = getTime()
    tracemalloc.start()
    start_memory = getMemory()

    book_id_str = str(good_reads_book_id)
    book = lp.get(catalog['books_by_id'], book_id_str)

    stop_memory = getMemory()
    end_time = getTime()
    tiempo_transcurrido = deltaTime(end_time, start_time)
    memoria_usada = deltaMemory(start_memory, stop_memory)
    tracemalloc.stop()
    return book, tiempo_transcurrido, memoria_usada



def get_books_by_author(catalog, author_name):
    """
    Retorna los libros asociado al autor ingresado por párametro
    """
    start_time = getTime()
    tracemalloc.start()
    start_memory = getMemory()

    # Autor a reportar (lo que pidió el usuario)
    author = author_name

    # Lista de libros del autor (si no existe el autor, devolvemos una lista vacía)
    author_book_list = lp.get(catalog['books_by_authors'], author_name)
    if not author_book_list:
        author_book_list = al.new_list()

    stop_memory = getMemory()
    end_time = getTime()
    tiempo_transcurrido = deltaTime(end_time, start_time)
    memoria_usada = deltaMemory(start_memory, stop_memory)
    tracemalloc.stop()
    return author, author_book_list, tiempo_transcurrido, memoria_usada



def get_books_by_tag(catalog, tag_name):
    """
    Retorna el número de libros que fueron etiquetados con el tag_name especificado.
    - Se obtiene el tag asociado al tag_name dado.
    - Teniendo la información del tag, se obtiene el tag_id para relacionarlo con la estructura que contiene el 
    set de datos de book_tags y obtener más información.
    - Teniendo el tag_id, se puede obtener el goodreads_book_id de la estructura que contiene los datos 
    de book_tags y finalmente relacionarlo con los datos completos del libro.

    """ #TODO
    
    start_time = getTime()
    tracemalloc.start()
    start_memory = getMemory()

    tag_name = (tag_name or "").strip()
    book_list_by_tag = al.new_list()

    # 1) tag_name -> tag (para obtener tag_id)
    tag = lp.get(catalog['tags'], tag_name)
    if tag:
        tag_id = tag['tag_id']

        # 2) tag_id -> lista de filas en book_tags (cada fila tiene goodreads_book_id)
        rows = lp.get(catalog['book_tags'], tag_id)
        if rows:
            n = al.size(rows)
            for i in range(n):
                row = al.get_element(rows, i)
                gr_id = row['goodreads_book_id']
                # 3) id -> libro completo
                book = lp.get(catalog['books_by_id'], gr_id)
                if book:
                    al.add_last(book_list_by_tag, book)

    stop_memory = getMemory()
    end_time = getTime()
    tiempo_transcurrido = deltaTime(end_time, start_time)
    memoria_usada = deltaMemory(start_memory, stop_memory)
    tracemalloc.stop()
    # 3 valores (lo que espera view.py)
    return book_list_by_tag, tiempo_transcurrido, memoria_usada



def get_books_by_author_pub_year(catalog, author_name, pub_year):
    """
    - Se obtiene el mapa asociado al author_name dado
    - Si el author existe, se obtiene el mapa asociado al año de publicación
    Retorna los libros asociados a un autor y un año de publicación específicos
    """
    start_time = getTime()
    tracemalloc.start()
    start_memory = getMemory()

    # Normalizaciones
    author_key = (author_name or "").strip()
    year_key = str(pub_year).strip() if pub_year is not None else ""

    if year_key == "" or year_key.lower() == "none":
        year_key = "Unknown"

    # Generamos candidatos para el año (1937, 1937.0) por cómo vienen los CSV
    year_candidates = [year_key]
    if year_key.endswith(".0"):
        year_candidates.append(year_key[:-2])          # "1937.0" -> "1937"
    elif year_key.isdigit():
        year_candidates.append(year_key + ".0")        # "1937"   -> "1937.0"

    resultado = al.new_list()

    author_map = lp.get(catalog['books_by_year_author'], author_key)
    if author_map:
        found = None
        for y in year_candidates:
            lst = lp.get(author_map, y)
            if lst:
                found = lst
                break
        if found:
            resultado = found  # devolvemos la lista existente

    stop_memory = getMemory()
    end_time = getTime()
    tiempo_transcurrido = deltaTime(end_time, start_time)
    memoria_usada = deltaMemory(start_memory, stop_memory)
    tracemalloc.stop()
    return resultado, tiempo_transcurrido, memoria_usada



#  -------------------------------------------------------------
# Funciones utilizadas para obtener el tamaño de los mapas
#  -------------------------------------------------------------

def book_size(catalog):
    return lp.size(catalog['books_by_id'])


def author_size(catalog):
    return lp.size(catalog['books_by_authors'])


def tag_size(catalog):
    return lp.size(catalog['tags'])


def book_tag_size(catalog):
    return lp.size(catalog['book_tags'])

#  -------------------------------------------------------------
# Funciones utilizadas para obtener memoria y tiempo
#  -------------------------------------------------------------

def getTime():
    """
    Devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter() * 1000)

def getMemory():
    """
    Toma una muestra de la memoria alocada en un instante de tiempo
    """
    return tracemalloc.take_snapshot()

def deltaTime(end, start):
    """
    Devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    return float(end - start)

def deltaMemory(start_memory, stop_memory):
    """
    Calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en kBytes
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = sum(stat.size_diff for stat in memory_diff) / 1024.0
    return delta_memory