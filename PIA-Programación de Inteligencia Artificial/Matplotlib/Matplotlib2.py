# Ejercicio 02
# Escribir un programa que pregunte al usuario por las ventas de un rango de años y
# muestre por pantalla un diagrama de líneas con la evolución de las ventas.

import matplotlib.pyplot as plt

print("\n--- Ejercicio 02: Evolución de Ventas ---")
inicio = int(input("Ingrese el año de inicio: "))
fin = int(input("Ingrese el año de fin: "))

ventas = {}
for anyo in range(inicio, fin + 1):
    venta = float(input(f"Ingrese las ventas del año {anyo}: "))
    ventas[anyo] = venta

plt.figure(figsize=(10, 6))
plt.plot(list(ventas.keys()), list(ventas.values()), marker='o', linestyle='-', color='green')
plt.title('Evolución de las Ventas')
plt.xlabel('Año')
plt.ylabel('Ventas')
plt.grid(True)
plt.xticks(list(ventas.keys()))  # Asegurar que se muestren todos los años en el eje X
plt.show()