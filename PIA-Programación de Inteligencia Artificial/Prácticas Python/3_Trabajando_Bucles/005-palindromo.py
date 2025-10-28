# Escribe un programa que verifique si una palabra es un palíndromo utilizando un bucle
# while.

palabra = input("Introduce una palabra: ")
longitud = len(palabra)

es_palindromo = True
i = 0
while i < longitud // 2:
    if palabra[i] != palabra[longitud - 1 - i]:
        es_palindromo = False
        break
    i += 1
if es_palindromo:
    print(f"La palabra '{palabra}' es un palíndromo.")
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")
