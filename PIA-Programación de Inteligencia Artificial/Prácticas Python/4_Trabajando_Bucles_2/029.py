#  Invertir una cadena: Escribe un programa que invierta una cadena ingresada por el 
# usuario usando un bucle for.

texto = input("Ingresa una cadena: ")
invertida = ""

for c in texto:
    invertida = c + invertida

print("Cadena invertida:", invertida)
