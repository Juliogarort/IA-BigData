# Realizar la simulación de la mezcla de una baraja de cartas estándar (52 cartas) y realizar el 
# reparto de 5 cartas al azar. 

import random

palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

baraja = []
for palo in palos:
    for valor in valores:
        baraja.append(f"{valor} de {palo}")

random.shuffle(baraja)

print("Repartiendo las casrtas")
print("Tu mano es:")
for i in range(5):
    print(f"{i+1}. {baraja[i]}")