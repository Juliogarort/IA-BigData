# 50. Crea una lista de enteros y usa reduce() para obtener el producto de todos los elementos.

numeros = [1, 2, 3, 4, 5]

from functools import reduce
producto = reduce(lambda x, y: x * y, numeros)

print("--------------------") 
print("El producto de todos los elementos es:", producto)
print("--------------------") 