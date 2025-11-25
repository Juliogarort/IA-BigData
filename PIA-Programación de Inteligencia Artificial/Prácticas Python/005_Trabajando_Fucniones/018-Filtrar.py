# Filtrar números pares en una lista. Usa una función lambda con filter() para obtener
# sólo los números pares de una lista.


numeros = input("Ingresa varios números separados por espacios: ")
lista = [int(n) for n in numeros.split()]

pares = list(filter(lambda x: x % 2 == 0, lista))

print("Los números pares son:", pares)
