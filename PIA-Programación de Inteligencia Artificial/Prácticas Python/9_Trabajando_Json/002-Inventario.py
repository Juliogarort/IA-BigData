import json
import os

# Ruta del archivo JSON
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOMBRE_ARCHIVO = os.path.join(BASE_DIR, "inventario_productos.json")

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def cargar_datos():
    if os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, 'r', encoding='utf-8') as archivo:
            try:
                datos = json.load(archivo)
                return datos.get("productos", [])
            except json.JSONDecodeError:
                print(f"Error: El archivo {NOMBRE_ARCHIVO} está vacío o corrompido. Se creará uno nuevo.")
                return []
    else:
        print(f"Archivo {NOMBRE_ARCHIVO} no encontrado. Se creará uno nuevo.")
        return []

def guardar_datos(productos):
    with open(NOMBRE_ARCHIVO, 'w', encoding='utf-8') as archivo:
        json.dump({"productos": productos}, archivo, indent=4, ensure_ascii=False)
    print(f"✓ Datos guardados correctamente.")

def inicializar_datos():
    productos = cargar_datos()
    if not productos:
        productos_iniciales = [
            {"nombre": "Laptop", "categoria": "Electrónica", "precio": 1000, "stock": 15},
            {"nombre": "Teclado", "categoria": "Accesorios", "precio": 50, "stock": 30},
            {"nombre": "Mouse", "categoria": "Accesorios", "precio": 40, "stock": 50},
            {"nombre": "Monitor", "categoria": "Electrónica", "precio": 300, "stock": 7},
            {"nombre": "Silla Gamer", "categoria": "Muebles", "precio": 200, "stock": 5},
            {"nombre": "Impresora", "categoria": "Electrónica", "precio": 150, "stock": 10},
            {"nombre": "Escritorio", "categoria": "Muebles", "precio": 120, "stock": 8},
            {"nombre": "Auriculares", "categoria": "Accesorios", "precio": 60, "stock": 25},
            {"nombre": "USB 64GB", "categoria": "Almacenamiento", "precio": 15, "stock": 100},
            {"nombre": "Disco Duro Externo", "categoria": "Almacenamiento", "precio": 80, "stock": 20}
        ]
        guardar_datos(productos_iniciales)
        print(f"✓ Archivo de inventario creado con 10 productos iniciales.")
        return productos_iniciales
    return productos

def mostrar_producto(producto):
    print(f"Nombre: {producto['nombre']}")
    print(f"Categoría: {producto['categoria']}")
    print(f"Precio: ${producto['precio']}")
    print(f"Stock: {producto['stock']}")

def filtrar_por_categoria(categoria):
    productos = cargar_datos()
    encontrados = [p for p in productos if p["categoria"].lower() == categoria.lower()]
    if encontrados:
        print(f"\n--- Productos en la categoría '{categoria}': ---")
        for prod in encontrados:
            mostrar_producto(prod)
            print("-" * 30)
    else:
        print(f"✗ No se encontraron productos en la categoría '{categoria}'.")

def calcular_valor_total():
    productos = cargar_datos()
    total = sum(p["precio"] * p["stock"] for p in productos)
    print(f"\n--- VALOR TOTAL DEL INVENTARIO: ${total} ---")

def actualizar_stock(nombre_producto, nuevo_stock):
    productos = cargar_datos()
    actualizado = False
    for prod in productos:
        if prod["nombre"].lower() == nombre_producto.lower():
            prod["stock"] = nuevo_stock
            actualizado = True
            break
    if actualizado:
        guardar_datos(productos)
        print(f"✓ Stock de '{nombre_producto}' actualizado a {nuevo_stock}.")
    else:
        print(f"✗ No se pudo actualizar. Producto '{nombre_producto}' no encontrado.")

def mostrar_menu():
    print(f"\n╔" + "═" * 30 + "╗")
    print(f"║    Inventario de Productos   ║")
    print(f"╚" + "═" * 30 + "╝")
    print(f"1. Filtrar productos por categoría")
    print(f"2. Calcular valor total del inventario")
    print(f"3. Actualizar stock de un producto")
    print(f"4. Salir")
    print(f"" + "=" * 32 + f"")

def solicitar_nombre_producto(mensaje):
    while True:
        nombre = input(mensaje).strip()
        if nombre:
            return nombre
        else:
            print(f"✗ El nombre no puede estar vacío. Intente nuevamente.")

def solicitar_stock(mensaje):
    while True:
        try:
            stock = int(input(mensaje))
            if stock >= 0:
                return stock
            else:
                print("✗ El stock no puede ser negativo.")
        except ValueError:
            print("✗ Ingrese un número entero válido.")

if __name__ == "__main__":
    productos_actuales = inicializar_datos()

    while True:
        limpiar_consola()
        mostrar_menu()
        try:
            opcion = input(f"\nSeleccione una opción (1-4): ")
        except KeyboardInterrupt:
            print(f"\n\nSaliendo del sistema de inventario. ¡Hasta luego!")
            break

        if opcion == '1':
            categoria_buscar = input("Ingrese la categoría a filtrar: ").strip()
            filtrar_por_categoria(categoria_buscar)
        elif opcion == '2':
            calcular_valor_total()
        elif opcion == '3':
            nombre_producto = solicitar_nombre_producto("Ingrese el nombre del producto a actualizar: ")
            nuevo_stock = solicitar_stock("Ingrese el nuevo stock: ")
            actualizar_stock(nombre_producto, nuevo_stock)
        elif opcion == '4':
            print(f"\nSaliendo del sistema de inventario. ¡Hasta luego!")
            break
        else:
            print(f"\n✗ Opción no válida. Por favor, seleccione una opción del 1 al 4.")
        
        input(f"\nPresione Enter para continuar...")