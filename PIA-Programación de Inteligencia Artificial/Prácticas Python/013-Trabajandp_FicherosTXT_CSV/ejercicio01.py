

import os

# Obtener la ruta del directorio donde está este script
DIRECTORIO_SCRIPT = os.path.dirname(os.path.abspath(__file__))

def crear_tabla_multiplicar():

    # Pedimos el número al usuario
    n = int(input("Introduce un número entre 1 y 10: "))
    
    # Verificamos que esté en el rango correcto
    if n < 1 or n > 10:
        print("Error: El número debe estar entre 1 y 10")
        return
    
    # Creamos el nombre del fichero con la ruta completa
    nombre_fichero = f"tabla-{n}.txt"
    ruta_completa = os.path.join(DIRECTORIO_SCRIPT, nombre_fichero)
    
    # Abrimos el fichero en modo escritura
    with open(ruta_completa, 'w', encoding='utf-8') as fichero:
        # Escribimos la tabla de multiplicar (del 1 al 10)
        for i in range(1, 11):
            resultado = n * i
            linea = f"{n} x {i} = {resultado}\n"
            fichero.write(linea)
    
    print(f"Tabla de multiplicar del {n} guardada en {nombre_fichero}")
    print(f"Ubicación: {DIRECTORIO_SCRIPT}")


def leer_tabla_multiplicar():

    # Pedimos el número al usuario
    n = int(input("Introduce un número entre 1 y 10: "))
    
    # Verificamos que esté en el rango correcto
    if n < 1 or n > 10:
        print("Error: El número debe estar entre 1 y 10")
        return
    
    # Creamos el nombre del fichero con la ruta completa
    nombre_fichero = f"tabla-{n}.txt"
    ruta_completa = os.path.join(DIRECTORIO_SCRIPT, nombre_fichero)
    
    # Intentamos abrir y leer el fichero
    try:
        with open(ruta_completa, 'r', encoding='utf-8') as fichero:
            print(f"\nTabla de multiplicar del {n}:")
            print("-" * 30)
            # Leemos y mostramos todo el contenido
            contenido = fichero.read()
            print(contenido)
    except FileNotFoundError:
        print(f"Error: El fichero {nombre_fichero} no existe.")
        print("Primero debes crear la tabla usando la opción 1.")


def leer_linea_tabla():
 
    # Pedimos los dos números al usuario
    n = int(input("Introduce el número de la tabla (1-10): "))
    m = int(input("Introduce el número de línea a mostrar (1-10): "))
    
    # Verificamos que estén en el rango correcto
    if n < 1 or n > 10 or m < 1 or m > 10:
        print("Error: Los números deben estar entre 1 y 10")
        return
    
    # Creamos el nombre del fichero con la ruta completa
    nombre_fichero = f"tabla-{n}.txt"
    ruta_completa = os.path.join(DIRECTORIO_SCRIPT, nombre_fichero)
    
    # Intentamos abrir y leer el fichero
    try:
        with open(ruta_completa, 'r', encoding='utf-8') as fichero:
            # Leemos todas las líneas del fichero
            lineas = fichero.readlines()
            
            # Mostramos la línea m (restamos 1 porque las listas empiezan en 0)
            if m <= len(lineas):
                print(f"\nLínea {m} de la tabla del {n}:")
                print(lineas[m - 1].strip())
            else:
                print(f"Error: La línea {m} no existe en el fichero")
    except FileNotFoundError:
        print(f"Error: El fichero {nombre_fichero} no existe.")
        print("Primero debes crear la tabla usando la opción 1.")


def menu():
    while True:
        print("\n" + "=" * 50)
        print("EJERCICIO 01 - TABLAS DE MULTIPLICAR")
        print("=" * 50)
        print("1. Crear tabla de multiplicar")
        print("2. Leer tabla de multiplicar completa")
        print("3. Leer una línea específica de la tabla")
        print("4. Salir")
        print("=" * 50)
        
        opcion = input("Elige una opción (1-4): ")
        
        if opcion == '1':
            crear_tabla_multiplicar()
        elif opcion == '2':
            leer_tabla_multiplicar()
        elif opcion == '3':
            leer_linea_tabla()
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Elige entre 1 y 4.")


# Programa principal
if __name__ == "__main__":
    menu()
