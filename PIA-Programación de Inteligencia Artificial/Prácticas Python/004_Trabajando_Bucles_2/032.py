#  Encontrar el número mayor en una lista: Escribe un programa que encuentre el número 
# más grande en una lista usando un bucle.

numeros = [int(x) for x in input("Ingresa números separados por espacio: ").split()]
mayor = numeros[0]

for n in numeros:
    if n > mayor:
        mayor = n

print("El número mayor es:", mayor)
