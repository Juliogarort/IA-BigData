import json
import os
from datetime import datetime

# Ruta del archivo JSON
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOMBRE_ARCHIVO = os.path.join(BASE_DIR, "tareas.json")

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def cargar_datos():
    if os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, 'r', encoding='utf-8') as archivo:
            try:
                datos = json.load(archivo)
                return datos.get("tareas", [])
            except json.JSONDecodeError:
                print(f"Error: El archivo {NOMBRE_ARCHIVO} está vacío o corrompido. Se creará uno nuevo.")
                return []
    else:
        print(f"Archivo {NOMBRE_ARCHIVO} no encontrado. Se creará uno nuevo.")
        return []

def guardar_datos(tareas):
    with open(NOMBRE_ARCHIVO, 'w', encoding='utf-8') as archivo:
        json.dump({"tareas": tareas}, archivo, indent=4, ensure_ascii=False)
    print(f"✓ Datos guardados correctamente.")

def inicializar_datos():
    tareas = cargar_datos()
    if not tareas:
        tareas_iniciales = [
            {"descripcion": "Estudiar Python", "vencimiento": "2024-11-01", "estado": "pendiente"},
            {"descripcion": "Revisar proyecto", "vencimiento": "2024-10-29", "estado": "completada"},
            {"descripcion": "Hacer la compra", "vencimiento": "2024-10-30", "estado": "pendiente"},
            {"descripcion": "Llamar al médico", "vencimiento": "2024-11-02", "estado": "pendiente"},
            {"descripcion": "Preparar presentación", "vencimiento": "2024-11-05", "estado": "completada"},
            {"descripcion": "Leer un libro", "vencimiento": "2024-11-10", "estado": "pendiente"},
            {"descripcion": "Ir al gimnasio", "vencimiento": "2024-10-28", "estado": "completada"},
            {"descripcion": "Enviar correo a cliente", "vencimiento": "2024-11-03", "estado": "pendiente"},
            {"descripcion": "Actualizar CV", "vencimiento": "2024-11-08", "estado": "pendiente"},
            {"descripcion": "Revisar factura", "vencimiento": "2024-11-07", "estado": "completada"}
        ]
        guardar_datos(tareas_iniciales)
        print(f"✓ Archivo de tareas creado con 10 tareas iniciales.")
        return tareas_iniciales
    return tareas

def mostrar_tarea(tarea):
    print(f"Descripción: {tarea['descripcion']}")
    print(f"Vencimiento: {tarea['vencimiento']}")
    print(f"Estado: {tarea['estado']}")

def filtrar_tareas_completadas():
    tareas = cargar_datos()
    encontradas = [t for t in tareas if t["estado"] == "completada"]
    if encontradas:
        print(f"\n--- Tareas completadas: ---")
        for t in encontradas:
            mostrar_tarea(t)
            print("-" * 30)
    else:
        print(f"✗ No se encontraron tareas completadas.")

def agregar_nueva_tarea():
    descripcion = input("Ingrese la descripción de la nueva tarea: ").strip()
    while True:
        vencimiento = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(vencimiento, "%Y-%m-%d")
            break
        except ValueError:
            print("✗ Formato de fecha inválido. Use YYYY-MM-DD.")
    
    estado = input("Ingrese el estado (pendiente/completada): ").strip().lower()
    while estado not in ["pendiente", "completada"]:
        print("✗ Estado inválido. Debe ser 'pendiente' o 'completada'.")
        estado = input("Ingrese el estado (pendiente/completada): ").strip().lower()

    nueva_tarea = {
        "descripcion": descripcion,
        "vencimiento": vencimiento,
        "estado": estado
    }

    tareas = cargar_datos()
    tareas.append(nueva_tarea)
    guardar_datos(tareas)
    print(f"✓ Tarea '{descripcion}' agregada correctamente.")

def actualizar_estado_tarea():
    descripcion = input("Ingrese la descripción de la tarea a actualizar: ").strip()
    tareas = cargar_datos()
    actualizado = False
    for t in tareas:
        if t["descripcion"].lower() == descripcion.lower():
            nuevo_estado = input("Ingrese el nuevo estado (pendiente/completada): ").strip().lower()
            while nuevo_estado not in ["pendiente", "completada"]:
                print("✗ Estado inválido. Debe ser 'pendiente' o 'completada'.")
                nuevo_estado = input("Ingrese el nuevo estado (pendiente/completada): ").strip().lower()
            t["estado"] = nuevo_estado
            actualizado = True
            break
    if actualizado:
        guardar_datos(tareas)
        print(f"✓ Estado de la tarea '{descripcion}' actualizado.")
    else:
        print(f"✗ No se encontró la tarea con descripción '{descripcion}'.")

def mostrar_menu():
    print(f"\n╔" + "═" * 30 + "╗")
    print(f"║      Agenda de Tareas        ║")
    print(f"╚" + "═" * 30 + "╝")
    print(f"1. Agregar nueva tarea")
    print(f"2. Actualizar estado de una tarea")
    print(f"3. Filtrar tareas completadas")
    print(f"4. Salir")
    print(f"" + "=" * 32 + f"")

if __name__ == "__main__":
    tareas_actuales = inicializar_datos()

    while True:
        limpiar_consola()
        mostrar_menu()
        try:
            opcion = input(f"\nSeleccione una opción (1-4): ")
        except KeyboardInterrupt:
            print(f"\n\nSaliendo de la agenda de tareas. ¡Hasta luego!")
            break

        if opcion == '1':
            agregar_nueva_tarea()
        elif opcion == '2':
            actualizar_estado_tarea()
        elif opcion == '3':
            filtrar_tareas_completadas()
        elif opcion == '4':
            print(f"\nSaliendo de la agenda de tareas. ¡Hasta luego!")
            break
        else:
            print(f"\n✗ Opción no válida. Por favor, seleccione una opción del 1 al 4.")
        
        input(f"\nPresione Enter para continuar...")