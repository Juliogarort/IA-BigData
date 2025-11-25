# ORDEN: Crear una función que ordene una lista de números de menor a mayor sin usar
# el método sort()



numeros = input("Ingresa números separados por espacios: ")
lista = [int(n) for n in numeros.split()]

def ordenar_lista(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[i]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

print("Lista ordenada:", ordenar_lista(lista))
