# Ejercicio 10: Análisis de Puntuaciones de Juegos
# Solicita al usuario las puntuaciones de un jugador en 8 rondas de un juego.
# Crea una Serie con las puntuaciones y asigna números de ronda como índice.
# Calcula la puntuación máxima, mínima y la diferencia entre la más alta y la más baja.
# Muestra las rondas en las que la puntuación es superior a 80.
# Ordena las puntuaciones de menor a mayor y muestra el ranking.

import pandas as pd

num_rondas = 8
puntuaciones = []

print("Ingrese las puntuaciones del jugador en 8 rondas")

# 1. Ingreso de puntuaciones
for i in range(num_rondas):
    while True:
        entrada = input(f"Ronda {i+1}: ")

        if entrada == "":
            print("Error: el campo no puede estar vacío. Intente nuevamente.")
        else:
            try:
                puntuaciones.append(float(entrada))
                break
            except ValueError:
                print("Error: debe ingresar un número válido.")

# 2. Crear la Serie
serie_puntuaciones = pd.Series(
    puntuaciones, index=[f"Ronda {i+1}" for i in range(num_rondas)]
)

# 3. Puntuaciones máxima y mínima
puntuacion_maxima = serie_puntuaciones.max()
puntuacion_minima = serie_puntuaciones.min()
diferencia = puntuacion_maxima - puntuacion_minima

print(f"\nPuntuación máxima: {puntuacion_maxima}")
print(f"Puntuación mínima: {puntuacion_minima}")
print(f"Diferencia entre la más alta y la más baja: {diferencia}")

# 4. Rondas con puntuación superior a 80
print("\nRondas con puntuación superior a 80:")
rondas_altas = serie_puntuaciones[serie_puntuaciones > 80]
if rondas_altas.empty:
    print("Ninguna ronda tuvo puntuación superior a 80.")
else:
    for ronda, puntuacion in rondas_altas.items():
        print(f"{ronda}: {puntuacion}")

# 5. Ranking de puntuaciones (ordenadas de menor a mayor)
serie_ordenada = serie_puntuaciones.sort_values()

print("\nRanking de puntuaciones (de menor a mayor):")
print("-" * 30)
for posicion, (ronda, puntuacion) in enumerate(serie_ordenada.items(), start=1):
    print(f"{posicion}. {ronda}: {puntuacion}")

# 6. Resumen estadístico
print("Ronda                      │ Puntuación")
print("-" * 70)

# Escalado del gráfico
puntuacion_max = serie_ordenada.max()

for ronda, puntuacion in serie_ordenada.items():
    barra_longitud = int((puntuacion / puntuacion_max) * 35)
    barra_longitud = max(1, barra_longitud)

    barra = "█" * barra_longitud
    print(f"{ronda:<20}        │ {barra} {puntuacion}")

print("-" * 70)
print(f"Puntuación máxima de referencia: {puntuacion_max}")
print("=" * 70)


print("")
