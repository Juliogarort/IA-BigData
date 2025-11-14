# Escribe una función que reciba una fecha en formato DD/MM/YYYY y un número de días, 
# y luego devuelva la nueva fecha después de sumar esos días.

import datetime

def sumar_dias(fecha, dias):
    f = datetime.datetime.strptime(fecha, "%d/%m/%Y")
    nueva = f + datetime.timedelta(days=dias)
    return nueva.strftime("%d/%m/%Y")

print(sumar_dias("10/03/2025", 7))
