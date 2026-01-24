# PANDAS -- DATAFRAMES
# 
 
import pandas as pd

## Creamos DataFrame desde Diccionario

datos = {
        'Nombre':["Juan","Pedro","Marta","Luis","Leticia"],
        'Edad':[18,30,23,40,28],
        'Ciudad':["Sevilla","Málaga","Sevilla","Jerez","Ronda"]
}

df = pd.DataFrame(datos)

print(df)

#Información sobre DataFrame
print ( "- - - - - - - - - - - - - - - - - - - - - -")
#Mostrar primera fila
print("\nPrimeras filas .... ")
print(df.head())
#Indicar número de filas (n)
print(df.head(2))

#Mostrar últimas filas
print("\nUltimas filas")
print(df.tail())
#Indicar N filas
print(df.tail(2))

#Mostrar info general
print("\nInfo general .... ")
print(df.info())

#Mostrar Descripcionx
print("\nDescripción .... ")
print(df.describe())

#Dimensiones
print("\nDimension .... ")
print(df.shape)

#Elementos del DataFrame
print("\nNum. Elementos")
print(df.size)

#Columnas
print("\nColumnas .... ")
print(df.columns)

#Tipos de datos
print("\nDatos .... ")
print(df.dtypes)
