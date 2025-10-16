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