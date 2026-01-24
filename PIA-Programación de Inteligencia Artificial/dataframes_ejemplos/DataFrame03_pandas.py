# DataFrame desde Lista de Listas
import pandas as pd

# Lista de listas: 
datos_lista = [
    [101, 'Ana', 25, 'Madrid', 2500.75, '2023-01-15', 2, True],
    [102, 'Pedro', 30, 'Barcelona', 3200.50, '2022-12-10', 5, True],
    [103, 'Luis', 35, 'Valencia', 4000.00, '2023-02-20', 3, False],
    [104, 'María', 28, 'Sevilla', 3600.80, '2023-03-05', 4, True],
    [105, 'Jorge', 40, 'Bilbao', 4500.10, '2022-11-25', 7, False],
    [106, 'Sofía', 22, 'Madrid', 2700.60, '2023-04-10', 1, True],
    [107, 'Carlos', 33, 'Barcelona', 3100.00, '2023-05-15', 6, False],
    [108, 'Lucía', 29, 'Valencia', 3900.25, '2023-06-18', 2, True],
    [109, 'Marta', 41, 'Sevilla', 3700.90, '2023-07-22', 5, True],
    [110, 'Fernando', 38, 'Bilbao', 4800.75, '2023-08-30', 8, False]
]
# Definir las columnas correspondientes
columnas = ['ID', 'Nombre', 'Edad', 'Ciudad', 'Ingresos Mensuales', 'Fecha de Registro', 'Empleados a Cargo', 'Activo']

# Crear el DataFrame a partir de la lista de listas
df = pd.DataFrame(datos_lista, columns=columnas)
print(df['Fecha de Registro'])
print(df['Fecha de Registro'].dtype)
# Convertir la columna 'Fecha de Registro' a formato datetime
df['Fecha de Registro'] = pd.to_datetime(df['Fecha de Registro'])
#df['Fecha de Registro'] = pd.to_datetime(df['Fecha de Registro'], format='%Y-%m-%d', errors='coerce')

#Para evitar problemas de truncamiento o tamaño ponemos las dos lineas siguientes para ver todos los datos del DF: 

#pd.set_option('display.max_columns', None)
#pd.set_option('display.width', 1000)


# Mostrar el DataFrame
print(df)

