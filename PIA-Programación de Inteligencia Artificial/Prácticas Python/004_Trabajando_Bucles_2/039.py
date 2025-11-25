#  Pares e impares separados: Dada una lista de números, separa los números pares e 
# impares en dos listas diferentes.

numeros = [int(x) for x in input("Ingresa números separados por espacio: ").split()]
pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("Pares:", pares)
print("Impares:", impares)
