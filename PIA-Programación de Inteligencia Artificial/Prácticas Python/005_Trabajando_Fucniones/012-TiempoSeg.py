# TIEMPO SEGUNDOS: Generar una función que tome un número total de segundos y lo
# convierta a horas, minutos y segundos.


total_segundos = int(input("Ingresa el total de segundos: "))

def segundos_a_tiempo(segundos):
    horas = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60
    return horas, minutos, segundos

h, m, s = segundos_a_tiempo(total_segundos)
print("Equivale a:", h, "horas,", m, "minutos y", s, "segundos.")
