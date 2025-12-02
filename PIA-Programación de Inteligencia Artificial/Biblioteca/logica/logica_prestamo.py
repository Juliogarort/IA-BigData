import csv
import os
from datetime import datetime, timedelta
from modelos.prestamo import Prestamo
from logica import logica_libro, logica_usuario

DIRECTORIO_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_CSV_PRESTAMOS = os.path.join(DIRECTORIO_BASE, "datos", "biblioPrestamos_temp.csv")


def leer_prestamos():
# Lee todos los préstamos del archivo CSV
    if not os.path.exists(RUTA_CSV_PRESTAMOS):
        return []
    
    prestamos = []
    try:
        with open(RUTA_CSV_PRESTAMOS, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                prestamo = Prestamo.desde_diccionario(fila)
                prestamos.append(prestamo)
    except Exception as e:
        print(f"Error al leer préstamos: {e}")
    
    return prestamos


def guardar_prestamos(prestamos):
# Guarda la lista de préstamos en el archivo CSV
    try:
        with open(RUTA_CSV_PRESTAMOS, 'w', newline='', encoding='utf-8') as archivo:
            campos = ['id_prestamo', 'id_usuario', 'id_libro', 'fecha_inicio', 'fecha_fin', 'fecha_devolucion']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for prestamo in prestamos:
                escritor.writerow(prestamo.a_diccionario())
        print("✓ Datos guardados correctamente")
    except Exception as e:
        print(f"Error al guardar préstamos: {e}")


def generar_id_prestamo():
# Genera un ID único para un nuevo préstamo
    prestamos = leer_prestamos()
    if not prestamos:
        return "1"
    
    numeros = []
    for prestamo in prestamos:
        try:
            numero = int(prestamo.id_prestamo)
            numeros.append(numero)
        except:
            pass
    
    if numeros:
        nuevo_numero = max(numeros) + 1
    else:
        nuevo_numero = 1
    
    return str(nuevo_numero)


def registrar_prestamo():
    print("\n=== REGISTRAR PRÉSTAMO ===")
    
    usuarios = logica_usuario.leer_usuarios()
    if not usuarios:
        print("Error: No hay usuarios registrados. Primero debe dar de alta usuarios.")
        return
    
    libros = logica_libro.leer_libros()
    if not libros:
        print("Error: No hay libros registrados. Primero debe dar de alta libros.")
        return
    
    print("\nUsuarios registrados:")
    for usuario in usuarios:
        print(f"  {usuario}")
    
    id_usuario = input("\nIngrese el ID del usuario (o 'cancelar' para volver): ").strip()
    
    if id_usuario.lower() == 'cancelar':
        return
    
# Verificamos que el usuario exista
    usuario = logica_usuario.buscar_usuario_por_id(id_usuario)
    if not usuario:
        print(f"Error: No se encontró ningún usuario con ID {id_usuario}")
        return
    
# libros disponibles
    libros_disponibles = [libro for libro in libros if libro.disponible == "True"]
    
    if not libros_disponibles:
        print("Error: No hay libros disponibles para préstamo en este momento")
        return
    
    print("\nLibros disponibles:")
    for libro in libros_disponibles:
        print(f"  {libro}")
    
    id_libro = input("\nIngrese el ID del libro a prestar (o 'cancelar' para volver): ").strip()
    
    if id_libro.lower() == 'cancelar':
        return
    
    libro = logica_libro.buscar_libro_por_id(id_libro)
    if not libro:
        print(f"Error: No se encontró ningún libro con ID {id_libro}")
        return
    
    if libro.disponible != "True":
        print(f"Error: El libro '{libro.titulo}' no está disponible para préstamo")
        return
    
    id_prestamo = generar_id_prestamo()
    
# calculo las fechas
    fecha_inicio = datetime.now()
    fecha_fin = fecha_inicio + timedelta(days=15)  # 15 días de préstamo
    
# formateo las fechas
    fecha_inicio_str = fecha_inicio.strftime("%Y-%m-%d")
    fecha_fin_str = fecha_fin.strftime("%Y-%m-%d")
    
# creo el préstamo
    nuevo_prestamo = Prestamo(id_prestamo, id_usuario, id_libro, fecha_inicio_str, fecha_fin_str, "")
    
# guardo el préstamo
    prestamos = leer_prestamos()
    prestamos.append(nuevo_prestamo)
    guardar_prestamos(prestamos)
    
# marco el libro como no disponible
    libro.disponible = "False"
    logica_libro.guardar_libros(libros)
    
    print(f"\n✓ Préstamo registrado correctamente")
    print(f"  ID Préstamo: {id_prestamo}")
    print(f"  Usuario: {usuario.nombre} {usuario.apellidos}")
    print(f"  Libro: {libro.titulo}")
    print(f"  Fecha de inicio: {fecha_inicio_str}")
    print(f"  Fecha de devolución límite: {fecha_fin_str}")


def registrar_devolucion():
# Registra la devolución de un libro prestado
    print("\n=== REGISTRAR DEVOLUCIÓN ===")
    
# Leemos los préstamos
    prestamos = leer_prestamos()
    
# Filtramos solo los préstamos pendientes
    prestamos_pendientes = [p for p in prestamos if p.esta_pendiente()]
    
    if not prestamos_pendientes:
        print("No hay préstamos pendientes de devolución")
        return
    
# Mostramos los préstamos pendientes
    print("\nPréstamos pendientes de devolución:")
    for prestamo in prestamos_pendientes:
# Buscamos información del usuario y libro
        usuario = logica_usuario.buscar_usuario_por_id(prestamo.id_usuario)
        libro = logica_libro.buscar_libro_por_id(prestamo.id_libro)
        
        nombre_usuario = f"{usuario.nombre} {usuario.apellidos}" if usuario else "Desconocido"
        titulo_libro = libro.titulo if libro else "Desconocido"
        
        print(f"  ID: {prestamo.id_prestamo} | Usuario: {nombre_usuario} | Libro: {titulo_libro} | Límite: {prestamo.fecha_fin}")
    
# Solicitamos el ID del préstamo
    id_prestamo = input("\nIngrese el ID del préstamo a devolver (o 'cancelar' para volver): ").strip()
    
    if id_prestamo.lower() == 'cancelar':
        return
    
# Buscamos el préstamo
    prestamo_encontrado = None
    for prestamo in prestamos:
        if prestamo.id_prestamo == id_prestamo:
            prestamo_encontrado = prestamo
            break
    
    if not prestamo_encontrado:
        print(f"Error: No se encontró ningún préstamo con ID {id_prestamo}")
        return
    
    if not prestamo_encontrado.esta_pendiente():
        print(f"Error: Este préstamo ya fue devuelto el {prestamo_encontrado.fecha_devolucion}")
        return
    
# Registro la fecha de devolución
    fecha_devolucion = datetime.now().strftime("%Y-%m-%d")
    prestamo_encontrado.fecha_devolucion = fecha_devolucion
    
    guardar_prestamos(prestamos)
    
# libro como disponible
    libros = logica_libro.leer_libros()
    for libro in libros:
        if libro.id_libro == prestamo_encontrado.id_libro:
            libro.disponible = "True"
            break
    logica_libro.guardar_libros(libros)
    
    print(f"\n✓ Devolución registrada correctamente")
    print(f"  Fecha de devolución: {fecha_devolucion}")


def listar_prestamos_pendientes():
# prestamos pendientes de devolucion
    print("\n=== PRÉSTAMOS PENDIENTES ===")
    
    prestamos = leer_prestamos()
    prestamos_pendientes = [p for p in prestamos if p.esta_pendiente()]
    
    if not prestamos_pendientes:
        print("No hay préstamos pendientes de devolución")
        return
    
    print(f"\nTotal de préstamos pendientes: {len(prestamos_pendientes)}\n")
    
    for prestamo in prestamos_pendientes:

        usuario = logica_usuario.buscar_usuario_por_id(prestamo.id_usuario)
        libro = logica_libro.buscar_libro_por_id(prestamo.id_libro)
        
        nombre_usuario = f"{usuario.nombre} {usuario.apellidos}" if usuario else "Desconocido"
        titulo_libro = libro.titulo if libro else "Desconocido"
        
        print(f"  ID Préstamo: {prestamo.id_prestamo}")
        print(f"    Usuario: {nombre_usuario} (ID: {prestamo.id_usuario})")
        print(f"    Libro: {titulo_libro} (ID: {prestamo.id_libro})")
        print(f"    Fecha inicio: {prestamo.fecha_inicio}")
        print(f"    Fecha límite: {prestamo.fecha_fin}")
        print()


def listar_todos_prestamos():
# lista completa de prestamos
    print("\n=== HISTORIAL DE PRÉSTAMOS ===")
    
    prestamos = leer_prestamos()
    
    if not prestamos:
        print("No hay préstamos registrados en el sistema")
        return
    
    print(f"\nTotal de préstamos: {len(prestamos)}\n")
    
    for prestamo in prestamos:
# Buscamos información del usuario y libro
        usuario = logica_usuario.buscar_usuario_por_id(prestamo.id_usuario)
        libro = logica_libro.buscar_libro_por_id(prestamo.id_libro)
        
        nombre_usuario = f"{usuario.nombre} {usuario.apellidos}" if usuario else "Desconocido"
        titulo_libro = libro.titulo if libro else "Desconocido"
        
        estado = "PENDIENTE" if prestamo.esta_pendiente() else f"Devuelto el {prestamo.fecha_devolucion}"
        
        print(f"  ID Préstamo: {prestamo.id_prestamo}")
        print(f"    Usuario: {nombre_usuario} (ID: {prestamo.id_usuario})")
        print(f"    Libro: {titulo_libro} (ID: {prestamo.id_libro})")
        print(f"    Fecha inicio: {prestamo.fecha_inicio}")
        print(f"    Fecha límite: {prestamo.fecha_fin}")
        print(f"    Estado: {estado}")
        print()
