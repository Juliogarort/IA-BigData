import csv
import os
from modelos.libro import Libro


# aqui usa los csv temporales, ya que usa como base el csv original para que cuando haga crud se haga sobre el temporal
DIRECTORIO_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_CSV_LIBROS = os.path.join(DIRECTORIO_BASE, "datos", "biblioLibros.csv")


def leer_libros():
# lee todos los libros del archivo csv
    if not os.path.exists(RUTA_CSV_LIBROS):
        return []
    
    libros = []
    try:
        with open(RUTA_CSV_LIBROS, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                libro = Libro.desde_diccionario(fila)
                libros.append(libro)
    except Exception as e:
        print(f"Error al leer libros: {e}")
    
    return libros


def guardar_libros(libros):
# Guarda la lista de libros en el archivo CSV.
    try:
        with open(RUTA_CSV_LIBROS, 'w', newline='', encoding='utf-8') as archivo:
# Definimos las columnas del CSV
            campos = ['id_libro', 'titulo', 'autor', 'anyo', 'n_pags', 'genero', 
                     'editorial', 'estado', 'disponible']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            
# Escribimos la cabecera
            escritor.writeheader()
            
# Escribimos cada libro
            for libro in libros:
                escritor.writerow(libro.a_diccionario())
        
        print("✓ Datos guardados correctamente")
    except Exception as e:
        print(f"Error al guardar libros: {e}")


def generar_id_libro():
# Genera un ID único para un nuevo libro

    libros = leer_libros()
    if not libros:
        return "1"
    
# Extraemos los números de los IDs existentes

    numeros = []
    for libro in libros:
        try:
            numero = int(libro.id_libro)
            numeros.append(numero)
        except:
            pass
    
# El nuevo ID será el máximo + 1

    if numeros:
        nuevo_numero = max(numeros) + 1
    else:
        nuevo_numero = 1
    
    return str(nuevo_numero)


def buscar_libro_por_id(id_libro):
# Busca un libro por su ID.

    libros = leer_libros()
    for libro in libros:
        if libro.id_libro == id_libro:
            return libro
    return None


def alta_libro():
# Registra un nuevo libro en el sistema mediante los datos introducidos por el usuario y los guarda en el csv

    print("\n=== ALTA DE LIBRO ===")
    
# Generamos automáticamente el ID
    id_libro = generar_id_libro()
    print(f"ID asignado automáticamente: {id_libro}")
    
# Solicitamos los datos del libro
    titulo = input("Título del libro: ").strip()
    if not titulo:
        print("Error: El título no puede estar vacío")
        return
    
    autor = input("Autor: ").strip()
    anyo = input("Año de publicación: ").strip()
    n_pags = input("Número de páginas: ").strip()
    genero = input("Género (novela, ensayo, poesía, etc.): ").strip()
    editorial = input("Editorial: ").strip()
    
# Estado del libro
    print("\nEstado del libro:")
    print("1. Nuevo")
    print("2. Usado")
    opcion_estado = input("Seleccione estado (1-2): ").strip()
    estado = "Nuevo" if opcion_estado == "1" else "Usado"
    
# Por defecto, un libro nuevo está disponible
    disponible = "True"
    
# Creamos el objeto Libro
    nuevo_libro = Libro(id_libro, titulo, autor, anyo, n_pags, genero, editorial, estado, disponible)
    
# Leemos los libros existentes, añadimos el nuevo y guardamos
    libros = leer_libros()
    libros.append(nuevo_libro)
    guardar_libros(libros)
    
    print(f"\n✓ Libro '{titulo}' registrado correctamente con ID {id_libro}")


def baja_libro():
# Elimina el libro que el usuario seleccione mediante su id
    print("\n=== BAJA DE LIBRO ===")
    
# Mostramos los libros disponibles
    libros = leer_libros()
    if not libros:
        print("No hay libros registrados en el sistema")
        return
    
    print("\nLibros registrados:")
    for libro in libros:
        print(f"  {libro}")
    
# Solicitamos el ID del libro a eliminar
    id_libro = input("\nIngrese el ID del libro a eliminar (o 'cancelar' para volver): ").strip()
    
    if id_libro.lower() == 'cancelar':
        return
    
# Buscamos y eliminamos el libro
    libro_encontrado = False
    libros_actualizados = []
    
    for libro in libros:
        if libro.id_libro == id_libro:
            libro_encontrado = True
# Confirmamos la eliminación
            confirmacion = input(f"¿Está seguro de eliminar '{libro.titulo}'? (si/no): ").strip().lower()
            if confirmacion == 'si':
                print(f"✓ Libro '{libro.titulo}' eliminado correctamente")
            else:
                print("Operación cancelada")
                libros_actualizados.append(libro)
        else:
            libros_actualizados.append(libro)
    
    if not libro_encontrado:
        print(f"Error: No se encontró ningún libro con ID {id_libro}")
        return
    
# Guardamos los cambios
    guardar_libros(libros_actualizados)


def modificar_libro():
# Modifica el libro que el usuario seleccione mediante su id    

    print("\n=== MODIFICAR LIBRO ===")
    
# Mostramos los libros disponibles
    libros = leer_libros()
    if not libros:
        print("No hay libros registrados en el sistema")
        return
    
    print("\nLibros registrados:")
    for libro in libros:
        print(f"  {libro}")
    
# Solicitamos el ID del libro a modificar
    id_libro = input("\nIngrese el ID del libro a modificar (o 'cancelar' para volver): ").strip()
    
    if id_libro.lower() == 'cancelar':
        return
    
# Buscamos el libro
    libro_encontrado = None
    for libro in libros:
        if libro.id_libro == id_libro:
            libro_encontrado = libro
            break
    
    if not libro_encontrado:
        print(f"Error: No se encontró ningún libro con ID {id_libro}")
        return
    
# Mostramos los datos actuales
    print(f"\nDatos actuales del libro '{libro_encontrado.titulo}':")
    print(f"1. Título: {libro_encontrado.titulo}")
    print(f"2. Autor: {libro_encontrado.autor}")
    print(f"3. Año: {libro_encontrado.anyo}")
    print(f"4. Páginas: {libro_encontrado.n_pags}")
    print(f"5. Género: {libro_encontrado.genero}")
    print(f"6. Editorial: {libro_encontrado.editorial}")
    print(f"7. Estado: {libro_encontrado.estado}")
    print(f"8. Disponible: {libro_encontrado.disponible}")
    
# Solicitamos qué campo modificar
    print("\n¿Qué campo desea modificar? (1-8, o 0 para cancelar)")
    opcion = input("Opción: ").strip()
    
    if opcion == "0":
        return
    elif opcion == "1":
        nuevo_valor = input("Nuevo título: ").strip()
        if nuevo_valor:
            libro_encontrado.titulo = nuevo_valor
    elif opcion == "2":
        nuevo_valor = input("Nuevo autor: ").strip()
        if nuevo_valor:
            libro_encontrado.autor = nuevo_valor
    elif opcion == "3":
        nuevo_valor = input("Nuevo año: ").strip()
        if nuevo_valor:
            libro_encontrado.anyo = nuevo_valor
    elif opcion == "4":
        nuevo_valor = input("Nuevo número de páginas: ").strip()
        if nuevo_valor:
            libro_encontrado.n_pags = nuevo_valor
    elif opcion == "5":
        nuevo_valor = input("Nuevo género: ").strip()
        if nuevo_valor:
            libro_encontrado.genero = nuevo_valor
    elif opcion == "6":
        nuevo_valor = input("Nueva editorial: ").strip()
        if nuevo_valor:
            libro_encontrado.editorial = nuevo_valor
    elif opcion == "7":
        print("1. Nuevo  2. Usado")
        opcion_estado = input("Nuevo estado (1-2): ").strip()
        if opcion_estado == "1":
            libro_encontrado.estado = "Nuevo"
        elif opcion_estado == "2":
            libro_encontrado.estado = "Usado"
    elif opcion == "8":
        nuevo_valor = input("¿Disponible? (True/False): ").strip()
        if nuevo_valor in ['True', 'False']:
            libro_encontrado.disponible = nuevo_valor
    else:
        print("Opción no válida")
        return
    
# Guardamos los cambios
    guardar_libros(libros)
    print("\n✓ Libro modificado correctamente")


def listar_libros():
# Muestra un listado de todos los libros registrados en el sistema

    print("\n=== LISTADO DE LIBROS ===")
    
    libros = leer_libros()
    
    if not libros:
        print("No hay libros registrados en el sistema")
        return
    
    print(f"\nTotal de libros: {len(libros)}\n")
    
    for libro in libros:
        print(f"  {libro}")
    
    print()  
