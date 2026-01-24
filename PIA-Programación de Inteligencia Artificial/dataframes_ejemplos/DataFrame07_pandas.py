# Cargar Excel a DataFrame

# Fichero notas de alumnos 
# F:\Curso24_25\SI\Tareas_DAM_Tardes\SI_DAM_tutoria.xlsx

import pandas as pd

ruta_archivo = "F:/Curso24_25/SI/Tareas_DAM_Tardes/SI_DAM_tutoria.xlsx"
df = pd.read_excel(ruta_archivo)

# Otro fichero ejemplo:
# C:\00_python\datos_alumnos.xlsx

ruta_archivo="C:/00_python/datos_alumnos.xlsx"
df_alumnos = pd.read_excel(ruta_archivo)

print(df_alumnos.head())

# Calcular la nota final por cada módulo y añadir como columnas adicionales
df_alumnos['Programación Final'] = df_alumnos[['Programación T1', 'Programación T2', 'Programación T3']].mean(axis=1).round(2)
df_alumnos['Base de Datos Final'] = df_alumnos[['Base de Datos T1', 'Base de Datos T2', 'Base de Datos T3']].mean(axis=1).round(2)
df_alumnos['Lenguajes Final'] = df_alumnos[['Lenguajes T1', 'Lenguajes T2', 'Lenguajes T3']].mean(axis=1).round(2)
df_alumnos['Sistemas Final'] = df_alumnos[['Sistemas T1', 'Sistemas T2', 'Sistemas T3']].mean(axis=1).round(2)
df_alumnos['Entornos Final'] = df_alumnos[['Entornos T1', 'Entornos T2', 'Entornos T3']].mean(axis=1).round(2)

# Mostrar las primeras filas del DataFrame para verificar que se ha actualizado correctamente
print(df_alumnos.head())

# Exportar el DataFrame actualizado a un nuevo archivo Excel
ruta_salida = 'C:/00_python/datos_alumnos_copia.xlsx' 
df_alumnos.to_excel(ruta_salida, index=False)



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

import matplotlib.pyplot as plt
# Gráficos
promedio_modulos.plot(kind='bar')
plt.ylabel('Nota Promedio')
plt.title('Nota Promedio por Módulo')
plt.show()

# Exportar el DataFrame actualizado a un nuevo archivo Excel
ruta_salida = 'C:/00_python/datos_alumnos_copia2.xlsx'  # Cambia esto por la ruta de salida
df_alumnos.to_excel(ruta_salida, index=False)


