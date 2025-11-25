#  Generar números aleatorios hasta que sea cero: Usa un bucle para generar números 
# aleatorios entre 1 y 10 hasta que se genere un cero.

import random

num = random.randint(0, 10)
while num != 0:
    print("Número generado:", num)
    num = random.randint(0, 10)

print("¡Se generó un cero! Fin del programa.")


