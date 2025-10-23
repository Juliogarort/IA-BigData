# 1. Números pares con for
# Escribe un programa que imprima todos los números pares entre 1 y 100 utilizando un bucle
# for. Utiliza una condición if para verificar si el número es par.

for numero in range(-1, 101):
    if numero % 2 == 0:
        print(f"{numero}, ", end="")