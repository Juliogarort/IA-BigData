# Simular el lanzamiento de dos dados de seis caras y mostrar el resultado de cada dado y la 
# suma total.

import random

# Tiración de dados
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

# Suma
suma_total = dado1 + dado2

# Resultados
print("Tiración de dados: ")
print(f"Dado 1: {dado1}")
print(f"Dado 2: {dado2}")
print(f"Suma total: {suma_total}")
