# Ejercicio 8: Análisis de Datos Meteorológicos
# Solicita al usuario las precipitaciones registradas durante los últimos 7 días.
# Crea una Serie con los datos.
# Identifica los días sin lluvia (0 mm) y reemplázalos con "Sin precipitación".
# Calcula el total y el promedio de precipitaciones.
# Muestra los días con precipitación por encima del promedio.

import pandas as pd

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
precipitaciones = []

print("Ingrese las precipitaciones (en mm) de cada día")

# 1. Ingreso de precipitaciones
for dia in dias:
    while True:
        entrada = input(f"{dia}: ")

        if entrada == "":
            print("Error: el campo no puede estar vacío. Intente nuevamente.")
        else:
            try:
                precipitaciones.append(float(entrada))
                break
            except ValueError:
                print("Error: debe ingresar un número válido.")

# 2. Crear la Serie
serie_precipitaciones = pd.Series(precipitaciones, index=dias)

# 3. Análisis de precipitaciones
print("\nPrecipitaciones registradas:")
print("-" * 30)
for dia, precip in serie_precipitaciones.items():
    if precip == 0:
        print(f"{dia:<12}: Sin precipitación")
    else:
        print(f"{dia:<12}: {precip} mm")

# 4. Total y promedio de precipitaciones
total = serie_precipitaciones.sum()
promedio = serie_precipitaciones.mean()

print(f"\nTotal de precipitaciones: {total:.2f} mm")
print(f"Promedio de precipitaciones: {promedio:.2f} mm")

# 5. Días con precipitación por encima del promedio
print("\nDías con precipitación por encima del promedio:")
dias_lluviosos = serie_precipitaciones[serie_precipitaciones > promedio]
if dias_lluviosos.empty:
    print("Ningún día tuvo precipitaciones por encima del promedio.")
else:
    for dia, precip in dias_lluviosos.items():
        print(f"{dia}: {precip} mm")

# 6. Contar días sin lluvia
dias_sin_lluvia = (serie_precipitaciones == 0).sum()
print(f"\nDías sin lluvia: {dias_sin_lluvia}")

print("")
