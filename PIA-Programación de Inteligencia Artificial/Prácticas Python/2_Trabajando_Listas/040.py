# 40. Divide una lista en partes iguales, por ejemplo, una lista de 12 elementos en 3 listas de 4.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
partes = 3
tamaño_parte = len(lista) // partes

listas_divididas = [lista[i * tamaño_parte:(i + 1) * tamaño_parte] for i in range(partes)]
print(listas_divididas)