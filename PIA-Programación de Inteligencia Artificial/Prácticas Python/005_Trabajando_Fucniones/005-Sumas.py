# SUMAS: Escribir una función que reciba una lista y devuelva la suma de sus elementos.


numeros = input("Ingresa varios números separados por espacios: ")
lista = [int(n) for n in numeros.split()]

def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

print("La suma de los números es:", sumar_lista(lista))
