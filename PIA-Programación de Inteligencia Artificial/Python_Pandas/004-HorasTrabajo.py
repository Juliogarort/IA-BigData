# Ejercicio 4: Registro de Horas de Trabajo
# Solicita al usuario que ingrese las horas trabajadas por un empleado durante 5 días laborales.
# Crea una Serie con los datos.
# Calcula el total de horas trabajadas, y muestra los días en los que el empleado trabajó más de 8 horas.
# Reemplaza las horas menores a 6 con "Medio tiempo".
# Muestra una lista de días y su clasificación de horas (Normal, Medio tiempo, Extra).

import pandas as pd

dias_laborales = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
horas = []

print("Ingrese las horas trabajadas por día")

# 1. solicitamos las horas trabajadas durante la semana
for dia in dias_laborales:
    while True:
        entrada = input(f"{dia}: ")

        if entrada == "":
            print("Error: el campo no puede estar vacío. Intente nuevamente.")
        else:
            try:
                horas.append(float(entrada))
                break
            except ValueError:
                print("Error: debe ingresar un número válido.")

# 2. seria con las horas trabajadas 
serie_horas = pd.Series(horas, index=dias_laborales)

# 3. total de horas trabajadas y dias con mas de 8 horas
print("\nTotal de horas trabajadas en la semana:")
print(round(serie_horas.sum(), 2))

print("\nDías con más de 8 horas trabajadas:")
dias_extra = serie_horas[serie_horas > 8]
if dias_extra.empty:
    print("Ningún día se trabajó más de 8 horas.")
else:
    for dia, hora in dias_extra.items():
        print(f"{dia}: {hora} horas")

# 4. reemplazar horas por clasificaciones correspondientes 
serie_clasificacion = serie_horas.apply(
    lambda x: "Extra" if x > 8 else ("Medio tiempo" if x < 6 else "Normal")
)

print("\nClasificación de horas trabajadas:")
for dia, clasificacion in serie_clasificacion.items():
    print(f"{dia:<12}: {clasificacion}")

print("")
