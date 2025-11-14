# Crea una función que reciba una fecha en formato YYYY-MM-DD y la convierta en el 
# formato DD/MM/YYYY.

import datetime

def convertir_formato(fecha):
    f = datetime.datetime.strptime(fecha, "%Y-%m-%d")
    return f.strftime("%d/%m/%Y")

print(convertir_formato("2025-03-10"))
