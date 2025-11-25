# Realizar la simulación de una Quiniela con 15 partidos. Para cada partido, el resultado puede 
# ser “1” (gana el local), “X” (empate” o “2” (gana el visitante). 

import random

print("LA QUINIELA")
print("1 = Gana el local | X = Empate | 2 = Gana el visitante\n")

resultados = ['1', 'X', '2']

for partido in range(1, 16):
    resultado = random.choice(resultados)
    print(f"Partido {partido:2d}: {resultado}")

print("\n¡Quiniela generada!")