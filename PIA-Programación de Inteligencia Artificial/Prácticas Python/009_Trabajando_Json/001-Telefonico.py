import json
import os

# Ruta del Json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOMBRE_ARCHIVO = os.path.join(BASE_DIR, "directorio_telefonico.json")


def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def cargar_datos():
    if os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, 'r', encoding='utf-8') as archivo:
            try:
                datos = json.load(archivo)
                return datos.get("contactos", [])
            except json.JSONDecodeError:
                print(f"Error: El archivo {NOMBRE_ARCHIVO} está vacío o corrompido. Se creará uno nuevo.")
                return []
    else:
        print(f"Archivo {NOMBRE_ARCHIVO} no encontrado. Se creará uno nuevo.")
        return []

def guardar_datos(contactos):
    with open(NOMBRE_ARCHIVO, 'w', encoding='utf-8') as archivo:
        json.dump({"contactos": contactos}, archivo, indent=4, ensure_ascii=False)
    print(f"✓ Datos guardados correctamente.")

def inicializar_datos():
    contactos = cargar_datos()
    if not contactos:
        contactos_iniciales = [
            {"nombre": "Juan", "apellidos": "Pérez", "telefono": "612345678", "correo": "juan@gmail.com"},
            {"nombre": "Laura", "apellidos": "Gómez", "telefono": "623456789", "correo": "laura@gmail.com"},
            {"nombre": "Ana", "apellidos": "Martínez", "telefono": "611111111", "correo": "ana@gmail.com"},
            {"nombre": "Luis", "apellidos": "Fernández", "telefono": "622222222", "correo": "luis@gmail.com"},
            {"nombre": "Sofía", "apellidos": "Rodríguez", "telefono": "633333333", "correo": "sofia@gmail.com"},
            {"nombre": "Miguel", "apellidos": "López", "telefono": "644444444", "correo": "miguel@gmail.com"},
        ]
        guardar_datos(contactos_iniciales)
        print(f"✓ Archivo de directorio creado con 10 contactos iniciales.")
        return contactos_iniciales
    return contactos

def mostrar_contacto(contacto):
    print(f"Nombre: {contacto['nombre']}")
    print(f"Apellidos: {contacto['apellidos']}")
    print(f"Teléfono: {contacto['telefono']}")
    print(f"Correo: {contacto['correo']}")

def buscar_contacto(nombre):
    contactos = cargar_datos()
    encontrados = [c for c in contactos if c["nombre"].lower() == nombre.lower()]
    if encontrados:
        print(f"\n--- Contacto(s) encontrado(s) con nombre '{nombre}': ---")
        for contacto in encontrados:
            mostrar_contacto(contacto)
            print("-" * 30)
    else:
        print(f"✗ No se encontró ningún contacto con el nombre '{nombre}'.")

def actualizar_telefono(nombre, nuevo_telefono):
    contactos = cargar_datos()
    actualizado = False
    for contacto in contactos:
        if contacto["nombre"].lower() == nombre.lower():
            contacto["telefono"] = nuevo_telefono
            actualizado = True
            break
    if actualizado:
        guardar_datos(contactos)
        print(f"✓ Teléfono de '{nombre}' actualizado a {nuevo_telefono}.")
    else:
        print(f"✗ No se pudo actualizar. No se encontró ningún contacto con el nombre '{nombre}'.")

def agregar_contacto(nombre, apellidos, telefono, correo):
    contactos = cargar_datos()
    nuevo_contacto = {
        "nombre": nombre,
        "apellidos": apellidos,
        "telefono": telefono,
        "correo": correo
    }
    contactos.append(nuevo_contacto)
    guardar_datos(contactos)
    print(f"✓ Contacto '{nombre} {apellidos}' agregado correctamente.")

def eliminar_contacto(nombre):
    contactos = cargar_datos()
    contactos_filtrados = [c for c in contactos if c["nombre"].lower() != nombre.lower()]
    if len(contactos) == len(contactos_filtrados):
        print(f"✗ No se pudo eliminar. No se encontró ningún contacto con el nombre '{nombre}'.")
    else:
        guardar_datos(contactos_filtrados)
        print(f"✓ Contacto '{nombre}' eliminado correctamente.")

def mostrar_menu():
    print(f"\n╔" + "═" * 30 + "╗")
    print(f"║    Directorio Telefónico     ║")
    print(f"╚" + "═" * 30 + "╝")
    print(f"1. Buscar contacto por nombre")
    print(f"2. Actualizar número de teléfono")
    print(f"3. Agregar nuevo contacto")
    print(f"4. Eliminar contacto")
    print(f"5. Salir")
    print(f"" + "=" * 32 + f"")

def solicitar_nombre(mensaje):
    while True:
        nombre = input(mensaje).strip()
        if nombre:
            return nombre
        else:
            print(f"✗ El nombre no puede estar vacío. Intente nuevamente.")

def solicitar_telefono(mensaje):
    while True:
        telefono = input(mensaje).strip()
        if telefono.isdigit() and len(telefono) == 9:
            return telefono
        else:
            print(f"✗ El teléfono debe tener 9 dígitos numéricos. Intente nuevamente.")

def solicitar_correo(mensaje):
    while True:
        correo = input(mensaje).strip()
        if "@" in correo and "." in correo:
            return correo
        else:
            print(f"✗ Formato de correo inválido. Intente nuevamente.")

if __name__ == "__main__":
    contactos_actuales = inicializar_datos()

    while True:
        limpiar_consola()
        mostrar_menu()
        try:
            opcion = input(f"\nSeleccione una opción (1-5): ")
        except KeyboardInterrupt:
            print(f"\n\nSaliendo del directorio telefónico. ¡Hasta luego!")
            break

        if opcion == '1':
            nombre_buscar = solicitar_nombre("Ingrese el nombre del contacto a buscar: ")
            buscar_contacto(nombre_buscar)
        elif opcion == '2':
            nombre_actualizar = solicitar_nombre("Ingrese el nombre del contacto cuyo teléfono desea actualizar: ")
            nuevo_tel = solicitar_telefono("Ingrese el nuevo número de teléfono: ")
            actualizar_telefono(nombre_actualizar, nuevo_tel)
        elif opcion == '3':
            nombre_nuevo = solicitar_nombre("Ingrese el nombre: ")
            apellidos_nuevo = input("Ingrese los apellidos: ").strip()
            telefono_nuevo = solicitar_telefono("Ingrese el teléfono: ")
            correo_nuevo = solicitar_correo("Ingrese el correo electrónico: ")
            agregar_contacto(nombre_nuevo, apellidos_nuevo, telefono_nuevo, correo_nuevo)
        elif opcion == '4':
            nombre_eliminar = solicitar_nombre("Ingrese el nombre del contacto a eliminar: ")
            eliminar_contacto(nombre_eliminar)
        elif opcion == '5':
            print(f"\nSaliendo del directorio telefónico. ¡Hasta luego!")
            break
        else:
            print(f"\n✗ Opción no válida. Por favor, seleccione una opción del 1 al 5.")
        
        input(f"\nPresione Enter para continuar...")