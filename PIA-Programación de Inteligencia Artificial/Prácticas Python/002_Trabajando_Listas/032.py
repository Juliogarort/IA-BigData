# 32. Usa enumerate() para imprimir el índice y el valor de cada elemento de una lista.

ciudades = ["Sevilla Este", "Narnia", "Sevilla", "La Rinconada"]

for indice, ciudad in enumerate(ciudades):
    print(f"Indice: {indice}, Ciudad: {ciudad}")