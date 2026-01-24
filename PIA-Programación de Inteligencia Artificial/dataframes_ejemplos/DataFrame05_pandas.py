# DataFrame con origen en Array
import pandas as pd 
import numpy as np

# Array de datos:
datos_array = np.array([
    [301, 'Laura', 32, 'Madrid', 3000.50, '2023-01-10', 3, True],
    [302, 'Manuel', 45, 'Barcelona', 5000.75, '2023-03-15', 5, False],
    [303, 'Sara', 28, 'Valencia', 3200.00, '2023-04-20', 1, True],
    [304, 'Pablo', 50, 'Sevilla', 4100.60, '2023-05-25', 4, True],
    [305, 'Clara', 37, 'Bilbao', 4800.90, '2023-06-30', 6, False],
    [306, 'David', 29, 'Madrid', 2900.00, '2023-07-10', 2, True],
    [307, 'Ana', 33, 'Barcelona', 3100.50, '2023-02-15', 3, True],
    [308, 'Luis', 41, 'Valencia', 4600.75, '2023-03-18', 4, False],
    [309, 'Marta', 26, 'Sevilla', 2800.30, '2023-04-25', 1, True],
    [310, 'Jorge', 38, 'Bilbao', 5100.80, '2023-05-10', 5, False],
    [311, 'Elena', 36, 'Madrid', 4000.00, '2023-06-12', 4, True],
    [312, 'Carlos', 48, 'Barcelona', 3700.25, '2023-07-20', 6, False],
    [313, 'Isabel', 27, 'Valencia', 3300.60, '2023-08-15', 2, True],
    [314, 'Fernando', 52, 'Sevilla', 5500.90, '2023-09-01', 7, True],
    [315, 'Gloria', 30, 'Bilbao', 2700.50, '2023-01-25', 1, False],
    [316, 'Raúl', 43, 'Madrid', 4900.75, '2023-02-18', 5, True],
    [317, 'Sofía', 34, 'Barcelona', 3600.80, '2023-03-12', 3, False],
    [318, 'Héctor', 29, 'Valencia', 3100.40, '2023-04-22', 2, True],
    [319, 'Nuria', 39, 'Sevilla', 4500.00, '2023-05-17', 4, True],
    [320, 'Andrés', 46, 'Bilbao', 5200.25, '2023-06-25', 6, False],
    [321, 'Beatriz', 31, 'Madrid', 3400.50, '2023-07-30', 3, True],
    [322, 'Pablo', 44, 'Barcelona', 4700.75, '2023-08-05', 5, False],
    [323, 'Mónica', 28, 'Valencia', 2800.90, '2023-09-10', 1, True],
    [324, 'Javier', 37, 'Sevilla', 3900.60, '2023-01-15', 4, True],
    [325, 'Teresa', 42, 'Bilbao', 5000.30, '2023-02-20', 6, False],
    [326, 'Rosa', 35, 'Madrid', 3800.75, '2023-03-18', 3, True],
    [327, 'Miguel', 49, 'Barcelona', 4300.50, '2023-04-22', 4, True],
    [328, 'Claudia', 33, 'Valencia', 3200.25, '2023-05-12', 2, False],
    [329, 'Alberto', 38, 'Sevilla', 4100.80, '2023-06-10', 3, True],
    [330, 'Patricia', 40, 'Bilbao', 4600.00, '2023-07-05', 5, False],
    [331, 'Iván', 31, 'Madrid', 3000.40, '2023-08-18', 2, True],
    [332, 'Esther', 45, 'Barcelona', 5100.60, '2023-09-25', 6, True],
    [333, 'Roberto', 50, 'Valencia', 4800.30, '2023-01-05', 4, False],
    [334, 'Silvia', 29, 'Sevilla', 3500.90, '2023-02-14', 3, True],
    [335, 'Adrián', 36, 'Bilbao', 4000.50, '2023-03-21', 5, True],
    [336, 'Carmen', 47, 'Madrid', 5200.75, '2023-04-15', 6, False],
    [337, 'Mario', 32, 'Barcelona', 3100.00, '2023-05-25', 2, True],
    [338, 'Lucía', 28, 'Valencia', 3300.25, '2023-06-05', 3, True],
    [339, 'Gonzalo', 41, 'Sevilla', 4500.80, '2023-07-10', 4, False],
    [340, 'Alicia', 35, 'Bilbao', 4700.90, '2023-08-22', 5, True],
    [341, 'Eduardo', 39, 'Madrid', 3800.60, '2023-09-12', 3, True],
    [342, 'Raquel', 44, 'Barcelona', 4000.30, '2023-01-20', 4, False],
    [343, 'Lorena', 33, 'Valencia', 3600.75, '2023-02-18', 2, True],
    [344, 'Óscar', 49, 'Sevilla', 5100.40, '2023-03-22', 6, True],
    [345, 'Julia', 26, 'Bilbao', 2900.00, '2023-04-25', 1, False],
    [346, 'Víctor', 38, 'Madrid', 4800.50, '2023-05-15', 4, True],
    [347, 'Laura', 50, 'Barcelona', 5400.80, '2023-06-30', 7, False],
    [348, 'Tomás', 29, 'Valencia', 3100.60, '2023-07-25', 2, True],
    [349, 'Daniela', 47, 'Sevilla', 4500.90, '2023-08-18', 5, True],
    [350, 'Felipe', 34, 'Bilbao', 3800.40, '2023-09-01', 3, False]
])

# Definir las columnas correspondientes
columnas = ['ID', 'Nombre', 'Edad', 'Ciudad', 'Ingresos Mensuales', 'Fecha de Registro', 'Empleados a Cargo', 'Activo']

# Crear el DataFrame a partir del array
df = pd.DataFrame(datos_array, columns=columnas)

# Convertir la columna 'Fecha de Registro' a formato datetime
df['Fecha de Registro'] = pd.to_datetime(df['Fecha de Registro'])

# Convertir columnas numéricas a tipo adecuado
df['ID'] = df['ID'].astype(int)
df['Edad'] = df['Edad'].astype(int)
df['Ingresos Mensuales'] = df['Ingresos Mensuales'].astype(float)
df['Empleados a Cargo'] = df['Empleados a Cargo'].astype(int)
df['Activo'] = df['Activo'].astype(bool)

# Mostrar el DataFrame
#print(df)
print(df.dtypes)