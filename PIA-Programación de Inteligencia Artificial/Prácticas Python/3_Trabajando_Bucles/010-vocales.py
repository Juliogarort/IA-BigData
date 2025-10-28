#  Escribe un programa que cuente cuántas vocales hay en una palabra dada utilizando un
# bucle for y una condición if.

palabra = input("Introduce una palabra: ")
vocales = "aeiouAEIOU"
contador = 0

for letra in palabra:
    if letra in vocales:
        contador += 1
print(f"La palabra '{palabra}' tiene {contador} vocales.")
