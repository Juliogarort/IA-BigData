import json
import os

# Ruta del archivo JSON
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOMBRE_ARCHIVO = os.path.join(BASE_DIR, "alumnos.json")

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def cargar_datos():
    if os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, 'r', encoding='utf-8') as archivo:
            try:
                datos = json.load(archivo)
                return datos.get("alumnos", [])
            except json.JSONDecodeError:
                print(f"Error: El archivo {NOMBRE_ARCHIVO} está vacío o corrompido. Se creará uno nuevo.")
                return []
    else:
        print(f"Archivo {NOMBRE_ARCHIVO} no encontrado. Se creará uno nuevo.")
        return []

def guardar_datos(alumnos):
    with open(NOMBRE_ARCHIVO, 'w', encoding='utf-8') as archivo:
        json.dump({"alumnos": alumnos}, archivo, indent=4, ensure_ascii=False)
    print(f"✓ Datos guardados correctamente.")

def inicializar_datos():
    alumnos = cargar_datos()
    if not alumnos:
        alumnos_iniciales = [
            {"nombre": "Carlos", "edad": 20, "calificacion": 85, "ciudad": "Madrid"},
            {"nombre": "Lucía", "edad": 22, "calificacion": 90, "ciudad": "Barcelona"},
            {"nombre": "Pedro", "edad": 19, "calificacion": 78, "ciudad": "Valencia"},
            {"nombre": "Ana", "edad": 21, "calificacion": 92, "ciudad": "Madrid"},
            {"nombre": "Miguel", "edad": 20, "calificacion": 88, "ciudad": "Sevilla"},
            {"nombre": "Sofía", "edad": 23, "calificacion": 76, "ciudad": "Bilbao"},
            {"nombre": "Javier", "edad": 22, "calificacion": 95, "ciudad": "Barcelona"},
            {"nombre": "Paula", "edad": 19, "calificacion": 83, "ciudad": "Valencia"},
            {"nombre": "David", "edad": 21, "calificacion": 70, "ciudad": "Madrid"},
            {"nombre": "Elena", "edad": 20, "calificacion": 89, "ciudad": "Sevilla"}
        ]
        guardar_datos(alumnos_iniciales)
        print(f"✓ Archivo de alumnos creado con 10 alumnos iniciales.")
        return alumnos_iniciales
    return alumnos

def mostrar_alumno(alumno):
    print(f"Nombre: {alumno['nombre']}")
    print(f"Edad: {alumno['edad']}")
    print(f"Calificación: {alumno['calificacion']}")
    print(f"Ciudad: {alumno['ciudad']}")

def filtrar_aprobados():
    alumnos = cargar_datos()
    aprobados = [a for a in alumnos if a["calificacion"] >= 80]
    if aprobados:
        print(f"\n--- Alumnos aprobados (calificación >= 80): ---")
        for a in aprobados:
            mostrar_alumno(a)
            print("-" * 30)
    else:
        print(f"✗ No se encontraron alumnos aprobados.")

def calcular_edad_promedio():
    alumnos = cargar_datos()
    if alumnos:
        promedio = sum(a["edad"] for a in alumnos) / len(alumnos)
        print(f"\n--- EDAD PROMEDIO DE LOS ALUMNOS: {promedio:.2f} años ---")
    else:
        print(f"✗ No hay alumnos registrados para calcular la edad promedio.")

def agregar_alumno():
    nombre = input("Ingrese el nombre del alumno: ").strip()
    while True:
        try:
            edad = int(input("Ingrese la edad del alumno: "))
            if edad > 0:
                break
            else:
                print("✗ La edad debe ser mayor a 0.")
        except ValueError:
            print("✗ Ingrese un número entero válido.")

    while True:
        try:
            calificacion = float(input("Ingrese la calificación del alumno (0-100): "))
            if 0 <= calificacion <= 100:
                break
            else:
                print("✗ La calificación debe estar entre 0 y 100.")
        except ValueError:
            print("✗ Ingrese un número válido.")

    ciudad = input("Ingrese la ciudad del alumno: ").strip()

    nuevo_alumno = {
        "nombre": nombre,
        "edad": edad,
        "calificacion": calificacion,
        "ciudad": ciudad
    }

    alumnos = cargar_datos()
    alumnos.append(nuevo_alumno)
    guardar_datos(alumnos)
    print(f"✓ Alumno '{nombre}' agregado correctamente.")

def eliminar_alumno():
    nombre = input("Ingrese el nombre del alumno a eliminar: ").strip()
    alumnos = cargar_datos()
    encontrado = False
    for i, alumno in enumerate(alumnos):
        if alumno["nombre"].lower() == nombre.lower():
            del alumnos[i]
            encontrado = True
            break
    if encontrado:
        guardar_datos(alumnos)
        print(f"✓ Alumno '{nombre}' eliminado correctamente.")
    else:
        print(f"✗ No se encontró el alumno con nombre '{nombre}'.")

def mostrar_menu():
    print(f"\n╔" + "═" * 30 + "╗")
    print(f"║    Sistema de Alumnos        ║")
    print(f"╚" + "═" * 30 + "╝")
    print(f"1. Agregar nuevo alumno")
    print(f"2. Eliminar alumno")
    print(f"3. Filtrar alumnos aprobados")
    print(f"4. Calcular edad promedio")
    print(f"5. Salir")
    print(f"" + "=" * 32 + f"")

if __name__ == "__main__":
    alumnos_actuales = inicializar_datos()

    while True:
        limpiar_consola()
        mostrar_menu()
        try:
            opcion = input(f"\nSeleccione una opción (1-5): ")
        except KeyboardInterrupt:
            print(f"\n\nSaliendo del sistema de alumnos. ¡Hasta luego!")
            break

        if opcion == '1':
            agregar_alumno()
        elif opcion == '2':
            eliminar_alumno()
        elif opcion == '3':
            filtrar_aprobados()
        elif opcion == '4':
            calcular_edad_promedio()
        elif opcion == '5':
            print(f"\nSaliendo del sistema de alumnos. ¡Hasta luego!")
            break
        else:
            print(f"\n✗ Opción no válida. Por favor, seleccione una opción del 1 al 5.")
        
        input(f"\nPresione Enter para continuar...")