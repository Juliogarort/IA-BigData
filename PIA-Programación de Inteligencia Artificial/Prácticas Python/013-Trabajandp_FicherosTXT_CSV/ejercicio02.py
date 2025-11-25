
import os

# Obtener la ruta del directorio donde está este script
DIRECTORIO_SCRIPT = os.path.dirname(os.path.abspath(__file__))
RUTA_LISTIN = os.path.join(DIRECTORIO_SCRIPT, 'listin.txt')

def crear_listin():

    try:
        # Intentamos abrir el fichero en modo lectura para ver si existe
        with open(RUTA_LISTIN, 'r', encoding='utf-8'):
            print("El listín ya existe.")
    except FileNotFoundError:
        # Si no existe, lo creamos vacío
        with open(RUTA_LISTIN, 'w', encoding='utf-8'):
            pass
        print("Listín telefónico creado correctamente.")
        print(f"Ubicación: {DIRECTORIO_SCRIPT}")


def consultar_telefono():
 
    nombre = input("Introduce el nombre del cliente a buscar: ")
    
    try:
        # Abrimos el fichero para leer
        with open(RUTA_LISTIN, 'r', encoding='utf-8') as fichero:
            encontrado = False
            
            # Leemos línea por línea
            for linea in fichero:
                # Quitamos espacios en blanco al inicio y final
                linea = linea.strip()
                
                # Si la línea no está vacía
                if linea:
                    # Separamos el nombre y el teléfono por la coma
                    datos = linea.split(',')
                    nombre_fichero = datos[0]
                    telefono = datos[1]
                    
                    # Comparamos el nombre (sin distinguir mayúsculas/minúsculas)
                    if nombre_fichero.lower() == nombre.lower():
                        print(f"\nCliente: {nombre_fichero}")
                        print(f"Teléfono: {telefono}")
                        encontrado = True
                        break
            
            if not encontrado:
                print(f"No se encontró el cliente '{nombre}' en el listín.")
                
    except FileNotFoundError:
        print("Error: El listín no existe. Créalo primero con la opción 1.")


def anadir_cliente():
    nombre = input("Introduce el nombre del cliente: ")
    telefono = input("Introduce el teléfono del cliente: ")
    
    try:
        # Primero verificamos si el cliente ya existe
        with open(RUTA_LISTIN, 'r', encoding='utf-8') as fichero:
            for linea in fichero:
                if linea.strip():
                    datos = linea.split(',')
                    if datos[0].lower() == nombre.lower():
                        print(f"El cliente '{nombre}' ya existe en el listín.")
                        return
        
        # Si no existe, lo añadimos al final del fichero
        with open(RUTA_LISTIN, 'a', encoding='utf-8') as fichero:
            fichero.write(f"{nombre},{telefono}\n")
        
        print(f"Cliente '{nombre}' añadido correctamente.")
        
    except FileNotFoundError:
        print("Error: El listín no existe. Créalo primero con la opción 1.")


def eliminar_cliente():
    nombre = input("Introduce el nombre del cliente a eliminar: ")
    
    try:
        # Leemos todo el contenido del fichero
        with open(RUTA_LISTIN, 'r', encoding='utf-8') as fichero:
            lineas = fichero.readlines()
        
        # Creamos una lista nueva sin el cliente a eliminar
        nuevas_lineas = []
        encontrado = False
        
        for linea in lineas:
            if linea.strip():
                datos = linea.split(',')
                # Si no es el cliente a eliminar, lo guardamos
                if datos[0].lower() != nombre.lower():
                    nuevas_lineas.append(linea)
                else:
                    encontrado = True
        
        if encontrado:
            # Reescribimos el fichero sin el cliente eliminado
            with open(RUTA_LISTIN, 'w', encoding='utf-8') as fichero:
                fichero.writelines(nuevas_lineas)
            print(f"Cliente '{nombre}' eliminado correctamente.")
        else:
            print(f"No se encontró el cliente '{nombre}' en el listín.")
            
    except FileNotFoundError:
        print("Error: El listín no existe. Créalo primero con la opción 1.")


def mostrar_listin():

    try:
        with open(RUTA_LISTIN, 'r', encoding='utf-8') as fichero:
            lineas = fichero.readlines()
            
            if not lineas or all(not linea.strip() for linea in lineas):
                print("El listín está vacío.")
            else:
                print("\n" + "=" * 50)
                print("LISTÍN TELEFÓNICO")
                print("=" * 50)
                for linea in lineas:
                    if linea.strip():
                        datos = linea.strip().split(',')
                        print(f"Cliente: {datos[0]:<20} Teléfono: {datos[1]}")
                print("=" * 50)
                
    except FileNotFoundError:
        print("Error: El listín no existe. Créalo primero con la opción 1.")


def menu():

    while True:
        print("\n" + "=" * 50)
        print("EJERCICIO 02 - LISTÍN TELEFÓNICO")
        print("=" * 50)
        print("1. Crear listín")
        print("2. Consultar teléfono de un cliente")
        print("3. Añadir nuevo cliente")
        print("4. Eliminar cliente")
        print("5. Mostrar todos los clientes")
        print("6. Salir")
        print("=" * 50)
        
        opcion = input("Elige una opción (1-6): ")
        
        if opcion == '1':
            crear_listin()
        elif opcion == '2':
            consultar_telefono()
        elif opcion == '3':
            anadir_cliente()
        elif opcion == '4':
            eliminar_cliente()
        elif opcion == '5':
            mostrar_listin()
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Elige entre 1 y 6.")


# Programa principal
if __name__ == "__main__":
    menu()
