# Ejercicio 5: Inventario de Productos
# Pide al usuario que ingrese la cantidad de 8 productos diferentes en stock.
# Crea una Serie y asigna nombres de productos como índice.
# Muestra los productos con menos de 10 unidades.
# Rellena cualquier valor faltante (NaN) con 0.
# Muestra los productos ordenados por la cantidad en stock.

import pandas as pd
import numpy as np

productos = []
cantidades = []

print("Ingrese el nombre y la cantidad de 8 productos diferentes")
print("(Deje la cantidad vacía para asignar un valor faltante)")
print("-" * 50)

# 1. Ingreso de productos y cantidades
for i in range(1, 9):
    print(f"\nProducto {i}:")
    
    # Pedir nombre del producto
    while True:
        nombre = input("  Nombre del producto: ").strip()
        if nombre == "":
            print("  Error: el nombre no puede estar vacío.")
        else:
            productos.append(nombre)
            break
    
    # Pedir cantidad
    while True:
        entrada = input("  Cantidad en stock: ")
        if entrada == "":
            cantidades.append(np.nan)
            print("  (Valor faltante registrado)")
            break
        else:
            try:
                cantidad = float(entrada)
                if cantidad < 0:
                    print("  Error: el stock no puede ser negativo.")
                else:
                    cantidades.append(cantidad)
                    break
            except ValueError:
                print("  Entrada inválida, se asignará valor faltante.")
                cantidades.append(np.nan)
                break

# 2. Crear la Serie
serie_inventario = pd.Series(cantidades, index=productos)

print("\n" + "=" * 50)
print("ANÁLISIS DE INVENTARIO")
print("=" * 50)

# 3. Productos con menos de 10 unidades (antes de rellenar NaN)
print("\nProductos con menos de 10 unidades:")
print("-" * 35)
productos_bajos = serie_inventario[serie_inventario < 10]
if productos_bajos.empty:
    print("Todos los productos tienen stock suficiente")
else:
    for producto, cantidad in productos_bajos.items():
        if pd.isna(cantidad):
            print(f"{producto}: Sin dato")
        else:
            print(f"{producto}: {int(cantidad)} unidades")

# 4. Rellenar valores faltantes con 0
serie_inventario_completo = serie_inventario.fillna(0)

print("\nInventario después de rellenar valores faltantes con 0:")
print("-" * 35)
for producto, cantidad in serie_inventario_completo.items():
    print(f"{producto:<20}: {int(cantidad)} unidades")

# 5. Productos ordenados por cantidad
print("\nProductos ordenados por cantidad en stock:")
print("-" * 35)
serie_ordenado = serie_inventario_completo.sort_values(ascending=False)
for producto, cantidad in serie_ordenado.items():
    print(f"{producto:<20}: {int(cantidad)} unidades")

print("")