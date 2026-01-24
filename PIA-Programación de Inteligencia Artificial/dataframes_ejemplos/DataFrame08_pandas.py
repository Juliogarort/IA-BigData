# Ejercicio Pandas DataFrame

import pandas as pd
import matplotlib.pyplot as plt
import random

# Generar datos para trabajar con DataFrames y exportar a Excel
nombres = ["Alejandro", "María", "Carlos", "Lucía", "José", "Ana", "Javier", "Laura", "Pablo", "Marta",
           "Sergio", "Elena", "Fernando", "Cristina", "David", "Isabel", "Rubén", "Patricia", "Manuel", "Raquel"]
apellidos = ["García", "Martínez", "López", "Sánchez", "Pérez", "Gómez", "Fernández", "Díaz", "Ruiz", "Moreno",
             "Jiménez", "Álvarez", "Romero", "Vargas", "Silva", "Castro", "Ortega", "Núñez", "Ramos", "Molina"]

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
    
    data.append([nombre, apellido, correo, edad] + programacion + base_datos + lenguajes + sistemas + entornos)

# Crear el DataFrame
columnas = [
    "Nombre", "Apellidos", "Correo", "Edad",
    "Programación T1", "Programación T2", "Programación T3",
    "Base de Datos T1", "Base de Datos T2", "Base de Datos T3",
    "Lenguajes T1", "Lenguajes T2", "Lenguajes T3",
    "Sistemas T1", "Sistemas T2", "Sistemas T3",
    "Entornos T1", "Entornos T2", "Entornos T3"
]
df_alumnos = pd.DataFrame(data, columns=columnas)

# Guardar el DataFrame en un archivo Excel
ruta_archivo = "datos_alumnos.xlsx"
df_alumnos.to_excel(ruta_archivo, index=False)

# Cargar el archivo Excel en un DataFrame
df_alumnos = pd.read_excel(ruta_archivo)

# Calcular la nota final por cada módulo y añadir como columnas adicionales
df_alumnos['Programación Final'] = df_alumnos[['Programación T1', 'Programación T2', 'Programación T3']].mean(axis=1).round(2)
df_alumnos['Base de Datos Final'] = df_alumnos[['Base de Datos T1', 'Base de Datos T2', 'Base de Datos T3']].mean(axis=1).round(2)
df_alumnos['Lenguajes Final'] = df_alumnos[['Lenguajes T1', 'Lenguajes T2', 'Lenguajes T3']].mean(axis=1).round(2)
df_alumnos['Sistemas Final'] = df_alumnos[['Sistemas T1', 'Sistemas T2', 'Sistemas T3']].mean(axis=1).round(2)
df_alumnos['Entornos Final'] = df_alumnos[['Entornos T1', 'Entornos T2', 'Entornos T3']].mean(axis=1).round(2)

# Mostrar las primeras filas del DataFrame para verificar que se ha actualizado correctamente
print(df_alumnos.head())

# Filtrar alumnos mayores de 21 años
mayores_21 = df_alumnos[df_alumnos['Edad'] > 21]
print("Alumnos mayores de 21 años:")
print(mayores_21)

# Filtrar alumnos con nota final de Programación mayor o igual a 8
programacion_alta = df_alumnos[df_alumnos['Programación Final'] >= 8]
print("Alumnos con nota alta en Programación:")
print(programacion_alta)

# Ordenar alumnos por nota final de Programación de mayor a menor
df_ordenado = df_alumnos.sort_values(by='Programación Final', ascending=False)
print("Alumnos ordenados por nota de Programación:")
print(df_ordenado)

# Calcular estadísticas básicas sobre las notas finales de Programación
media_programacion = df_alumnos['Programación Final'].mean()
mediana_programacion = df_alumnos['Programación Final'].median()
desviacion_programacion = df_alumnos['Programación Final'].std()
print(f"Media de Programación: {media_programacion}")
print(f"Mediana de Programación: {mediana_programacion}")
print(f"Desviación estándar de Programación: {desviacion_programacion}")

# Añadir una columna con el promedio general de todas las notas finales
df_alumnos['Promedio General'] = df_alumnos[['Programación Final', 'Base de Datos Final', 'Lenguajes Final', 'Sistemas Final', 'Entornos Final']].mean(axis=1).round(2)
print("Promedio General de cada alumno:")
print(df_alumnos[['Nombre', 'Apellidos', 'Promedio General']])

# Contar cuántos alumnos tienen una nota mayor a 5 en Lenguajes
alumnos_aprobados_lenguajes = df_alumnos[df_alumnos['Lenguajes Final'] > 5].shape[0]
print(f"Número de alumnos con nota mayor a 5 en Lenguajes: {alumnos_aprobados_lenguajes}")

# Agrupar alumnos por edad y calcular la media de la nota de Base de Datos para cada grupo
promedio_base_datos_por_edad = df_alumnos.groupby('Edad')['Base de Datos Final'].mean()
print("Promedio de Base de Datos por edad:")
print(promedio_base_datos_por_edad)

# Identificar alumnos que aprobaron todos los módulos
aprobados_todos = df_alumnos[
    (df_alumnos['Programación Final'] >= 5) &
    (df_alumnos['Base de Datos Final'] >= 5) &
    (df_alumnos['Lenguajes Final'] >= 5) &
    (df_alumnos['Sistemas Final'] >= 5) &
    (df_alumnos['Entornos Final'] >= 5)
]
print("Alumnos que aprobaron todos los módulos:")
print(aprobados_todos)

# Crear un gráfico de barras de la nota promedio de cada módulo
modulos = ['Programación Final', 'Base de Datos Final', 'Lenguajes Final', 'Sistemas Final', 'Entornos Final']
promedio_modulos = df_alumnos[modulos].mean()

promedio_modulos.plot(kind='bar')
plt.ylabel('Nota Promedio')
plt.title('Nota Promedio por Módulo')
plt.show()

# Exportar el DataFrame actualizado a un nuevo archivo Excel
ruta_salida = 'datos_alumnos_actualizado.xlsx'
df_alumnos.to_excel(ruta_salida, index=False)

# Ejercicios para practicar con Pandas y DataFrames
# 1. Filtrar alumnos con edad mayor o igual a 20 años y mostrar sus notas finales.
print("Alumnos con edad mayor o igual a 20 años:")
print(df_alumnos[df_alumnos['Edad'] >= 20])

# 2. Crear una nueva columna que indique si el alumno aprobó o no (promedio general >= 5).
df_alumnos['Aprobado'] = df_alumnos['Promedio General'] >= 5
print("Alumnos aprobados:")
print(df_alumnos[['Nombre', 'Apellidos', 'Aprobado']])

# 3. Calcular la nota máxima de cada módulo y mostrar los resultados.
notas_maximas = df_alumnos[modulos].max()
print("Nota máxima de cada módulo:")
print(notas_maximas)

# 4. Filtrar los alumnos que tienen una nota superior a 9 en Lenguajes.
alumnos_nota_alta_lenguajes = df_alumnos[df_alumnos['Lenguajes Final'] > 9]
print("Alumnos con nota superior a 9 en Lenguajes:")
print(alumnos_nota_alta_lenguajes)

# 5. Contar cuántos alumnos tienen una nota final menor a 5 en Sistemas.
alumnos_sistemas_suspensos = df_alumnos[df_alumnos['Sistemas Final'] < 5].shape[0]
print(f"Número de alumnos con nota menor a 5 en Sistemas: {alumnos_sistemas_suspensos}")

# 6. Obtener el alumno con la nota más alta en Programación.
alumno_mejor_programacion = df_alumnos.loc[df_alumnos['Programación Final'].idxmax()]
print("Alumno con la nota más alta en Programación:")
print(alumno_mejor_programacion)

# 7. Agrupar alumnos por la columna 'Aprobado' y contar cuántos hay en cada grupo.
aprobados_conteo = df_alumnos.groupby('Aprobado').size()
print("Número de alumnos aprobados y no aprobados:")
print(aprobados_conteo)

# 8. Exportar a CSV los alumnos que reprobaron al menos un módulo.
alumnos_reprobados = df_alumnos[
    (df_alumnos['Programación Final'] < 5) |
    (df_alumnos['Base de Datos Final'] < 5) |
    (df_alumnos['Lenguajes Final'] < 5) |
    (df_alumnos['Sistemas Final'] < 5) |
    (df_alumnos['Entornos Final'] < 5)
]
alumnos_reprobados.to_csv('alumnos_reprobados.csv', index=False)

# 9. Crear un gráfico de dispersión de las notas finales de Programación vs Base de Datos.
df_alumnos.plot.scatter(x='Programación Final', y='Base de Datos Final', title='Notas Programación vs Base de Datos')
plt.show()

# 10. Calcular la desviación estándar de la nota promedio general.
desviacion_promedio_general = df_alumnos['Promedio General'].std()
print(f"Desviación estándar del promedio general: {desviacion_promedio_general}")
