# Calculadora de promedio: Solicita al usuario ingresar números hasta que ingrese un 
# cero, luego calcula el promedio de los números ingresados.

suma = 0
contador = 0

while True:
    num = float(input("Ingresa un número (0 para terminar): "))
    if num == 0:
        break
    suma += num
    contador += 1

if contador > 0:
    print("Promedio:", suma / contador)
else:
    print("No ingresaste números.")
