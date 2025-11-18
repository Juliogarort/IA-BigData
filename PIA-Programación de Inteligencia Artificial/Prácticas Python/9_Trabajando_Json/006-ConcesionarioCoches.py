import json
import os

# Ruta del archivo JSON
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOMBRE_ARCHIVO = os.path.join(BASE_DIR, "coches.json")

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def cargar_datos():
    if os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, 'r', encoding='utf-8') as archivo:
            try:
                datos = json.load(archivo)
                return datos.get("coches", [])
            except json.JSONDecodeError:
                print(f"Error: El archivo {NOMBRE_ARCHIVO} está vacío o corrompido. Se creará uno nuevo.")
                return []
    else:
        print(f"Archivo {NOMBRE_ARCHIVO} no encontrado. Se creará uno nuevo.")
        return []

def guardar_datos(coches):
    with open(NOMBRE_ARCHIVO, 'w', encoding='utf-8') as archivo:
        json.dump({"coches": coches}, archivo, indent=4, ensure_ascii=False)
    print(f"✓ Datos guardados correctamente.")

def inicializar_datos():
    coches = cargar_datos()
    if not coches:
        coches_iniciales = [
            {"marca": "Toyota", "modelo": "Corolla", "precio": 20000, "año": 2023},
            {"marca": "Ford", "modelo": "Focus", "precio": 18000, "año": 2022},
            {"marca": "Honda", "modelo": "Civic", "precio": 22000, "año": 2023},
            {"marca": "Chevrolet", "modelo": "Malibu", "precio": 25000, "año": 2022},
            {"marca": "Nissan", "modelo": "Altima", "precio": 23000, "año": 2021},
            {"marca": "BMW", "modelo": "Serie 3", "precio": 40000, "año": 2023},
            {"marca": "Audi", "modelo": "RSQ8", "precio": 172669, "año": 2020},
            {"marca": "Mercedes", "modelo": "AMG-One", "precio": 5400000, "año": 2022},
            {"marca": "Volkswagen", "modelo": "Golf", "precio": 26000, "año": 2021},
            {"marca": "Hyundai", "modelo": "I 30", "precio": 19000, "año": 2022}
        ]
        guardar_datos(coches_iniciales)
        print(f"✓ Archivo de coches creado con 10 vehículos iniciales.")
        return coches_iniciales
    return coches

def mostrar_coche(coche):
    print(f"Marca: {coche['marca']}")
    print(f"Modelo: {coche['modelo']}")
    print(f"Precio: {coche['precio']:,} €")
    print(f"Año: {coche['año']}")

def filtrar_por_marca(marca):
    coches = cargar_datos()
    encontrados = [c for c in coches if c["marca"].lower() == marca.lower()]
    if encontrados:
        print(f"\n--- Coches de la marca '{marca}': ---")
        for c in encontrados:
            mostrar_coche(c)
            print("-" * 30)
    else:
        print(f"✗ No se encontraron coches de la marca '{marca}'.")

def calcular_valor_promedio():
    coches = cargar_datos()
    if coches:
        promedio = sum(c["precio"] for c in coches) / len(coches)
        print(f"\n--- VALOR PROMEDIO DE LOS COCHES: {promedio:,.2f}€ ---")
    else:
        print(f"✗ No hay coches registrados para calcular el valor promedio.")

def actualizar_precio():
    modelo = input("Ingrese el modelo del coche a actualizar: ").strip()
    coches = cargar_datos()
    encontrado = False
    for c in coches:
        if c["modelo"].lower() == modelo.lower():
            while True:
                try:
                    nuevo_precio = float(input(f"Ingrese el nuevo precio para '{modelo}': "))
                    if nuevo_precio >= 0:
                        c["precio"] = nuevo_precio
                        encontrado = True
                        break
                    else:
                        print("✗ El precio no puede ser negativo.")
                except ValueError:
                    print("✗ Ingrese un número válido.")
            break
    if encontrado:
        guardar_datos(coches)
        print(f"✓ Precio del coche '{modelo}' actualizado correctamente.")
    else:
        print(f"✗ No se encontró el coche con modelo '{modelo}'.")

def mostrar_menu():
    print(f"\n╔" + "═" * 30 + "╗")
    print(f"║   Concesionario de Coches    ║")
    print(f"╚" + "═" * 30 + "╝")
    print(f"1. Filtrar coches por marca")
    print(f"2. Calcular valor promedio de los coches")
    print(f"3. Actualizar precio de un coche")
    print(f"4. Salir")
    print(f"" + "=" * 32 + f"")

if __name__ == "__main__":
    coches_actuales = inicializar_datos()

    while True:
        limpiar_consola()
        mostrar_menu()
        try:
            opcion = input(f"\nSeleccione una opción (1-4): ")
        except KeyboardInterrupt:
            print(f"\n\nSaliendo del concesionario. ¡Hasta luego!")
            break

        if opcion == '1':
            marca = input("Ingrese la marca a filtrar: ").strip()
            filtrar_por_marca(marca)
        elif opcion == '2':
            calcular_valor_promedio()
        elif opcion == '3':
            actualizar_precio()
        elif opcion == '4':
            print(f"\nSaliendo del concesionario. ¡Hasta luego!")
            break
        else:
            print(f"\n✗ Opción no válida. Por favor, seleccione una opción del 1 al 4.")
        
        input(f"\nPresione Enter para continuar...")