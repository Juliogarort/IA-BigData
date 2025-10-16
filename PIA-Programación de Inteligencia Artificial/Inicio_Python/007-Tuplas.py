# 1. Crear una tupla
puntos = (5, 10, 15, 20, 25)
print("Tupla inicial:", puntos)
print("--------------------")

# 2. Imprime el tercer valor de la tupla
print("Valor en la tercera posicion de la tupla:", puntos[2])
print("--------------------")

# 3. Convierte la tupla en una lista
puntos_lista = list(puntos)

# 4. Agrega el valor 30 al final de la lista
puntos_lista.append(30)

# 5. Convierte la lista nuevamente en tupla e imprimela
puntos = tuple(puntos_lista)
print("Tupla final:", puntos)