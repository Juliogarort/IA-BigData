#  Determinar el segundo número más grande en una lista: Usa bucles y condicionales 
# para encontrar el segundo número más grande en una lista.

numeros = [int(x) for x in input("Ingresa números separados por espacio: ").split()]
mayor = segundo = float('-inf')

for n in numeros:
    if n > mayor:
        segundo = mayor
        mayor = n
    elif n > segundo and n != mayor:
        segundo = n

print("El segundo número más grande es:", segundo)
