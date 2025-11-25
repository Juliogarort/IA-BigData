# TIEMPO: Generar una función que tome un número total de horas, minutos y segundos,
# y devuelva el tiempo total en segundos.


horas = int(input("Ingresa las horas: "))
minutos = int(input("Ingresa los minutos: "))
segundos = int(input("Ingresa los segundos: "))

def tiempo_a_segundos(h, m, s):
    total = h * 3600 + m * 60 + s
    return total

print("El tiempo total en segundos es:", tiempo_a_segundos(horas, minutos, segundos))
