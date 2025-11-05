# CONTAR: Generar una función que cuente cuántas vocales hay en una cadena.


texto = input("Escribe una frase: ")

def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
    return contador

print("La frase tiene", contar_vocales(texto), "vocales.")
