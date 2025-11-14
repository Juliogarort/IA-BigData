# Crea una función que obtenga la fecha y hora actuales, luego formatea la fecha para que 
# se muestre en el formato DD/MM/YYYY HH:MM:SS. 

import datetime

def fecha_actual_formateada():
    fecha_hora = datetime.datetime.now()
    return fecha_hora.strftime("%d/%m/%Y %H:%M:%S")

print(fecha_actual_formateada())
