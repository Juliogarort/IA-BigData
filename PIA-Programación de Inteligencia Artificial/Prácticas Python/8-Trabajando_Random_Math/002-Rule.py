# Simular el funcionamiento de la ruleta. La ruleta tiene 36 números (del 1 al 36) y un número 
# especial, el 0 (Gana la banca). Realizar la simulación del giro de la ruleta y mostrar el número 
# resultante.

import random

numero_ganador = random.randint(0, 36)

print("Mira la bolita mira la bolita...")
print(f"¡El número ganador es: {numero_ganador}!")

if numero_ganador == 0:
    print("¡Gana la banca!")