# DataFrame Esportación a CSV y EXCEL
import pandas as pd

# Datos de Diccionario
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
    {'ID': 320, 'Nombre': 'Andrés', 'Edad': 46, 'Ciudad': 'Bilbao', 'Ingresos Mensuales': 5200.25, 'Fecha de Registro': '2023-06-25', 'Empleados a Cargo': 6, 'Activo': False},
    {'ID': 321, 'Nombre': 'Beatriz', 'Edad': 31, 'Ciudad': 'Madrid', 'Ingresos Mensuales': 3400.50, 'Fecha de Registro': '2023-07-30', 'Empleados a Cargo': 3, 'Activo': True},
    {'ID': 322, 'Nombre': 'Pablo', 'Edad': 44, 'Ciudad': 'Barcelona', 'Ingresos Mensuales': 4700.75, 'Fecha de Registro': '2023-08-05', 'Empleados a Cargo': 5, 'Activo': False},
    {'ID': 323, 'Nombre': 'Mónica', 'Edad': 28, 'Ciudad': 'Valencia', 'Ingresos Mensuales': 2800.90, 'Fecha de Registro': '2023-09-10', 'Empleados a Cargo': 1, 'Activo': True},
    {'ID': 324, 'Nombre': 'Javier', 'Edad': 37, 'Ciudad': 'Sevilla', 'Ingresos Mensuales': 3900.60, 'Fecha de Registro': '2023-01-15', 'Empleados a Cargo': 4, 'Activo': True},
    {'ID': 325, 'Nombre': 'Teresa', 'Edad': 42, 'Ciudad': 'Bilbao', 'Ingresos Mensuales': 5000.30, 'Fecha de Registro': '2023-02-20', 'Empleados a Cargo': 6, 'Activo': False},
    {'ID': 326, 'Nombre': 'Rosa', 'Edad': 35, 'Ciudad': 'Madrid', 'Ingresos Mensuales': 3800.75, 'Fecha de Registro': '2023-03-18', 'Empleados a Cargo': 3, 'Activo': True},
    {'ID': 327, 'Nombre': 'Miguel', 'Edad': 49, 'Ciudad': 'Barcelona', 'Ingresos Mensuales': 4300.50, 'Fecha de Registro': '2023-04-22', 'Empleados a Cargo': 4, 'Activo': True},
    {'ID': 328, 'Nombre': 'Claudia', 'Edad': 33, 'Ciudad': 'Valencia', 'Ingresos Mensuales': 3200.25, 'Fecha de Registro': '2023-05-12', 'Empleados a Cargo': 2, 'Activo': False},
    {'ID': 329, 'Nombre': 'Alberto', 'Edad': 38, 'Ciudad': 'Sevilla', 'Ingresos Mensuales': 4100.80, 'Fecha de Registro': '2023-06-10', 'Empleados a Cargo': 3, 'Activo': True},
    {'ID': 330, 'Nombre': 'Patricia', 'Edad': 40, 'Ciudad': 'Bilbao', 'Ingresos Mensuales': 4600.00, 'Fecha de Registro': '2023-07-05', 'Empleados a Cargo': 5, 'Activo': False},
    {'ID': 331, 'Nombre': 'Iván', 'Edad': 31, 'Ciudad': 'Madrid', 'Ingresos Mensuales': 3000.40, 'Fecha de Registro': '2023-08-18', 'Empleados a Cargo': 2, 'Activo': True},
    {'ID': 332, 'Nombre': 'Esther', 'Edad': 45, 'Ciudad': 'Barcelona', 'Ingresos Mensuales': 5100.60, 'Fecha de Registro': '2023-09-25', 'Empleados a Cargo': 6, 'Activo': True},
    {'ID': 333, 'Nombre': 'Roberto', 'Edad': 50, 'Ciudad': 'Valencia', 'Ingresos Mensuales': 4800.30, 'Fecha de Registro': '2023-01-05', 'Empleados a Cargo': 4, 'Activo': False},
    {'ID': 334, 'Nombre': 'Silvia', 'Edad': 29, 'Ciudad': 'Sevilla', 'Ingresos Mensuales': 3500.90, 'Fecha de Registro': '2023-02-14', 'Empleados a Cargo': 3, 'Activo': True},
    {'ID': 335, 'Nombre': 'Adrián', 'Edad': 36, 'Ciudad': 'Bilbao', 'Ingresos Mensuales': 4000.50, 'Fecha de Registro': '2023-03-21', 'Empleados a Cargo': 5, 'Activo': True},
    {'ID': 336, 'Nombre': 'Carmen', 'Edad': 47, 'Ciudad': 'Madrid', 'Ingresos Mensuales': 5200.75, 'Fecha de Registro': '2023-04-15', 'Empleados a Cargo': 6, 'Activo': False},
    {'ID': 337, 'Nombre': 'Mario', 'Edad': 32, 'Ciudad': 'Barcelona', 'Ingresos Mensuales': 3100.00, 'Fecha de Registro': '2023-05-25', 'Empleados a Cargo': 2, 'Activo': True},
    {'ID': 338, 'Nombre': 'Lucía', 'Edad': 28, 'Ciudad': 'Valencia', 'Ingresos Mensuales': 3300.25, 'Fecha de Registro': '2023-06-05', 'Empleados a Cargo': 3, 'Activo': True},
    {'ID': 339, 'Nombre': 'Gonzalo', 'Edad': 41, 'Ciudad': 'Sevilla', 'Ingresos Mensuales': 4500.80, 'Fecha de Registro': '2023-07-10', 'Empleados a Cargo': 4, 'Activo': False},
    {'ID': 340, 'Nombre': 'Alicia', 'Edad': 35, 'Ciudad': 'Bilbao', 'Ingresos Mensuales': 4700.90, 'Fecha de Registro': '2023-08-22', 'Empleados a Cargo': 5, 'Activo': True},
    {'ID': 341, 'Nombre': 'Eduardo', 'Edad': 39, 'Ciudad': 'Madrid', 'Ingresos Mensuales': 3800.60, 'Fecha de Registro': '2023-09-12', 'Empleados a Cargo': 3, 'Activo': True},
    {'ID': 342, 'Nombre': 'Raquel', 'Edad': 44, 'Ciudad': 'Barcelona', 'Ingresos Mensuales': 4000.30, 'Fecha de Registro': '2023-01-20', 'Empleados a Cargo': 4, 'Activo': False},
    {'ID': 343, 'Nombre': 'Lorena', 'Edad': 33, 'Ciudad': 'Valencia', 'Ingresos Mensuales': 3600.75, 'Fecha de Registro': '2023-02-18', 'Empleados a Cargo': 2, 'Activo': True},
    {'ID': 344, 'Nombre': 'Óscar', 'Edad': 49, 'Ciudad': 'Sevilla', 'Ingresos Mensuales': 5100.40, 'Fecha de Registro': '2023-03-22', 'Empleados a Cargo': 6, 'Activo': True},
    {'ID': 345, 'Nombre': 'Julia', 'Edad': 26, 'Ciudad': 'Bilbao', 'Ingresos Mensuales': 2900.00, 'Fecha de Registro': '2023-04-25', 'Empleados a Cargo': 1, 'Activo': False},
    {'ID': 346, 'Nombre': 'Víctor', 'Edad': 38, 'Ciudad': 'Madrid', 'Ingresos Mensuales': 4800.50, 'Fecha de Registro': '2023-05-15', 'Empleados a Cargo': 4, 'Activo': True},
    {'ID': 347, 'Nombre': 'Laura', 'Edad': 50, 'Ciudad': 'Barcelona', 'Ingresos Mensuales': 5400.80, 'Fecha de Registro': '2023-06-30', 'Empleados a Cargo': 7, 'Activo': False},
    {'ID': 348, 'Nombre': 'Tomás', 'Edad': 29, 'Ciudad': 'Valencia', 'Ingresos Mensuales': 3100.60, 'Fecha de Registro': '2023-07-25', 'Empleados a Cargo': 2, 'Activo': True},
    {'ID': 349, 'Nombre': 'Daniela', 'Edad': 47, 'Ciudad': 'Sevilla', 'Ingresos Mensuales': 4500.90, 'Fecha de Registro': '2023-08-18', 'Empleados a Cargo': 5, 'Activo': True},
    {'ID': 350, 'Nombre': 'Felipe', 'Edad': 34, 'Ciudad': 'Bilbao', 'Ingresos Mensuales': 3800.40, 'Fecha de Registro': '2023-09-01', 'Empleados a Cargo': 3, 'Activo': False}
]

# Crear el DataFrame a partir del diccionario
df = pd.DataFrame(datos_diccionario)

# Convertir la columna 'Fecha de Registro' a formato datetime
df['Fecha de Registro'] = pd.to_datetime(df['Fecha de Registro'])

# Mostrar el DataFrame
print(df)

# Exportar DataFrame a fichero CSV
df.to_csv('c:/00_python/datos_exportados.csv', index=False)
print("\nEXPORTACION DATOS a CSV....... \n")
# Nota; index=False se indica que NO copie el índice del DF.

# Exportar DataFrame a EXCEL
df.to_excel('c:/00_python/datos_exportados_excel.xlsx', index=False)
# Si falla exportación a Excel;
# se debe instalar módulo "openpyxl"
# en consola ejecutar lo siguiente; pip install openpyxl
print("\nEXPORTACION DATOS a EXCEL....... \n")
