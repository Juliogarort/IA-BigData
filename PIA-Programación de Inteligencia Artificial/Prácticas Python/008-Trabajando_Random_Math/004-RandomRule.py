# La computadora debe girar la ruleta y el jugador debe adivinar el número. El programa debe 
# indicar si el usuario ha acertado o no con el número. 

import random

numero_ganador = random.randint(0, 36)

print("Adivina el numerin de la rule AB")
print("La ruleta tiene números del 0 al 36")

while True:
    try:
        numero_jugador = int(input("¿Qué número crees que salió? :"))

        if 0 <= numero_jugador <= 36:
            break  
        else:
            print("¡Error! Debes elegir un número entre 0 y 36.")
    except ValueError:
        print("¡Error! Debes introducir un número válido.")

# Mostrar resultado
print(f"\nEl número ganador es: {numero_ganador}")

if numero_jugador == numero_ganador:
    print("¡FELICIDADES! ¡Has acertado!")
else:
    print("Uffff casi eeh! vuelve a intentarlo anda...")
