# DataFrame con lista de Diccionario
import pandas as pd

# Lista de Diccionario
datos_diccionario = [
    {'ID': 201, 'Nombre': 'Andrés', 'Edad': 26, 'Ciudad': 'Madrid', 'Ingresos Mensuales': 2800.50, 'Fecha de Registro': '2023-03-01', 'Empleados a Cargo': 1, 'Activo': True},
    {'ID': 202, 'Nombre': 'Beatriz', 'Edad': 31, 'Ciudad': 'Barcelona', 'Ingresos Mensuales': 3500.75, 'Fecha de Registro': '2022-11-15', 'Empleados a Cargo': 3, 'Activo': True},
    {'ID': 203, 'Nombre': 'Carlos', 'Edad': 29, 'Ciudad': 'Valencia', 'Ingresos Mensuales': 4000.00, 'Fecha de Registro': '2023-01-10', 'Empleados a Cargo': 2, 'Activo': False},
    {'ID': 204, 'Nombre': 'Diana', 'Edad': 27, 'Ciudad': 'Sevilla', 'Ingresos Mensuales': 3300.60, 'Fecha de Registro': '2023-02-20', 'Empleados a Cargo': 4, 'Activo': True},
    {'ID': 205, 'Nombre': 'Elena', 'Edad': 35, 'Ciudad': 'Bilbao', 'Ingresos Mensuales': 4600.90, 'Fecha de Registro': '2022-10-05', 'Empleados a Cargo': 5, 'Activo': False},
    {'ID': 206, 'Nombre': 'Francisco', 'Edad': 24, 'Ciudad': 'Madrid', 'Ingresos Mensuales': 2500.00, 'Fecha de Registro': '2023-04-15', 'Empleados a Cargo': 0, 'Activo': True},
    {'ID': 207, 'Nombre': 'Gloria', 'Edad': 33, 'Ciudad': 'Barcelona', 'Ingresos Mensuales': 3700.40, 'Fecha de Registro': '2023-05-18', 'Empleados a Cargo': 6, 'Activo': True},
    {'ID': 208, 'Nombre': 'Héctor', 'Edad': 28, 'Ciudad': 'Valencia', 'Ingresos Mensuales': 3900.30, 'Fecha de Registro': '2023-06-25', 'Empleados a Cargo': 2, 'Activo': False},
    {'ID': 209, 'Nombre': 'Isabel', 'Edad': 36, 'Ciudad': 'Sevilla', 'Ingresos Mensuales': 4200.75, 'Fecha de Registro': '2023-07-12', 'Empleados a Cargo': 7, 'Activo': True},
    {'ID': 210, 'Nombre': 'Javier', 'Edad': 39, 'Ciudad': 'Bilbao', 'Ingresos Mensuales': 4800.50, 'Fecha de Registro': '2023-08-01', 'Empleados a Cargo': 8, 'Activo': False}
]
# Crear el DataFrame a partir de la lista de diccionarios
df = pd.DataFrame(datos_diccionario)

# Convertir la columna 'Fecha de Registro' a formato datetime
df['Fecha de Registro'] = pd.to_datetime(df['Fecha de Registro'])

# Mostrar el DataFrame
print(df)
