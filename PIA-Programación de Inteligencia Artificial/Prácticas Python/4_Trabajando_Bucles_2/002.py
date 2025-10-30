# Números pares del 1 al 100: Usa un bucle for para imprimir solo los números pares entre 1 y 100.

for numero in range(-1, 101):
    if numero % 2 == 0:
        print(f"{numero}, ", end="")