import pandas as pd 

estudiantes = ["oc", "Rinconero", "patatero", "Juan", "juanez", "juanka", "paco", "paki", "paquez", ]
calificaciones = []
print("Ingrese las notas de los estudiantes de 0 hasta 100")

#  1. Ingreso de calificaciones
for estudiante in estudiantes:
    while True:
        entrada = input(f"Ingrese la calificación de {estudiante}: ")
        try:
            calificaciones.append(float(entrada))
            break
        except ValueError:
            print("Error: ingrese una calificación válida.")

# 2. Crear la Serie
serie_calificaciones = pd.Series(calificaciones, index=estudiantes)

# 3. Análisis estadístico
print("\nPromedio:", round(serie_calificaciones.mean(), 2))
print("Mediana:", serie_calificaciones.median())
print("Desviación estándar:", round(serie_calificaciones.std(), 2))

# 4. Reemplazar calificaciones menores a 50
serie_resultados = serie_calificaciones.copy()
serie_resultados[serie_resultados < 50] = "Reprobado"

print("\nResultados finales:")
print(serie_resultados)

# 5. Estudiantes aprobados
print("\nEstudiantes con calificaciones aprobatorias:")
print(serie_calificaciones[serie_calificaciones >= 50])