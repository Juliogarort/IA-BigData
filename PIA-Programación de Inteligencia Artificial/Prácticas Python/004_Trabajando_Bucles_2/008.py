# Imprimir los primeros N números impares: Escribe un programa que imprima los
# primeros N números impares utilizando un bucle while.

N = int(input("Ingrese la cantidad de números impares a imprimir: "))

contador = 0
numero = 1

while contador < N:
    print(numero)
    numero += 2
    contador += 1

    