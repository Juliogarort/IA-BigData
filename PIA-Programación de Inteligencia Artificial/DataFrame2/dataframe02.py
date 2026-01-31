import pandas as pd
import numpy as np

# Mostrar más filas
pd.set_option('display.max_rows', 300)  

# Mostrar más columnas
pd.set_option('display.max_columns', 500) 

# Nombres alumnos
nombres_alumnos = [
    "Juan Pérez", "María López", "Carlos García", "Ana Fernández",
    "Luis Martínez", "Sofía Gómez", "Miguel Rodríguez", "Laura Sánchez",
    "José Torres", "Lucía Morales", "Andrés Herrera", "Carmen Ruiz",
    "Raúl Castro", "Elena Jiménez", "Javier Gil", "Isabel Romero",
    "Hugo Ortiz", "Sara Delgado", "Pablo Ramírez", "Marta Vargas"
]

# Generar notas aleatorias 
notas = {
    "Alumno": nombres_alumnos,
    "Base de Datos": np.random.uniform(1, 10, 20).round(1),
    "Programación": np.random.uniform(1, 10, 20).round(1),
    "Sistemas Informáticos": np.random.uniform(1, 10, 20).round(1),
    "Lenguajes de Marcas": np.random.uniform(1, 10, 20).round(1),
    "Entornos de Desarrollo": np.random.uniform(1, 10, 20).round(1),
}

# DataFrame
df_alumnos = pd.DataFrame(notas)

# Mostrar el DataFrame
print(df_alumnos)


