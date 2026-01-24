import pandas as pd
import random
import os
import matplotlib.pyplot as plt

# Generar datos para trabajar con DataFrames y exportar a Excel
nombres = [
    "Alejandro",
    "María",
    "Carlos",
    "Lucía",
    "José",
    "Ana",
    "Javier",
    "Laura",
    "Pablo",
    "Marta",
    "Sergio",
    "Elena",
    "Fernando",
    "Cristina",
    "David",
    "Isabel",
    "Rubén",
    "Patricia",
    "Manuel",
    "Raquel",
]

apellidos = [
    "García",
    "Martínez",
    "López",
    "Sánchez",
    "Pérez",
    "Gómez",
    "Fernández",
    "Díaz",
    "Ruiz",
    "Moreno",
    "Jiménez",
    "Álvarez",
    "Romero",
    "Vargas",
    "Silva",
    "Castro",
    "Ortega",
    "Núñez",
    "Ramos",
    "Molina",
]

# Generar datos para los alumnos
data = []
for i in range(20):
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    correo = f"{nombre.lower()}.{apellido.lower()}@ejemplo.com"
    edad = random.randint(18, 25)
    programacion = [random.randint(0, 10) for _ in range(3)]  # Notas de 3 trimestres
    base_datos = [random.randint(0, 10) for _ in range(3)]
    lenguajes = [random.randint(0, 10) for _ in range(3)]
    sistemas = [random.randint(0, 10) for _ in range(3)]
    entornos = [random.randint(0, 10) for _ in range(3)]
    data.append(
        [nombre, apellido, correo, edad]
        + programacion
        + base_datos
        + lenguajes
        + sistemas
        + entornos
    )

# Crear el DataFrame
columnas = [
    "Nombre",
    "Apellidos",
    "Correo",
    "Edad",
    "Programación T1",
    "Programación T2",
    "Programación T3",
    "Base de Datos T1",
    "Base de Datos T2",
    "Base de Datos T3",
    "Lenguajes T1",
    "Lenguajes T2",
    "Lenguajes T3",
    "Sistemas T1",
    "Sistemas T2",
    "Sistemas T3",
    "Entornos T1",
    "Entornos T2",
    "Entornos T3",
]
df_alumnos = pd.DataFrame(data, columns=columnas)

# Guardar el DataFrame en un archivo Excel en la misma carpeta del script
ruta_script = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(ruta_script, "datos_alumnos.xlsx")
df_alumnos.to_excel(ruta_archivo, index=False)
print(f"Archivo guardado en: {ruta_archivo}")


# Ejercicios para practicar con Pandas y DataFrames


# 1. Filtra a los alumnos que tienen 20 años o más y muestra sus notas finales.
# ***********************************************************************************************************************************
print("=" * 70)
print("EJERCICIO 1: Alumnos con 20 años o más y sus notas finales")
print("=" * 70)


df_alumnos["Nota Final Programación"] = (
    df_alumnos[["Programación T1", "Programación T2", "Programación T3"]]
    .mean(axis=1)
    .round(2)
)
df_alumnos["Nota Final Base de Datos"] = (
    df_alumnos[["Base de Datos T1", "Base de Datos T2", "Base de Datos T3"]]
    .mean(axis=1)
    .round(2)
)
df_alumnos["Nota Final Lenguajes"] = (
    df_alumnos[["Lenguajes T1", "Lenguajes T2", "Lenguajes T3"]].mean(axis=1).round(2)
)
df_alumnos["Nota Final Sistemas"] = (
    df_alumnos[["Sistemas T1", "Sistemas T2", "Sistemas T3"]].mean(axis=1).round(2)
)
df_alumnos["Nota Final Entornos"] = (
    df_alumnos[["Entornos T1", "Entornos T2", "Entornos T3"]].mean(axis=1).round(2)
)

print(
    df_alumnos[df_alumnos["Edad"] >= 20][
        [
            "Nombre",
            "Apellidos",
            "Edad",
            "Nota Final Programación",
            "Nota Final Base de Datos",
            "Nota Final Lenguajes",
            "Nota Final Sistemas",
            "Nota Final Entornos",
        ]
    ]
)


# 2. Añade una nueva columna llamada 'Aprobado' que indique si el alumno ha aprobado o no (si su promedio general es mayor o igual a 5).
# ***********************************************************************************************************************************
print("=" * 70)
print("EJERCICIO 2: Columna Aprobado según promedio general")
print("=" * 70)
df_alumnos["Promedio General"] = (
    df_alumnos[
        [
            "Nota Final Programación",
            "Nota Final Base de Datos",
            "Nota Final Lenguajes",
            "Nota Final Sistemas",
            "Nota Final Entornos",
        ]
    ]
    .mean(axis=1)
    .round(2)
)
df_alumnos["Aprobado"] = df_alumnos["Promedio General"] >= 5
print(df_alumnos[["Nombre", "Apellidos", "Promedio General", "Aprobado"]])

# 3. Calcula la nota máxima de cada módulo y muestra los resultados.
# ***********************************************************************************************************************************
print("\n" + "=" * 70)
print("EJERCICIO 3: Nota máxima de cada módulo")
print("=" * 70)
print(f"Programación: {df_alumnos['Nota Final Programación'].max()}")
print(f"Base de Datos: {df_alumnos['Nota Final Base de Datos'].max()}")
print(f"Lenguajes: {df_alumnos['Nota Final Lenguajes'].max()}")
print(f"Sistemas: {df_alumnos['Nota Final Sistemas'].max()}")
print(f"Entornos: {df_alumnos['Nota Final Entornos'].max()}")

# 4. Filtra a los alumnos que tienen una nota final superior a 9 en la asignatura de 'Lenguajes'.
# ***********************************************************************************************************************************
print("\n" + "=" * 70)
print("EJERCICIO 4: Alumnos con nota final > 9 en Lenguajes")
print("=" * 70)
print(
    df_alumnos[df_alumnos["Nota Final Lenguajes"] > 9][
        ["Nombre", "Apellidos", "Nota Final Lenguajes"]
    ]
)

# 5. Cuenta cuántos alumnos tienen una nota final menor a 5 en la asignatura de 'Sistemas'.
# ***********************************************************************************************************************************
print("\n" + "=" * 70)
print("EJERCICIO 5: Alumnos con nota final < 5 en Sistemas")
print("=" * 70)
conteo = len(df_alumnos[df_alumnos["Nota Final Sistemas"] < 5])
print(f"Número de alumnos con nota < 5 en Sistemas: {conteo}")

# 6. Obtén al alumno con la nota más alta en la asignatura de 'Programación'.
# ***********************************************************************************************************************************
print("\n" + "=" * 70)
print("EJERCICIO 6: Alumno con la nota más alta en Programación")
print("=" * 70)
alumno_top = df_alumnos.loc[df_alumnos["Nota Final Programación"].idxmax()]
print(f"Alumno: {alumno_top['Nombre']} {alumno_top['Apellidos']}")
print(f"Nota Final Programación: {alumno_top['Nota Final Programación']}")

# 7. Agrupa a los alumnos según si han aprobado o no y cuenta cuántos alumnos hay en cada grupo.
# ***********************************************************************************************************************************
print("\n" + "=" * 70)
print("EJERCICIO 7: Conteo de alumnos Aprobados vs No Aprobados")
print("=" * 70)
print(df_alumnos.groupby("Aprobado").size())

# 8. Exporta a un archivo CSV los alumnos que han reprobado al menos un módulo.
# ***********************************************************************************************************************************
print("\n" + "=" * 70)
print("EJERCICIO 8: Exportar alumnos reprobados a CSV")
print("=" * 70)
reprobados = df_alumnos[
    (df_alumnos["Nota Final Programación"] < 5)
    | (df_alumnos["Nota Final Base de Datos"] < 5)
    | (df_alumnos["Nota Final Lenguajes"] < 5)
    | (df_alumnos["Nota Final Sistemas"] < 5)
    | (df_alumnos["Nota Final Entornos"] < 5)
]
ruta_csv = os.path.join(ruta_script, "alumnos_reprobados.csv")
reprobados.to_csv(ruta_csv, index=False)
print(f"Alumnos reprobados exportados a: {ruta_csv}")
print(f"Total reprobados: {len(reprobados)}")

# 9. Crea un gráfico de dispersión que muestre la relación entre las notas finales de 'Programación' y 'Base de Datos'.
# ***********************************************************************************************************************************
print("\n" + "=" * 70)
print("EJERCICIO 9: Gráfico de dispersión (Se abrirá en una ventana)")
print("=" * 70)
try:
    plt.figure(figsize=(10, 6))
    plt.scatter(
        df_alumnos["Nota Final Programación"], df_alumnos["Nota Final Base de Datos"]
    )
    plt.title("Relación Notas Programación vs Base de Datos")
    plt.xlabel("Nota Final Programación")
    plt.ylabel("Nota Final Base de Datos")
    # plt.show() # Comentado para no bloquear la ejecución si se corre en entorno sin GUI, descomentar para ver
    print("Gráfico generado (código incluido, descomentar plt.show() para visualizar)")
except Exception as e:
    print(f"No se pudo generar el gráfico: {e}")

# 10. Calcula la desviación estándar del promedio general de las notas.
# ***********************************************************************************************************************************
print("\n" + "=" * 70)
print("EJERCICIO 10: Desviación estándar del Promedio General")
print("=" * 70)
std_dev = df_alumnos["Promedio General"].std()
print(f"Desviación estándar del promedio general: {std_dev:.2f}")


# Ejercicios para trabajar con archivos Excel y CSV


# 11. Carga un archivo Excel con datos de alumnos en un DataFrame y muestra los primeros 5 registros.

# 12. Guarda una copia del archivo Excel en un archivo CSV.

# 13. Filtra los alumnos que tienen una edad mayor a 22 años y guarda este subconjunto en un nuevo archivo Excel.

# 14. Modifica las notas de los alumnos en el DataFrame y guarda los cambios en una nueva versión del archivo CSV.

# 15. Lee un archivo CSV con datos de alumnos y calcula el promedio de las notas de un módulo específico.

# 16. Agrupa a los alumnos por edad y guarda el promedio de cada grupo en un nuevo archivo Excel.

# 17. Añade una nueva columna al archivo CSV para indicar si el alumno está en el grupo de honor (promedio general superior a 9).

# 18. Carga un archivo Excel, calcula la nota mínima de cada módulo y guarda el resultado en un archivo CSV.

# 19. Fusiona los datos de dos archivos Excel con datos de alumnos y guarda el resultado combinado en un nuevo archivo.

# 20. Exporta un DataFrame a Excel y asegúrate de formatear los valores de las notas con dos decimales.
