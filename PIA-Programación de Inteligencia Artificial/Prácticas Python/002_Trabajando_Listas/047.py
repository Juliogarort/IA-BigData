# 47. Encuentra los duplicados en una lista de números y elimina las repeticiones.

numeros = [1, 2, 3, 4, 5, 3, 2, 6, 7, 8, 1, 9, 10, 5]
def eliminar_duplicados(lista):
    lista_sin_duplicados = []
    for numero in lista:
        if numero not in lista_sin_duplicados:
            lista_sin_duplicados.append(numero)
    return lista_sin_duplicados
numeros_sin_duplicados = eliminar_duplicados(numeros)

print("--------------------") 
print("Lista original:", numeros)
print("--------------------") 
print("Lista sin duplicados:", numeros_sin_duplicados)
print("--------------------") 