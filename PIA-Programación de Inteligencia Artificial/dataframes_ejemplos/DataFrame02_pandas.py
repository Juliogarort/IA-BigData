import pandas as pd

url_trabajo = 'c:/00_python/'

# Crear un diccionario con 20 líneas de datos
datos_diccionario = [
    {'ID': 301, 'Nombre': 'Laura', 'Edad': 32, 'Ciudad': 'Madrid', 'Ingresos Mensuales': 3000.50, 'Fecha de Registro': '2023-01-10', 'Empleados a Cargo': 3, 'Activo': True},
    {'ID': 302, 'Nombre': 'Manuel', 'Edad': 45, 'Ciudad': 'Barcelona', 'Ingresos Mensuales': 5000.75, 'Fecha de Registro': '2023-03-15', 'Empleados a Cargo': 5, 'Activo': False},
    {'ID': 303, 'Nombre': 'Sara', 'Edad': 28, 'Ciudad': 'Valencia', 'Ingresos Mensuales': 3200.00, 'Fecha de Registro': '2023-04-20', 'Empleados a Cargo': 1, 'Activo': True},
    {'ID': 304, 'Nombre': 'Pablo', 'Edad': 50, 'Ciudad': 'Sevilla', 'Ingresos Mensuales': 4100.60, 'Fecha de Registro': '2023-05-25', 'Empleados a Cargo': 4, 'Activo': True},
    {'ID': 305, 'Nombre': 'Clara', 'Edad': 37, 'Ciudad': 'Bilbao', 'Ingresos Mensuales': 4800.90, 'Fecha de Registro': '2023-06-30', 'Empleados a Cargo': 6, 'Activo': False},
    {'ID': 306, 'Nombre': 'David', 'Edad': 29, 'Ciudad': 'Madrid', 'Ingresos Mensuales': 2900.00, 'Fecha de Registro': '2023-07-10', 'Empleados a Cargo': 2, 'Activo': True},
    {'ID': 307, 'Nombre': 'Ana', 'Edad': 33, 'Ciudad': 'Barcelona', 'Ingresos Mensuales': 3100.50, 'Fecha de Registro': '2023-02-15', 'Empleados a Cargo': 3, 'Activo': True},
    {'ID': 308, 'Nombre': 'Luis', 'Edad': 41, 'Ciudad': 'Valencia', 'Ingresos Mensuales': 4600.75, 'Fecha de Registro': '2023-03-18', 'Empleados a Cargo': 4, 'Activo': False},
    {'ID': 309, 'Nombre': 'Marta', 'Edad': 26, 'Ciudad': 'Sevilla', 'Ingresos Mensuales': 2800.30, 'Fecha de Registro': '2023-04-25', 'Empleados a Cargo': 1, 'Activo': True},
    {'ID': 310, 'Nombre': 'Jorge', 'Edad': 38, 'Ciudad': 'Bilbao', 'Ingresos Mensuales': 5100.80, 'Fecha de Registro': '2023-05-10', 'Empleados a Cargo': 5, 'Activo': False},
    {'ID': 311, 'Nombre': 'Elena', 'Edad': 36, 'Ciudad': 'Madrid', 'Ingresos Mensuales': 4000.00, 'Fecha de Registro': '2023-06-12', 'Empleados a Cargo': 4, 'Activo': True},
    {'ID': 312, 'Nombre': 'Carlos', 'Edad': 48, 'Ciudad': 'Barcelona', 'Ingresos Mensuales': 3700.25, 'Fecha de Registro': '2023-07-20', 'Empleados a Cargo': 6, 'Activo': False},
    {'ID': 313, 'Nombre': 'Isabel', 'Edad': 27, 'Ciudad': 'Valencia', 'Ingresos Mensuales': 3300.60, 'Fecha de Registro': '2023-08-15', 'Empleados a Cargo': 2, 'Activo': True},
    {'ID': 314, 'Nombre': 'Fernando', 'Edad': 52, 'Ciudad': 'Sevilla', 'Ingresos Mensuales': 5500.90, 'Fecha de Registro': '2023-09-01', 'Empleados a Cargo': 7, 'Activo': True},
    {'ID': 315, 'Nombre': 'Gloria', 'Edad': 30, 'Ciudad': 'Bilbao', 'Ingresos Mensuales': 2700.50, 'Fecha de Registro': '2023-01-25', 'Empleados a Cargo': 1, 'Activo': False},
    {'ID': 316, 'Nombre': 'Raúl', 'Edad': 43, 'Ciudad': 'Madrid', 'Ingresos Mensuales': 4900.75, 'Fecha de Registro': '2023-02-18', 'Empleados a Cargo': 5, 'Activo': True},
    {'ID': 317, 'Nombre': 'Sofía', 'Edad': 34, 'Ciudad': 'Barcelona', 'Ingresos Mensuales': 3600.80, 'Fecha de Registro': '2023-03-12', 'Empleados a Cargo': 3, 'Activo': False},
    {'ID': 318, 'Nombre': 'Héctor', 'Edad': 29, 'Ciudad': 'Valencia', 'Ingresos Mensuales': 3100.40, 'Fecha de Registro': '2023-04-22', 'Empleados a Cargo': 2, 'Activo': True},
    {'ID': 319, 'Nombre': 'Nuria', 'Edad': 39, 'Ciudad': 'Sevilla', 'Ingresos Mensuales': 4500.00, 'Fecha de Registro': '2023-05-17', 'Empleados a Cargo': 4, 'Activo': True},
    {'ID': 320, 'Nombre': 'Andrés', 'Edad': 46, 'Ciudad': 'Bilbao', 'Ingresos Mensuales': 5200.25, 'Fecha de Registro': '2023-06-25', 'Empleados a Cargo': 6, 'Activo': False}
]

# Crear el DataFrame a partir del diccionario
df = pd.DataFrame(datos_diccionario)

# Convertir la columna 'Fecha de Registro' a formato datetime
df['Fecha de Registro'] = pd.to_datetime(df['Fecha de Registro'])

# Mostrar el DataFrame
print(df)

# Exportar el DataFrame a un archivo EXCEL llamado 'datos_exportados.xlsx'
df.to_excel(url_trabajo + 'datos_exportados.xlsx', index=False)
print("Fichero excel exportado")

# Ejemplos de operaciones con DataFrames
# 1. Seleccionar las primeras 5 filas del DataFrame
print(df.head())

# 2. Seleccionar las últimas 5 filas del DataFrame
print(df.tail())

# 3. Obtener información general sobre el DataFrame
print(df.info())

# 4. Describir las estadísticas del DataFrame
print(df.describe())

# 5. Filtrar filas donde 'Ingresos Mensuales' es mayor a 4000
print(df[df['Ingresos Mensuales'] > 4000])

# 6. Agrupar por 'Ciudad' y calcular la media de 'Ingresos Mensuales'
print(df.groupby('Ciudad')['Ingresos Mensuales'].mean())

# 7. Ordenar el DataFrame por 'Edad' de manera descendente
print(df.sort_values(by='Edad', ascending=False))

# 8. Añadir una nueva columna 'Ingresos Anuales'
df['Ingresos Anuales'] = df['Ingresos Mensuales'] * 12
print(df)

# 9. Añadir una nueva columna 'Años Hasta Retiro', suponiendo retiro a los 65 años
df['Años Hasta Retiro'] = 65 - df['Edad']
print(df)

# 10. Añadir una nueva columna 'Ingresos por Empleado'
df['Ingresos por Empleado'] = df.apply(lambda x: x['Ingresos Mensuales'] / x['Empleados a Cargo'] if x['Empleados a Cargo'] > 0 else 0, axis=1)
print(df)

# 11. Eliminar la columna 'Activo'
df.drop(columns=['Activo'], inplace=True)
print(df)

# 12. Filtrar filas donde 'Ciudad' sea 'Madrid' y 'Edad' mayor a 30
print(df[(df['Ciudad'] == 'Madrid') & (df['Edad'] > 30)])

# 13. Resetear el índice del DataFrame
df.reset_index(drop=True, inplace=True)
print(df)

# 14. Reemplazar valores en la columna 'Ciudad' ('Madrid' por 'MADRID')
df['Ciudad'] = df['Ciudad'].replace({'Madrid': 'MADRID'})
print(df)

# 15. Crear una nueva columna 'Categoría de Ingreso' basada en 'Ingresos Mensuales'
df['Categoría de Ingreso'] = pd.cut(df['Ingresos Mensuales'], bins=[0, 3000, 5000, 7000], labels=['Bajo', 'Medio', 'Alto'])
print(df)

# 16. Pivotar el DataFrame por 'Ciudad' y 'Empleados a Cargo'
pivot_df = df.pivot_table(values='Ingresos Mensuales', index='Ciudad', columns='Empleados a Cargo', aggfunc='mean')
print(pivot_df)

# 17. Guardar el DataFrame modificado a un nuevo archivo Excel
df.to_excel(url_trabajo + 'datos_modificados.xlsx', index=False)

# 18. Cargar un DataFrame desde un archivo CSV (ejemplo)
df_csv = pd.read_csv(url_trabajo + 'datos_exportados.csv')
print(df_csv)

# 19. Calcular la correlación entre 'Edad' e 'Ingresos Mensuales'
correlacion = df['Edad'].corr(df['Ingresos Mensuales'])
print(f'Correlación entre Edad e Ingresos Mensuales: {correlacion}')

# 20. Añadir una nueva columna 'Ingresos Netos Anuales' (suponiendo 20% de impuestos)
df['Ingresos Netos Anuales'] = df['Ingresos Anuales'] * 0.8
print(df)

# 21. Contar el número de empleados por cada ciudad
conteo_empleados = df['Ciudad'].value_counts()
print(conteo_empleados)

# 22. Crear una columna 'Fecha de Actualización' con la fecha actual
df['Fecha de Actualización'] = pd.Timestamp.now()
print(df)

# 23. Crear una nueva columna 'Antigüedad en Años' a partir de la 'Fecha de Registro'
df['Antigüedad en Años'] = (pd.Timestamp.now() - df['Fecha de Registro']).dt.days // 365
print(df)

# 24. Guardar el DataFrame con las nuevas columnas a un archivo Excel actualizado
df.to_excel(url_trabajo + 'datos_actualizados.xlsx', index=False)