import json
import os
from datetime import datetime

# Ruta del archivo JSON
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOMBRE_ARCHIVO = os.path.join(BASE_DIR, "ventas.json")

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def cargar_datos():
    if os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, 'r', encoding='utf-8') as archivo:
            try:
                datos = json.load(archivo)
                return datos.get("ventas", [])
            except json.JSONDecodeError:
                print(f"Error: El archivo {NOMBRE_ARCHIVO} está vacío o corrompido. Se creará uno nuevo.")
                return []
    else:
        print(f"Archivo {NOMBRE_ARCHIVO} no encontrado. Se creará uno nuevo.")
        return []

def guardar_datos(ventas):
    with open(NOMBRE_ARCHIVO, 'w', encoding='utf-8') as archivo:
        json.dump({"ventas": ventas}, archivo, indent=4, ensure_ascii=False)
    print(f"✓ Datos guardados correctamente.")

def inicializar_datos():
    ventas = cargar_datos()
    if not ventas:
        ventas_iniciales = [
            {"producto": "Laptop", "cantidad": 2, "precio": 1000, "fecha": "2024-10-28"},
            {"producto": "Teclado", "cantidad": 5, "precio": 50, "fecha": "2024-10-27"},
            {"producto": "Mouse", "cantidad": 3, "precio": 40, "fecha": "2024-10-26"},
            {"producto": "Monitor", "cantidad": 1, "precio": 300, "fecha": "2024-10-25"},
            {"producto": "Silla Gamer", "cantidad": 2, "precio": 200, "fecha": "2024-10-24"},
            {"producto": "Impresora", "cantidad": 1, "precio": 150, "fecha": "2024-10-23"},
            {"producto": "Escritorio", "cantidad": 1, "precio": 120, "fecha": "2024-10-22"},
            {"producto": "Auriculares", "cantidad": 4, "precio": 60, "fecha": "2024-10-21"},
            {"producto": "USB 64GB", "cantidad": 10, "precio": 15, "fecha": "2024-10-20"},
            {"producto": "Disco Duro Externo", "cantidad": 2, "precio": 80, "fecha": "2024-10-19"}
        ]
        guardar_datos(ventas_iniciales)
        print(f"✓ Archivo de ventas creado con 10 ventas iniciales.")
        return ventas_iniciales
    return ventas

def mostrar_venta(venta):
    print(f"Producto: {venta['producto']}")
    print(f"Cantidad: {venta['cantidad']}")
    print(f"Precio unitario: ${venta['precio']}")
    print(f"Fecha: {venta['fecha']}")
    print(f"Total: ${venta['cantidad'] * venta['precio']}")

def calcular_total_ventas():
    ventas = cargar_datos()
    total = sum(v["cantidad"] * v["precio"] for v in ventas)
    print(f"\n--- TOTAL DE VENTAS ACUMULADAS: ${total} ---")

def filtrar_por_producto(nombre_producto):
    ventas = cargar_datos()
    encontradas = [v for v in ventas if v["producto"].lower() == nombre_producto.lower()]
    if encontradas:
        print(f"\n--- Ventas del producto '{nombre_producto}': ---")
        for v in encontradas:
            mostrar_venta(v)
            print("-" * 30)
    else:
        print(f"✗ No se encontraron ventas para el producto '{nombre_producto}'.")

def filtrar_por_fecha(fecha):
    ventas = cargar_datos()
    encontradas = [v for v in ventas if v["fecha"] == fecha]
    if encontradas:
        print(f"\n--- Ventas del día {fecha}: ---")
        for v in encontradas:
            mostrar_venta(v)
            print("-" * 30)
    else:
        print(f"✗ No se encontraron ventas para la fecha '{fecha}'.")

def agregar_nueva_venta():
    producto = input("Ingrese el nombre del producto vendido: ").strip()
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad vendida: "))
            if cantidad > 0:
                break
            else:
                print("✗ La cantidad debe ser mayor a 0.")
        except ValueError:
            print("✗ Ingrese un número entero válido.")

    while True:
        try:
            precio = float(input("Ingrese el precio unitario: "))
            if precio >= 0:
                break
            else:
                print("✗ El precio no puede ser negativo.")
        except ValueError:
            print("✗ Ingrese un número válido.")

    while True:
        fecha = input("Ingrese la fecha de la venta (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            break
        except ValueError:
            print("✗ Formato de fecha inválido. Use YYYY-MM-DD.")

    nueva_venta = {
        "producto": producto,
        "cantidad": cantidad,
        "precio": precio,
        "fecha": fecha
    }

    ventas = cargar_datos()
    ventas.append(nueva_venta)
    guardar_datos(ventas)
    print(f"✓ Venta de '{producto}' agregada correctamente.")

def mostrar_menu():
    print(f"\n╔" + "═" * 30 + "╗")
    print(f"║     Registro de Ventas       ║")
    print(f"╚" + "═" * 30 + "╝")
    print(f"1. Agregar nueva venta")
    print(f"2. Calcular total de ventas")
    print(f"3. Filtrar ventas por producto")
    print(f"4. Filtrar ventas por fecha")
    print(f"5. Salir")
    print(f"" + "=" * 32 + f"")

if __name__ == "__main__":
    ventas_actuales = inicializar_datos()

    while True:
        limpiar_consola()
        mostrar_menu()
        try:
            opcion = input(f"\nSeleccione una opción (1-5): ")
        except KeyboardInterrupt:
            print(f"\n\nSaliendo del sistema de ventas. ¡Hasta luego!")
            break

        if opcion == '1':
            agregar_nueva_venta()
        elif opcion == '2':
            calcular_total_ventas()
        elif opcion == '3':
            producto = input("Ingrese el nombre del producto a filtrar: ").strip()
            filtrar_por_producto(producto)
        elif opcion == '4':
            fecha = input("Ingrese la fecha a filtrar (YYYY-MM-DD): ").strip()
            filtrar_por_fecha(fecha)
        elif opcion == '5':
            print(f"\nSaliendo del sistema de ventas. ¡Hasta luego!")
            break
        else:
            print(f"\n✗ Opción no válida. Por favor, seleccione una opción del 1 al 5.")
        
        input(f"\nPresione Enter para continuar...")