import json
import os

# Ruta del archivo JSON
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOMBRE_ARCHIVO = os.path.join(BASE_DIR, "libros.json")

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def cargar_datos():
    if os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, 'r', encoding='utf-8') as archivo:
            try:
                datos = json.load(archivo)
                return datos.get("libros", [])
            except json.JSONDecodeError:
                print(f"Error: El archivo {NOMBRE_ARCHIVO} está vacío o corrompido. Se creará uno nuevo.")
                return []
    else:
        print(f"Archivo {NOMBRE_ARCHIVO} no encontrado. Se creará uno nuevo.")
        return []

def guardar_datos(libros):
    with open(NOMBRE_ARCHIVO, 'w', encoding='utf-8') as archivo:
        json.dump({"libros": libros}, archivo, indent=4, ensure_ascii=False)
    print(f"✓ Datos guardados correctamente.")

def inicializar_datos():
    libros = cargar_datos()
    if not libros:
        libros_iniciales = [
            {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez", "genero": "Ficción", "año": 1967},
            {"titulo": "El Quijote", "autor": "Miguel de Cervantes", "genero": "Clásico", "año": 1605},
            {"titulo": "1984", "autor": "George Orwell", "genero": "Ciencia Ficción", "año": 1949},
            {"titulo": "Orgullo y Prejuicio", "autor": "Jane Austen", "genero": "Romance", "año": 1813},
            {"titulo": "La Sombra del Viento", "autor": "Carlos Ruiz Zafón", "genero": "Misterio", "año": 2001},
            {"titulo": "El Código Da Vinci", "autor": "Dan Brown", "genero": "Thriller", "año": 2003},
            {"titulo": "Harry Potter y la Piedra Filosofal", "autor": "J.K. Rowling", "genero": "Fantasía", "año": 1997},
            {"titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "genero": "Fábula", "año": 1943},
            {"titulo": "Crimen y Castigo", "autor": "Fiódor Dostoyevski", "genero": "Drama", "año": 1866},
            {"titulo": "Los Pilares de la Tierra", "autor": "Ken Follett", "genero": "Histórica", "año": 1989}
        ]
        guardar_datos(libros_iniciales)
        print(f"✓ Archivo de libros creado con 10 libros iniciales.")
        return libros_iniciales
    return libros

def mostrar_libro(libro):
    print(f"Título: {libro['titulo']}")
    print(f"Autor: {libro['autor']}")
    print(f"Género: {libro['genero']}")
    print(f"Año: {libro['año']}")

def filtrar_por_genero(genero):
    libros = cargar_datos()
    encontrados = [l for l in libros if l["genero"].lower() == genero.lower()]
    if encontrados:
        print(f"\n--- Libros del género '{genero}': ---")
        for l in encontrados:
            mostrar_libro(l)
            print("-" * 40)
    else:
        print(f"✗ No se encontraron libros del género '{genero}'.")

def filtrar_por_autor(autor):
    libros = cargar_datos()
    encontrados = [l for l in libros if autor.lower() in l["autor"].lower()]
    if encontrados:
        print(f"\n--- Libros del autor '{autor}': ---")
        for l in encontrados:
            mostrar_libro(l)
            print("-" * 40)
    else:
        print(f"✗ No se encontraron libros del autor '{autor}'.")

def listar_libros_recientes(anios=5):
    libros = cargar_datos()
    # Año actual
    from datetime import datetime
    actual = datetime.now().year
    recientes = [l for l in libros if actual - l["año"] <= anios and actual >= l["año"]]
    if recientes:
        print(f"\n--- Libros publicados en los últimos {anios} años: ---")
        for l in recientes:
            mostrar_libro(l)
            print("-" * 40)
    else:
        print(f"✗ No se encontraron libros recientes (últimos {anios} años).")

def agregar_libro():
    titulo = input("Ingrese el título del libro: ").strip()
    autor = input("Ingrese el autor del libro: ").strip()
    genero = input("Ingrese el género del libro: ").strip()
    while True:
        try:
            año = int(input("Ingrese el año de publicación: "))
            if año > 0:
                break
            else:
                print("✗ El año debe ser mayor a 0.")
        except ValueError:
            print("✗ Ingrese un número entero válido.")

    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "año": año
    }

    libros = cargar_datos()
    libros.append(nuevo_libro)
    guardar_datos(libros)
    print(f"✓ Libro '{titulo}' agregado correctamente.")

def mostrar_menu():
    print(f"\n╔" + "═" * 32 + "╗")
    print(f"║      Catálogo de Libros        ║")
    print(f"╚" + "═" * 32 + "╝")
    print(f"1. Filtrar libros por género")
    print(f"2. Filtrar libros por autor")
    print(f"3. Listar libros recientes")
    print(f"4. Agregar nuevo libro")
    print(f"5. Salir")
    print(f"" + "=" * 34 + f"")

if __name__ == "__main__":
    libros_actuales = inicializar_datos()

    while True:
        limpiar_consola()
        mostrar_menu()
        try:
            opcion = input(f"\nSeleccione una opción (1-5): ")
        except KeyboardInterrupt:
            print(f"\n\nSaliendo del catálogo de libros. ¡Hasta luego!")
            break

        if opcion == '1':
            genero = input("Ingrese el género a filtrar: ").strip()
            filtrar_por_genero(genero)
        elif opcion == '2':
            autor = input("Ingrese el autor a filtrar: ").strip()
            filtrar_por_autor(autor)
        elif opcion == '3':
            try:
                anios = int(input("¿Cuántos años hacia atrás considerar como 'recientes'? (por defecto 5): ") or "5")
            except ValueError:
                anios = 5
            listar_libros_recientes(anios)
        elif opcion == '4':
            agregar_libro()
        elif opcion == '5':
            print(f"\nSaliendo del catálogo de libros. ¡Hasta luego!")
            break
        else:
            print(f"\n✗ Opción no válida. Por favor, seleccione una opción del 1 al 5.")
        
        input(f"\nPresione Enter para continuar...")