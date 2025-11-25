# Escribe un programa que busque el número más grande en una lista utilizando un bucle for

numeros = [3, 5, 2, 8, 1, 4]

maximo = numeros[0]  
for numero in numeros:
    if numero > maximo:
        maximo = numero
print("El número más grande es:", maximo)

