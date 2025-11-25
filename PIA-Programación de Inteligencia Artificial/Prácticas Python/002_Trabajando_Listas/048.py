# 48. Crea una lista de nombres y ordénalos por la longitud de cada nombre.

nombres = ["Oc", "José", "Joseca", "Antonio", "Paco", "Pepe", "Elena", "Ana"]

def ordenada(lista):
    return sorted(lista, key=len)
nombres_ordenados = ordenada(nombres)

print("--------------------") 
print("Lista original:", nombres)
print("--------------------") 
print("Lista ordenada por longitud:", nombres_ordenados)
print("--------------------")