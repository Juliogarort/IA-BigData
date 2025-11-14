# Escribe una función que reciba una cadena en formato DD/MM/YYYY y la convierta en un 
# objeto datetime usando strptime().

import datetime

def convertir_cadena_a_fecha(cadena):
    fecha = datetime.datetime.strptime(cadena, "%d/%m/%Y")
    return fecha

print(convertir_cadena_a_fecha("14/11/2025"))
