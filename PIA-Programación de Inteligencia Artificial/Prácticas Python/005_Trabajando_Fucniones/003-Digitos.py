# DIGITOS: Escribir una función que sume los dígitos de un número entero positivo.

num = int(input("Ingresa un numerin xfa: "))


def sumar_digitos(num):
    suma = 0
    for digito in str(num):
        suma += int(digito)
    return suma

print("La suma de los dígitos de", num, "es", sumar_digitos(num))
