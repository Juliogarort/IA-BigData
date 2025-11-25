# Simular la versión básica del juego del BlackJack. Repartir cartas al azar hasta que el jugador 
# decida plantarse o supere 21.

import random

# Función para obtener una carta aleatoria
def obtener_carta():
    cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  
    return random.choice(cartas)

print("♠️♥️ BLACKJACK ♣️♦️")
suma_jugador = 0

# Repartir dos cartas iniciales
carta1 = obtener_carta()
carta2 = obtener_carta()
suma_jugador = carta1 + carta2

print(f"Tus cartas iniciales: {carta1} y {carta2}")
print(f"Suma actual: {suma_jugador}")

while suma_jugador < 21:
    decision = input("\n¿Quieres otra carta? (s/n): ").lower()
    
    if decision == 's':
        nueva_carta = obtener_carta()
        suma_jugador += nueva_carta
        print(f"Nueva carta: {nueva_carta}")
        print(f"Suma actual: {suma_jugador}")
    elif decision == 'n':
        print(f"Te plantas con {suma_jugador}")
        break
    else:
        print("Respuesta no válida. Escribe 's' para sí o 'n' para no")

print("\n--- Resultado  ---")
if suma_jugador > 21:
    print(f"¡Te pasaste! Suma: {suma_jugador}. Has perdido.")
elif suma_jugador == 21:
    print(f"¡BLACKJACK! ¡Has ganado!")
else:
    print(f"Te plantaste con {suma_jugador}. ¡Buen juego!")