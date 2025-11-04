# Palíndromo: Dada una palabra, usa un bucle para determinar si es un palíndromo.

palabra = input("Ingresa una palabra: ").lower()
invertida = ""

for c in palabra:
    invertida = c + invertida

if palabra == invertida:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
