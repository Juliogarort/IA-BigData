# Ejercicio 3: Análisis de Temperaturas Semanales
# Solicita al usuario las temperaturas registradas en una semana (7 días).
# Crea una Serie con los datos y calcula la temperatura máxima y mínima.
# Identifica los días que tienen temperaturas por encima de 25°C.
# Rellena posibles valores faltantes (NaN) con la temperatura promedio.
# Grafica las temperaturas de la semana.


import pandas as pd
import numpy as np

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
temperaturas = []

print("Ingrese las temperaturas de los días") 

# 1. Entrada de datos
for dia in dias:
    entrada = input(f"{dia}: ")
    if entrada == "":
        temperaturas.append(np.nan)
    else:
        try:
            temperaturas.append(float(entrada))
        except ValueError:
            print("Entrada inválida, se asignará NaN.")
            temperaturas.append(np.nan)

# 2. Crear la Serie
serie_dias = pd.Series(temperaturas, index=dias)

print("\nTemperaturas registradas")
print("-" * 24)

for dia, temp in serie_dias.items():
    if pd.isna(temp):
        print(f"{dia:<12}: Sin dato")
    else:
        print(f"{dia:<12}: {temp:.1f} °C")


