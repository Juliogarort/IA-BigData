# Escribe un programa que busque un número en una lista utilizando un bucle for, y si no lo
# encuentra, muestra un mensaje en el bloque else.

numeros = [3, 7, 12, 19, 24, 31, 45, 52, 67, 78]
numero_a_buscar = int(input("Introduce un numero para buscar en la lista: "))
for numero in numeros:
    if numero == numero_a_buscar:
        print(f"El numero {numero_a_buscar} se ha encontrado en la lista.")
        break
else:
    print(f"El numero {numero_a_buscar} no se ha encontrado en la lista.")
    