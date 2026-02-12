import matplotlib.pyplot as plt
import math
import random

# Ejercicio 01
# Utilizar la función de la raíz cuadrada (librería Math), generar un gráfico (Matplotlib) 
# de dispersión (Random) en el que se muestre 20 números enteros aleatorios entre 
# el 0 y 100 en el eje X y su raíz cuadrada en el eje Y.

print("\n--- Ejercicio 01: Gráfico de Dispersión ---")
print("Generando Gráfico...")

# 20 números aleatorios entre 0 y 100
x_values = [random.randint(0, 100) for _ in range(20)]

# raíz cuadrada de cada número
y_values = [math.sqrt(x) for x in x_values]

# gráfico de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(x_values, y_values, color='blue', alpha=0.7)

# títulos y etiquetas
plt.title('Gráfico de Dispersión: Números Aleatorios vs Raíz Cuadrada')
plt.xlabel('Número Entero (0-100)')
plt.ylabel('Raíz Cuadrada')
plt.grid(True)
plt.show()