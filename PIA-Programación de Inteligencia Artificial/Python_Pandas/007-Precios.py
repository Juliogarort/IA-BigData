# Ejercicio 7: Análisis de Precio de un Producto en Tiendas
# Pide al usuario que ingrese los precios de un producto en 5 tiendas diferentes.
# Crea una Serie y nombra cada tienda como índice.
# Muestra el precio más bajo y más alto.
# Identifica las tiendas con precios por encima de la mediana.
# Rellena los precios faltantes (NaN) con el precio promedio y grafica los precios.

import pandas as pd
import numpy as np

tiendas = ["Carrefour", "Mercadona", "Lidl", "Alcampo", "Dia"]
precios = []

print("Ingrese el precio del producto en cada tienda")
print("(Presione Enter sin escribir nada para dejar el valor vacío)")

# 1. Ingreso de precios
for tienda in tiendas:
    entrada = input(f"{tienda}: ")
    if entrada == "":
        precios.append(np.nan)
    else:
        try:
            precio = float(entrada)
            if precio < 0:
                print("Error: el precio no puede ser negativo, se asignará NaN.")
                precios.append(np.nan)
            else:
                precios.append(precio)
        except ValueError:
            print("Entrada inválida, se asignará NaN.")
            precios.append(np.nan)

# 2. Crear la Serie
serie_precios = pd.Series(precios, index=tiendas)

# 3. Rellenar valores NaN con el precio promedio
precio_promedio = serie_precios.mean()
serie_precios_completa = serie_precios.fillna(precio_promedio)

# 4. Mostrar precios
print("\nPrecios del producto por tienda:")
print("-" * 40)
for tienda, precio in serie_precios_completa.items():
    if pd.isna(serie_precios[tienda]):
        print(f"{tienda:<12}: {precio:.2f}€ (rellenado con promedio)")
    else:
        print(f"{tienda:<12}: {precio:.2f}€")

# 5. Precio más bajo y más alto
print(f"\nPrecio más bajo: {serie_precios_completa.min():.2f}€ en {serie_precios_completa.idxmin()}")
print(f"Precio más alto: {serie_precios_completa.max():.2f}€ en {serie_precios_completa.idxmax()}")

# 6. Tiendas con precios por encima de la mediana
mediana = serie_precios_completa.median()
print(f"\nMediana de precios: {mediana:.2f}€")
print("\nTiendas con precios por encima de la mediana:")
tiendas_caras = serie_precios_completa[serie_precios_completa > mediana]
if tiendas_caras.empty:
    print("Ninguna tienda tiene precios por encima de la mediana.")
else:
    for tienda, precio in tiendas_caras.items():
        print(f"{tienda}: {precio:.2f}€")

# 7. Gráfico de barras en consola

print("Tienda                      │ Precio (€)")
print("-" * 70)

# Encontrar el precio máximo para escalar
precio_max = serie_precios_completa.max()

# Crear el gráfico
for tienda, precio in serie_precios_completa.items():
    # Calcular la longitud de la barra escalando desde 0
    # Esto hace que las barras sean proporcionales al valor real del precio
    if precio_max > 0:
        barra_longitud = int((precio / precio_max) * 35)
    else:
        barra_longitud = 0
    
    barra = "█" * barra_longitud if barra_longitud > 0 else ""
    
    
    print(f"{tienda:<20}        │ {barra} {precio:.2f}€")


print("")