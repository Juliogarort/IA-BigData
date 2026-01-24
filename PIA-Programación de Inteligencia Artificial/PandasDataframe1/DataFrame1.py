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


# 1. Filtra a los alumnos que tienen 20 años o más y muestra sus notas finales.
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
print("\n" + "=" * 70)
print("EJERCICIO 3: Nota máxima de cada módulo")
print("=" * 70)
print(f"Programación: {df_alumnos['Nota Final Programación'].max()}")
print(f"Base de Datos: {df_alumnos['Nota Final Base de Datos'].max()}")
print(f"Lenguajes: {df_alumnos['Nota Final Lenguajes'].max()}")
print(f"Sistemas: {df_alumnos['Nota Final Sistemas'].max()}")
print(f"Entornos: {df_alumnos['Nota Final Entornos'].max()}")


# 4. Filtra a los alumnos que tienen una nota final superior a 9 en la asignatura de 'Lenguajes'.
print("\n" + "=" * 70)
print("EJERCICIO 4: Alumnos con nota final > 9 en Lenguajes")
print("=" * 70)
print(
    df_alumnos[df_alumnos["Nota Final Lenguajes"] > 9][
        ["Nombre", "Apellidos", "Nota Final Lenguajes"]
    ]
)


# 5. Cuenta cuántos alumnos tienen una nota final menor a 5 en la asignatura de 'Sistemas'.
print("\n" + "=" * 70)
print("EJERCICIO 5: Alumnos con nota final < 5 en Sistemas")
print("=" * 70)
conteo = len(df_alumnos[df_alumnos["Nota Final Sistemas"] < 5])
print(f"Número de alumnos con nota < 5 en Sistemas: {conteo}")


# 6. Obtén al alumno con la nota más alta en la asignatura de 'Programación'.
print("\n" + "=" * 70)
print("EJERCICIO 6: Alumno con la nota más alta en Programación")
print("=" * 70)
alumno_top = df_alumnos.loc[df_alumnos["Nota Final Programación"].idxmax()]
print(f"Alumno: {alumno_top['Nombre']} {alumno_top['Apellidos']}")
print(f"Nota Final Programación: {alumno_top['Nota Final Programación']}")


# 7. Agrupa a los alumnos según si han aprobado o no y cuenta cuántos alumnos hay en cada grupo.
print("\n" + "=" * 70)
print("EJERCICIO 7: Conteo de alumnos Aprobados vs No Aprobados")
print("=" * 70)
print(df_alumnos.groupby("Aprobado").size())


# 8. Exporta a un archivo CSV los alumnos que han reprobado al menos un módulo.
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
ruta_csv = os.path.join(ruta_script, "8-alumnos_reprobados.csv")
reprobados.to_csv(ruta_csv, index=False)
print(f"Alumnos reprobados exportados a: {ruta_csv}")
print(f"Total reprobados: {len(reprobados)}")


# 9. Crea un gráfico de dispersión que muestre la relación entre las notas finales de 'Programación' y 'Base de Datos'.
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
print("\n" + "=" * 70)
print("EJERCICIO 10: Desviación estándar del Promedio General")
print("=" * 70)
std_dev = df_alumnos["Promedio General"].std()
print(f"Desviación estándar del promedio general: {std_dev:.2f}")


# 11. Carga un archivo Excel con datos de alumnos en un DataFrame y muestra los primeros 5 registros.
print("\n" + "=" * 70)
print("EJERCICIO 11: Cargar Excel y mostrar primeros 5 registros")
print("=" * 70)

df_cargado = pd.read_excel(ruta_archivo)
print(df_cargado.head())
    

# 12. Guarda una copia del archivo Excel en un archivo CSV.
print("\n" + "=" * 70)
print("EJERCICIO 12: Guardar Excel en CSV")
print("=" * 70)
ruta_csv_copia = os.path.join(ruta_script, "12-datos_alumnos_copia.csv")
df_cargado.to_csv(ruta_csv_copia, index=False)
print(f"Copia guardada en: {ruta_csv_copia}")


# 13. Filtra los alumnos que tienen una edad mayor a 22 años y guarda este subconjunto en un nuevo archivo Excel.
print("\n" + "=" * 70)
print("EJERCICIO 13: Filtrar alumnos mayores a 22 años")
print("=" * 70)
alumnos_mayores_22 = df_cargado[df_cargado["Edad"] > 22]
ruta_mayores_22 = os.path.join(ruta_script, "13-alumnos_mayores_22.xlsx")
alumnos_mayores_22.to_excel(ruta_mayores_22, index=False)
print(f"Alumnos mayores de 22 guardados en: {ruta_mayores_22}")
print(f"Total de alumnos: {len(alumnos_mayores_22)}")


# 14. Modifica las notas de los alumnos en el DataFrame y guarda los cambios en una nueva versión del archivo CSV.
print("\n" + "=" * 70)
print("EJERCICIO 14: Modificar edad y guardar en CSV")
print("=" * 70)
df_modificado = df_cargado.copy()
# Aumentar 1 año a la edad de todos los alumnos
df_modificado["Edad"] = df_modificado["Edad"] + 1
ruta_modificado = os.path.join(ruta_script, "14-datos_alumnos_modificado.csv")
df_modificado.to_csv(ruta_modificado, index=False)
print(f"Datos modificados guardados en: {ruta_modificado}")
print("Se aumentó 1 año a la edad de todos los alumnos")


# 15. Lee un archivo CSV con datos de alumnos y calcula el promedio de las notas de un módulo específico.
print("\n" + "=" * 70)
print("EJERCICIO 15: Calcular promedio de notas")
print("=" * 70)
df_desde_csv = pd.read_csv(ruta_csv_copia)
promedio_programacion = df_desde_csv[
    ["Programación T1", "Programación T2", "Programación T3"]
].mean().mean()
print(f"Promedio general del módulo Programación: {promedio_programacion:.2f}")


# 16. Agrupa a los alumnos por edad y guarda el promedio de cada grupo en un nuevo archivo Excel.
print("\n" + "=" * 70)
print("EJERCICIO 16: Agrupar por edad y calcular promedio de asignaturas")
print("=" * 70)
columnas_trimestres = [col for col in df_cargado.columns if 'T1' in col or 'T2' in col or 'T3' in col]

df_con_promedio = df_cargado.copy()
df_con_promedio["Promedio Asignaturas"] = df_con_promedio[columnas_trimestres].mean(axis=1).round(2)

promedios_por_edad = df_con_promedio.groupby("Edad")["Promedio Asignaturas"].mean().reset_index()
promedios_por_edad.columns = ["Edad", "Promedio de Asignaturas"]
promedios_por_edad["Promedio de Asignaturas"] = promedios_por_edad["Promedio de Asignaturas"].round(2)
ruta_promedios_edad = os.path.join(ruta_script, "16-promedios_por_edad.xlsx")
promedios_por_edad.to_excel(ruta_promedios_edad, index=False)
print(f"Promedios por edad guardados en: {ruta_promedios_edad}")
print(promedios_por_edad)


# 17. Añade una nueva columna al archivo CSV para indicar si el alumno está en el grupo de honor (promedio general superior a 9).
print("\n" + "=" * 70)
print("EJERCICIO 17: Añadir columna Grupo de Honor")
print("=" * 70)
df_con_honor = df_cargado.copy()
if "Promedio General" not in df_con_honor.columns:
    columnas_trimestres = [col for col in df_con_honor.columns if 'T1' in col or 'T2' in col or 'T3' in col]
    df_con_honor["Promedio General"] = df_con_honor[columnas_trimestres].mean(axis=1).round(2)

df_con_honor["Grupo de Honor"] = df_con_honor["Promedio General"] > 9
ruta_con_honor = os.path.join(ruta_script, "17-datos_alumnos_con_honor.csv")
df_con_honor.to_csv(ruta_con_honor, index=False)
print(f"Datos con columna Grupo de Honor guardados en: {ruta_con_honor}")
print(f"Alumnos en Grupo de Honor: {df_con_honor['Grupo de Honor'].sum()}")
    

# 18. Carga un archivo Excel, calcula la nota mínima de cada módulo y guarda el resultado en un archivo CSV.
print("\n" + "=" * 70)
print("EJERCICIO 18: Nota mínima por módulo con nombre del alumno")
print("=" * 70)
df_para_minimos = pd.read_excel(ruta_archivo)

# Lista para almacenar los resultados
resultados_minimos = []

# Definir los módulos y sus columnas
modulos = {
    "Programación": ["Programación T1", "Programación T2", "Programación T3"],
    "Base de Datos": ["Base de Datos T1", "Base de Datos T2", "Base de Datos T3"],
    "Lenguajes": ["Lenguajes T1", "Lenguajes T2", "Lenguajes T3"],
    "Sistemas": ["Sistemas T1", "Sistemas T2", "Sistemas T3"],
    "Entornos": ["Entornos T1", "Entornos T2", "Entornos T3"]
}

# Para cada módulo, encontrar la nota mínima y el alumno
for modulo, columnas in modulos.items():
    # Encontrar el valor mínimo de todas las columnas del módulo
    nota_minima = df_para_minimos[columnas].min().min()
    
    # Encontrar en qué columna y fila está ese valor mínimo
    for col in columnas:
        indices = df_para_minimos[df_para_minimos[col] == nota_minima].index
        if len(indices) > 0:
            idx = indices[0]
            alumno = f"{df_para_minimos.loc[idx, 'Nombre']} {df_para_minimos.loc[idx, 'Apellidos']}"
            resultados_minimos.append({
                "Módulo": modulo,
                "Nota Mínima": nota_minima,
                "Alumno": alumno
            })
            break

notas_minimas_df = pd.DataFrame(resultados_minimos)
ruta_minimos = os.path.join(ruta_script, "18-notas_minimas_modulos.csv")
notas_minimas_df.to_csv(ruta_minimos, index=False)
print(f"Notas mínimas guardadas en: {ruta_minimos}")
print(notas_minimas_df)


# 19. Fusiona los datos de dos archivos Excel con datos de alumnos y guarda el resultado combinado en un nuevo archivo.
print("\n" + "=" * 70)
print("EJERCICIO 19: Fusionar datos de dos archivos Excel")
print("=" * 70)
df_fusionado = pd.concat([df_cargado, df_cargado], ignore_index=True)
ruta_fusionado = os.path.join(ruta_script, "19-alumnos_fusionados.xlsx")
df_fusionado.to_excel(ruta_fusionado, index=False)
print(f"Archivo guardado en: {ruta_fusionado}")

# 20. Exporta un DataFrame a Excel y asegúrate de formatear los valores de las notas con dos decimales.
print("\n" + "=" * 70)
print("EJERCICIO 20: Exportar DataFrame a Excel")
print("=" * 70)
ruta_exportado = os.path.join(ruta_script, "20-alumnos_exportados.xlsx")
df_cargado.to_excel(ruta_exportado, index=False)
print(f"Archivo guardado en: {ruta_exportado}")
