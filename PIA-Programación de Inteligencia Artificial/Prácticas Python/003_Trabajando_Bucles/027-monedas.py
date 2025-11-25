# Escribe un programa que simule el lanzamiento de una moneda hasta que salga cara tres veces consecutivas utilizando un bucle while

import random

cara_consecutivas = 0
lanzamientos = 0

while cara_consecutivas < 3:
    lanzamiento = random.choice(['cara', 'cruz'])
    lanzamientos += 1
    print(f"Lanzamiento {lanzamientos}: {lanzamiento}")
    if lanzamiento == 'cara':
        cara_consecutivas += 1
    else:
        cara_consecutivas = 0
print(f"Se han lanzado la moneda {lanzamientos} veces hasta obtener 3 caras consecutivas.")
