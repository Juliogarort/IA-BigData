# La Primitiva consiste en seleccionar 6 números aleatorios entre el 1 y el 49. Además, se elige 
# un número complementario y un reintegro (entre 0 y 9). Realizar programa para generar una 
# apuesta de la Primitiva.

import random

print("LA PRIMITIVA \n")

# Generar 6 números aleatorios entre 1 y 49 (sin repetición)
numeros_principales = random.sample(range(1, 50), 6)
numeros_principales.sort()  # Ordenarlos para que se vea mejor

# Generar el número complementario (debe ser diferente a los 6 principales)
numeros_restantes = [n for n in range(1, 50) if n not in numeros_principales]
complementario = random.choice(numeros_restantes)

# Generar el reintegro (entre 0 y 9)
reintegro = random.randint(0, 9)

# Mostrar la apuesta
print("Tu apuesta de la Primitiva:")
print(f"Números principales: {numeros_principales}")
print(f"Complementario: {complementario}")
print(f"Reintegro: {reintegro}")
print("\n¡Mucha suerte! ")