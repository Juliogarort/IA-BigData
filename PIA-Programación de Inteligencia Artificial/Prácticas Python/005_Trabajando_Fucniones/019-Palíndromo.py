#  Verificar si una cadena es palíndromo. Utilizar una función lambda para verificar si una
# cadena es un palíndromo (se lee igual al derecho y al revés) 


texto = input("Escribe una palabra o frase para comprobar si es palíndromo: ")

es_palindromo = lambda cadena: cadena.lower().replace(" ", "") == cadena.lower().replace(" ", "")[::-1]

if es_palindromo(texto):
    print("✅ Es un palíndromo.")
else:
    print("❌ No es un palíndromo.")
