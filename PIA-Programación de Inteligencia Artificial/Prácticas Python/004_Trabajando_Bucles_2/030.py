# Suma de dígitos: Dado un número, usa un bucle while para sumar todos sus dígitos.

numero = input("Ingresa un número: ")
suma = 0
i = 0

while i < len(numero):
    suma += int(numero[i])
    i += 1

print("Suma de los dígitos:", suma)
