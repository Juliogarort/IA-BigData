#  Juego de adivinanza: Crea un programa donde el usuario debe adivinar un número entre 
# 1 y 100, dándole pistas de si el número es mayor o menor.

import random

numero_secreto = random.randint(1, 100)
intento = 0
adivinado = False

while not adivinado:
    intento = int(input("Adivina el número (1-100): "))
    if intento < numero_secreto:
        print("El número es mayor.")
    elif intento > numero_secreto:
        print("El número es menor.")
    else:
        print("¡Correcto! El número era", numero_secreto)
        adivinado = True
