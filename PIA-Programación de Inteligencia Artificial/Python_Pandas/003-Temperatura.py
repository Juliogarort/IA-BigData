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

# 2. Creacion de la seria y calculo de temperatura max y min
serie_dias = pd.Series(temperaturas, index=dias)

print("\nTemperaturas registradas")
print("-" * 24)

for dia, temp in serie_dias.items():
    if pd.isna(temp):
        print(f"{dia:<12}: Sin dato")
    else:
        print(f"{dia:<12}: {temp:.1f} °C")

# 3. Rellenar valores NaN con la temperatura promedio
temperatura_promedio = serie_dias.mean()
serie_dias_completa = serie_dias.fillna(temperatura_promedio)

# 4. Análisis - Temperatura máxima y mínima
print(f"\nTemperatura máxima: {serie_dias_completa.max():.1f}°C")
print(f"Temperatura mínima: {serie_dias_completa.min():.1f}°C")
print(f"Temperatura promedio: {temperatura_promedio:.1f}°C")

# 5. Días con temperatura por encima de 25°C
print("\nDías con temperatura por encima de 25°C:")
dias_calurosos = serie_dias_completa[serie_dias_completa > 25]
if dias_calurosos.empty:
    print("Ningún día tuvo temperatura superior a 25°C.")
else:
    for dia, temp in dias_calurosos.items():
        print(f"{dia}: {temp:.1f}°C")

# 6. Gráfico de temperaturas
print("\nGráfica textual de temperaturas")
print("-" * 40)

for dia, temp in serie_dias_completa.items():
    barras = int(temp + 20) if temp > -20 else 0
    print(f"{dia:<12}: {'█' * barras} ({temp:.1f}°C)")


print("")
