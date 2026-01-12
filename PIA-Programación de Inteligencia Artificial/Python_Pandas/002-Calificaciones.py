import pandas as pd 

estudiantes = ["oc", "Rinconero", "patatero", "Juan", "juanez", "juanka", "paco", "paki", "paquez"]
calificaciones = []

print (" ")
print("Ingrese las notas de los estudiantes de 0 hasta 100")

# 1. Ingreso de calificaciones
for estudiante in estudiantes:
    while True:
        entrada = input(f"Ingrese la calificación de {estudiante}: ")
        try:
            calificaciones.append(float(entrada))
            break
        except ValueError:
            print("Error: ingrese una calificación válida.")

# 2. Crear la Serie numérica
serie_calificaciones = pd.Series(calificaciones, index=estudiantes)

# 3. Análisis estadístico
print("\nPromedio:", round(serie_calificaciones.mean(), 2))
print("Mediana:", serie_calificaciones.median())
print("Desviación estándar:", round(serie_calificaciones.std(), 2))

# 4. Crear serie de resultados (texto)
serie_resultados = serie_calificaciones.apply(
    lambda x: "Aprobado" if x >= 50 else "Reprobado"
)

print("\nResultados finales:")
# print(serie_resultados)

for estudiante, resultado in serie_resultados.items():
    print(f"{estudiante}: {resultado}")


# 5. Estudiantes aprobados
print("\nEstudiantes con calificaciones aprobatorias:")
aprobados = serie_calificaciones[serie_calificaciones >= 50]

if aprobados.empty:
    print("Ningún estudiante ha aprobado.")
else:
    for estudiante, nota in aprobados.items():
        print(f"{estudiante}: {nota}")


print ("") 
