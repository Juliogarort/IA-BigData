import json
import os

# Ruta del archivo JSON
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOMBRE_ARCHIVO = os.path.join(BASE_DIR, "peliculas.json")

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def cargar_datos():
    if os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, 'r', encoding='utf-8') as archivo:
            try:
                datos = json.load(archivo)
                return datos.get("peliculas", [])
            except json.JSONDecodeError:
                print(f"Error: El archivo {NOMBRE_ARCHIVO} está vacío o corrompido. Se creará uno nuevo.")
                return []
    else:
        print(f"Archivo {NOMBRE_ARCHIVO} no encontrado. Se creará uno nuevo.")
        return []

def guardar_datos(peliculas):
    with open(NOMBRE_ARCHIVO, 'w', encoding='utf-8') as archivo:
        json.dump({"peliculas": peliculas}, archivo, indent=4, ensure_ascii=False)
    print(f"✓ Datos guardados correctamente.")

def inicializar_datos():
    peliculas = cargar_datos()
    if not peliculas:
        peliculas_iniciales = [
            {"titulo": "El Laberinto del Fauno", "director": "Guillermo del Toro", "año": 2006, "genero": "Fantasía"},
            {"titulo": "Mar Adentro", "director": "Alejandro Amenábar", "año": 2004, "genero": "Drama"},
            {"titulo": "Matrix", "director": "Wachowski Sisters", "año": 1999, "genero": "Ciencia Ficción"},
            {"titulo": "Pulp Fiction", "director": "Quentin Tarantino", "año": 1994, "genero": "Crimen"},
            {"titulo": "El Padrino", "director": "Francis Ford Coppola", "año": 1972, "genero": "Drama"},
            {"titulo": "Interestelar", "director": "Christopher Nolan", "año": 2014, "genero": "Ciencia Ficción"},
            {"titulo": "La La Land", "director": "Damien Chazelle", "año": 2016, "genero": "Musical"},
            {"titulo": "El Rey León", "director": "Roger Allers", "año": 1994, "genero": "Animación"},
            {"titulo": "Parásitos", "director": "Bong Joon-ho", "año": 2019, "genero": "Thriller"},
            {"titulo": "Titanic", "director": "James Cameron", "año": 1997, "genero": "Romance"}
        ]
        guardar_datos(peliculas_iniciales)
        print(f"✓ Archivo de películas creado con 10 películas iniciales.")
        return peliculas_iniciales
    return peliculas

def mostrar_pelicula(pelicula):
    print(f"Título: {pelicula['titulo']}")
    print(f"Director: {pelicula['director']}")
    print(f"Año: {pelicula['año']}")
    print(f"Género: {pelicula['genero']}")

def filtrar_por_genero(genero):
    peliculas = cargar_datos()
    encontradas = [p for p in peliculas if p["genero"].lower() == genero.lower()]
    if encontradas:
        print(f"\n--- Películas del género '{genero}': ---")
        for p in encontradas:
            mostrar_pelicula(p)
            print("-" * 40)
    else:
        print(f"✗ No se encontraron películas del género '{genero}'.")

def listar_directores_unicos():
    peliculas = cargar_datos()
    directores = {p["director"] for p in peliculas}
    if directores:
        print(f"\n--- Directores únicos en el catálogo: ---")
        for d in sorted(directores):
            print(f"- {d}")
    else:
        print(f"✗ No hay directores registrados.")

def agregar_pelicula():
    titulo = input("Ingrese el título de la película: ").strip()
    director = input("Ingrese el director de la película: ").strip()
    while True:
        try:
            año = int(input("Ingrese el año de lanzamiento: "))
            if año > 0:
                break
            else:
                print("✗ El año debe ser mayor a 0.")
        except ValueError:
            print("✗ Ingrese un número entero válido.")
    genero = input("Ingrese el género de la película: ").strip()

    nueva_pelicula = {
        "titulo": titulo,
        "director": director,
        "año": año,
        "genero": genero
    }

    peliculas = cargar_datos()
    peliculas.append(nueva_pelicula)
    guardar_datos(peliculas)
    print(f"✓ Película '{titulo}' agregada correctamente.")

def mostrar_menu():
    print(f"\n╔" + "═" * 32 + "╗")
    print(f"║     Catálogo de Películas      ║")
    print(f"╚" + "═" * 32 + "╝")
    print(f"1. Filtrar películas por género")
    print(f"2. Listar directores únicos")
    print(f"3. Agregar nueva película")
    print(f"4. Salir")
    print(f"" + "=" * 34 + f"")

if __name__ == "__main__":
    peliculas_actuales = inicializar_datos()

    while True:
        limpiar_consola()
        mostrar_menu()
        try:
            opcion = input(f"\nSeleccione una opción (1-4): ")
        except KeyboardInterrupt:
            print(f"\n\nSaliendo del catálogo de películas. ¡Hasta luego!")
            break

        if opcion == '1':
            genero = input("Ingrese el género a filtrar: ").strip()
            filtrar_por_genero(genero)
        elif opcion == '2':
            listar_directores_unicos()
        elif opcion == '3':
            agregar_pelicula()
        elif opcion == '4':
            print(f"\nSaliendo del catálogo de películas. ¡Hasta luego!")
            break
        else:
            print(f"\n✗ Opción no válida. Por favor, seleccione una opción del 1 al 4.")
        
        input(f"\nPresione Enter para continuar...")