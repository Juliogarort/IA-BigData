# Crea una función que reciba dos cadenas de fecha en formato DD/MM/YYYY y calcule 
# cuántos días hay entre ambas.

import datetime

def diferencia_dias(fecha1, fecha2):
    f1 = datetime.datetime.strptime(fecha1, "%d/%m/%Y")
    f2 = datetime.datetime.strptime(fecha2, "%d/%m/%Y")
    diferencia = f2 - f1
    return diferencia.days

print("La diferencia es de : ", diferencia_dias("14/11/2025", "29/02/2028"), "días")