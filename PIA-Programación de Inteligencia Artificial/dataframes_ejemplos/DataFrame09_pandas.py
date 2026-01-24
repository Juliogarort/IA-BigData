# Cargar DATAFRAME desde datos de SQL.      

import sqlite3
import pandas as pd

# Conectar a la base de datos "colegio"
conexion = sqlite3.connect("colegio.db")

# Crear una consulta SQL para seleccionar los campos deseados de la tabla "alumnos"
consulta_sql = """
SELECT Nombre, apellidos, edad, correo_electronico, direccion, sexo, telefono
FROM alumnos
"""

# Cargar los datos en un DataFrame de Pandas
df_alumnos = pd.read_sql_query(consulta_sql, conexion)

# Cerrar la conexión con la base de datos
conexion.close()

# Mostrar el DataFrame para verificar los datos
print(df_alumnos)
