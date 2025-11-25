import json
import os

# Ruta del archivo JSON
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOMBRE_ARCHIVO = os.path.join(BASE_DIR, "superheroes.json")

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def cargar_datos():
    if os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, 'r', encoding='utf-8') as archivo:
            try:
                datos = json.load(archivo)
                return datos.get("superheroes", [])
            except json.JSONDecodeError:
                print(f"Error: El archivo {NOMBRE_ARCHIVO} está vacío o corrompido. Se creará uno nuevo.")
                return []
    else:
        print(f"Archivo {NOMBRE_ARCHIVO} no encontrado. Se creará uno nuevo.")
        return []

def guardar_datos(superheroes):
    with open(NOMBRE_ARCHIVO, 'w', encoding='utf-8') as archivo:
        json.dump({"superheroes": superheroes}, archivo, indent=4, ensure_ascii=False)
    print(f"✓ Datos guardados correctamente.")

def inicializar_datos():
    superheroes = cargar_datos()
    if not superheroes:
        superheroes_iniciales = [
            {"alias": "El Cid", "habilidades": ["esgrima", "estrategia"], "ciudad": "Burgos", "equipo": "Los Defensores"},
            {"alias": "La Dama de Plata", "habilidades": ["manipulación de metales"], "ciudad": "Toledo", "equipo": "Los Defensores"},
            {"alias": "Furia del Norte", "habilidades": ["resistencia", "clima"], "ciudad": "Santander", "equipo": "Guardianes del Norte"},
            {"alias": "Rayo Solar", "habilidades": ["velocidad", "luz solar"], "ciudad": "Sevilla", "equipo": "Equipo Sol"},
            {"alias": "Alma de Fuego", "habilidades": ["fuego", "curación"], "ciudad": "Valencia", "equipo": "Alianza del Fuego"},
            {"alias": "Murciélago de Acero", "habilidades": ["detective", "tecnología"], "ciudad": "Madrid", "equipo": "Justicia Nocturna"},
            {"alias": "Tormenta Mental", "habilidades": ["telequinesis", "lectura mental"], "ciudad": "Barcelona", "equipo": "Psíquicos Unidos"},
            {"alias": "Agente Escudo", "habilidades": ["defensa", "táctica"], "ciudad": "Bilbao", "equipo": "Escudo Urbano"},
            {"alias": "Cazadora de Sombras", "habilidades": ["sigilo", "combate"], "ciudad": "Granada", "equipo": "Noche Eterna"},
            {"alias": "Fuerza del Mar", "habilidades": ["control de agua", "natación"], "ciudad": "Alicante", "equipo": "Guardianes del Mar"}
        ]
        guardar_datos(superheroes_iniciales)
        print(f"✓ Archivo de superhéroes creado con 10 superhéroes iniciales.")
        return superheroes_iniciales
    return superheroes

def mostrar_superheroe(superheroe):
    print(f"Alias: {superheroe['alias']}")
    print(f"Habilidades: {', '.join(superheroe['habilidades'])}")
    print(f"Ciudad: {superheroe['ciudad']}")
    print(f"Equipo: {superheroe['equipo']}")

def filtrar_por_ciudad(ciudad):
    superheroes = cargar_datos()
    encontrados = [s for s in superheroes if s["ciudad"].lower() == ciudad.lower()]
    if encontrados:
        print(f"\n--- Superhéroes de la ciudad '{ciudad}': ---")
        for s in encontrados:
            mostrar_superheroe(s)
            print("-" * 40)
    else:
        print(f"✗ No se encontraron superhéroes en la ciudad '{ciudad}'.")

def filtrar_por_equipo(equipo):
    superheroes = cargar_datos()
    encontrados = [s for s in superheroes if s["equipo"].lower() == equipo.lower()]
    if encontrados:
        print(f"\n--- Superhéroes del equipo '{equipo}': ---")
        for s in encontrados:
            mostrar_superheroe(s)
            print("-" * 40)
    else:
        print(f"✗ No se encontraron superhéroes en el equipo '{equipo}'.")

def listar_habilidades_unicas():
    superheroes = cargar_datos()
    habilidades = set()
    for s in superheroes:
        habilidades.update(s["habilidades"])
    if habilidades:
        print(f"\n--- Habilidades únicas en la red: ---")
        for h in sorted(habilidades):
            print(f"- {h}")
    else:
        print(f"✗ No hay habilidades registradas.")

def agregar_superheroe():
    alias = input("Ingrese el alias del superhéroe: ").strip()
    habilidades = input("Ingrese las habilidades separadas por coma: ").strip().split(",")
    habilidades = [h.strip() for h in habilidades if h.strip()]
    ciudad = input("Ingrese la ciudad de origen: ").strip()
    equipo = input("Ingrese el equipo al que pertenece: ").strip()

    nuevo_superheroe = {
        "alias": alias,
        "habilidades": habilidades,
        "ciudad": ciudad,
        "equipo": equipo
    }

    superheroes = cargar_datos()
    superheroes.append(nuevo_superheroe)
    guardar_datos(superheroes)
    print(f"✓ Superhéroe '{alias}' agregado correctamente.")

def mostrar_menu():
    print(f"\n╔" + "═" * 32 + "╗")
    print(f"║      Red de Superhéroes        ║")
    print(f"╚" + "═" * 32 + "╝")
    print(f"1. Filtrar superhéroes por ciudad")
    print(f"2. Filtrar superhéroes por equipo")
    print(f"3. Listar habilidades únicas")
    print(f"4. Agregar nuevo superhéroe")
    print(f"5. Salir")
    print(f"" + "=" * 34 + f"")

if __name__ == "__main__":
    superheroes_actuales = inicializar_datos()

    while True:
        limpiar_consola()
        mostrar_menu()
        try:
            opcion = input(f"\nSeleccione una opción (1-5): ")
        except KeyboardInterrupt:
            print(f"\n\nSaliendo de la red de superhéroes. ¡Hasta luego!")
            break

        if opcion == '1':
            ciudad = input("Ingrese la ciudad a filtrar: ").strip()
            filtrar_por_ciudad(ciudad)
        elif opcion == '2':
            equipo = input("Ingrese el equipo a filtrar: ").strip()
            filtrar_por_equipo(equipo)
        elif opcion == '3':
            listar_habilidades_unicas()
        elif opcion == '4':
            agregar_superheroe()
        elif opcion == '5':
            print(f"\nSaliendo de la red de superhéroes. ¡Hasta luego!")
            break
        else:
            print(f"\n✗ Opción no válida. Por favor, seleccione una opción del 1 al 5.")
        
        input(f"\nPresione Enter para continuar...")