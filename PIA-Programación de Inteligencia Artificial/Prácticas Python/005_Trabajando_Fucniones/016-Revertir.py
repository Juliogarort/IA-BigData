# Revertir una cadena. Utiliza una función lambda para invertir una cadena de texto.


texto = input("Escribe una palabra o frase: ")

revertir = lambda cadena: cadena[::-1]

print("La cadena invertida es:", revertir(texto))
