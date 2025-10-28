# Crea un juego en el que el usuario intente adivinar un número secreto. El programa deberá
# seguir solicitando al usuario que adivine hasta que lo haga correctamente

import random

numero = random.randint(1, 10)

adivinado = False

while not adivinado:
    print("--------------------")
    intento = int(input("Adivina el número secreto (entre 1 y 10): "))
    print(" ")
    if intento == numero:
        adivinado = True
        print("¡Felicidades! Has adivinado el número.") 
        print("--------------------")
        print("--------------------")

    else:
        print("Número incorrecto. Intenta de nuevo.")

