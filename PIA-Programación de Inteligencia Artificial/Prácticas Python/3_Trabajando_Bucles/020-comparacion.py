# Escribe un programa que compare dos listas y cuente cuántos elementos coinciden utilizando
# un bucle for.

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

comunes = 0

for elemento in lista1:
    if elemento in lista2:
        comunes += 1
print(f"Número de elementos comunes: {comunes}")

print("Elementos comunes:", end=" ")
for elemento in lista1:
    if elemento in lista2:
        print(elemento, end=" ")