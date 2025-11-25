import json
import os
from datetime import datetime

# Ruta del archivo JSON
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOMBRE_ARCHIVO = os.path.join(BASE_DIR, "eventos.json")

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def cargar_datos():
    if os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, 'r', encoding='utf-8') as archivo:
            try:
                datos = json.load(archivo)
                return datos.get("eventos", [])
            except json.JSONDecodeError:
                print(f"Error: El archivo {NOMBRE_ARCHIVO} está vacío o corrompido. Se creará uno nuevo.")
                return []
    else:
        print(f"Archivo {NOMBRE_ARCHIVO} no encontrado. Se creará uno nuevo.")
        return []

def guardar_datos(eventos):
    with open(NOMBRE_ARCHIVO, 'w', encoding='utf-8') as archivo:
        json.dump({"eventos": eventos}, archivo, indent=4, ensure_ascii=False)
    print(f"✓ Datos guardados correctamente.")

def inicializar_datos():
    eventos = cargar_datos()
    if not eventos:
        eventos_iniciales = [
            {"titulo": "Conferencia Python", "fecha": "2024-11-15", "ubicacion": "Madrid", "organizador": "PyCon España"},
            {"titulo": "Taller de IA", "fecha": "2024-12-01", "ubicacion": "Barcelona", "organizador": "TechFest"},
            {"titulo": "Feria del Libro", "fecha": "2024-06-10", "ubicacion": "Bilbao", "organizador": "Asociación Cultural"},
            {"titulo": "Concierto de Jazz", "fecha": "2024-09-20", "ubicacion": "Valencia", "organizador": "Orquesta Local"},
            {"titulo": "Exposición de Arte", "fecha": "2024-10-05", "ubicacion": "Sevilla", "organizador": "Galería Moderna"},
            {"titulo": "Hackathon Tech", "fecha": "2024-11-20", "ubicacion": "Madrid", "organizador": "DevTeam"},
            {"titulo": "Festival de Cine", "fecha": "2024-07-15", "ubicacion": "Barcelona", "organizador": "Fundación Cine"},
            {"titulo": "Maratón Ciudad", "fecha": "2024-04-08", "ubicacion": "Valencia", "organizador": "Club Atletismo"},
            {"titulo": "Concurso de Startups", "fecha": "2024-11-25", "ubicacion": "Bilbao", "organizador": "Innovación Norte"},
            {"titulo": "Feria Gastronómica", "fecha": "2024-05-12", "ubicacion": "Sevilla", "organizador": "Asociación Chef"}
        ]
        guardar_datos(eventos_iniciales)
        print(f"✓ Archivo de eventos creado con 10 eventos iniciales.")
        return eventos_iniciales
    return eventos

def mostrar_evento(evento):
    print(f"Título: {evento['titulo']}")
    print(f"Fecha: {evento['fecha']}")
    print(f"Ubicación: {evento['ubicacion']}")
    print(f"Organizador: {evento['organizador']}")

def filtrar_por_fecha(fecha):
    eventos = cargar_datos()
    encontrados = [e for e in eventos if e["fecha"] == fecha]
    if encontrados:
        print(f"\n--- Eventos para la fecha {fecha}: ---")
        for e in encontrados:
            mostrar_evento(e)
            print("-" * 40)
    else:
        print(f"✗ No se encontraron eventos para la fecha '{fecha}'.")

def filtrar_por_ubicacion(ubicacion):
    eventos = cargar_datos()
    encontrados = [e for e in eventos if ubicacion.lower() in e["ubicacion"].lower()]
    if encontrados:
        print(f"\n--- Eventos en '{ubicacion}': ---")
        for e in encontrados:
            mostrar_evento(e)
            print("-" * 40)
    else:
        print(f"✗ No se encontraron eventos en '{ubicacion}'.")

def agregar_evento_futuro():
    titulo = input("Ingrese el título del evento: ").strip()
    while True:
        fecha = input("Ingrese la fecha del evento (YYYY-MM-DD): ").strip()
        try:
            fecha_obj = datetime.strptime(fecha, "%Y-%m-%d")
            if fecha_obj.date() >= datetime.now().date():
                break
            else:
                print("✗ La fecha debe ser futura.")
        except ValueError:
            print("✗ Formato de fecha inválido. Use YYYY-MM-DD.")

    ubicacion = input("Ingrese la ubicación del evento: ").strip()
    organizador = input("Ingrese el organizador del evento: ").strip()

    nuevo_evento = {
        "titulo": titulo,
        "fecha": fecha,
        "ubicacion": ubicacion,
        "organizador": organizador
    }

    eventos = cargar_datos()
    eventos.append(nuevo_evento)
    guardar_datos(eventos)
    print(f"✓ Evento '{titulo}' agregado correctamente.")

def eliminar_eventos_pasados():
    eventos = cargar_datos()
    hoy = datetime.now().date()
    eliminados = []
    for i in range(len(eventos) - 1, -1, -1):
        fecha_evento = datetime.strptime(eventos[i]["fecha"], "%Y-%m-%d").date()
        if fecha_evento < hoy:
            eliminados.append(eventos[i]["titulo"])
            del eventos[i]
    
    if eliminados:
        guardar_datos(eventos)
        print(f"✓ Se eliminaron {len(eliminados)} eventos pasados:")
        for titulo in eliminados:
            print(f"  - {titulo}")
    else:
        print(f"✗ No se encontraron eventos pasados para eliminar.")

def mostrar_menu():
    print(f"\n╔" + "═" * 32 + "╗")
    print(f"║      Agenda de Eventos         ║")
    print(f"╚" + "═" * 32 + "╝")
    print(f"1. Filtrar eventos por fecha")
    print(f"2. Filtrar eventos por ubicación")
    print(f"3. Agregar evento futuro")
    print(f"4. Eliminar eventos pasados")
    print(f"5. Salir")
    print(f"" + "=" * 34 + f"")

if __name__ == "__main__":
    eventos_actuales = inicializar_datos()

    while True:
        limpiar_consola()
        mostrar_menu()
        try:
            opcion = input(f"\nSeleccione una opción (1-5): ")
        except KeyboardInterrupt:
            print(f"\n\nSaliendo de la agenda de eventos. ¡Hasta luego!")
            break

        if opcion == '1':
            fecha = input("Ingrese la fecha a filtrar (YYYY-MM-DD): ").strip()
            filtrar_por_fecha(fecha)
        elif opcion == '2':
            ubicacion = input("Ingrese la ubicación a filtrar: ").strip()
            filtrar_por_ubicacion(ubicacion)
        elif opcion == '3':
            agregar_evento_futuro()
        elif opcion == '4':
            eliminar_eventos_pasados()
        elif opcion == '5':
            print(f"\nSaliendo de la agenda de eventos. ¡Hasta luego!")
            break
        else:
            print(f"\n✗ Opción no válida. Por favor, seleccione una opción del 1 al 5.")
        
        input(f"\nPresione Enter para continuar...")