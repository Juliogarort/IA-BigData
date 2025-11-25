#  Imprimir números divisibles por 3 y 5: Usa un bucle para imprimir los números entre 1 
# y 100 que sean divisibles por 3 y 5.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
