# Crea un programa que:
# 1. Declare una lista llamada números que contenga los valores [3, 8, 1, 6, 0, 8, 4].
# 2. Agrega un nuevo número al final de la lista (elige cualquier número).
# 3. Elimina el primer elemento de la lista.
# 4. Ordena la lista de menor a mayor.
# 5. Imprime la lista y su longitud

numeros = [3, 8, 1, 6, 0, 8, 4]
print("--------------------")

print("Lista inicial:", numeros)

print("--------------------")
numeros.append(5) # add numero al final
print("Lista con numero al final:", numeros)

print("--------------------")
numeros.pop(0) # elimina el primer elemento
print("Lista con primer elemento eliminado:", numeros)

print("--------------------")
numeros.sort() # lista ordenada
print("Lista ordenada:", numeros)

print("--------------------")
longitud = len(numeros)
print("Longitud de la lista:", longitud)