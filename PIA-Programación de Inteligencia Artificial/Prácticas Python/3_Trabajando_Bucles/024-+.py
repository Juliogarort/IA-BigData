# Escribe un programa que encuentre el número mayor y el menor de una lista utilizando un bucle for

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
mayor = numeros[0]
menor = numeros[0]  

for numero in numeros:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
print("El número mayor es:", mayor)
print("El número menor es:", menor)

