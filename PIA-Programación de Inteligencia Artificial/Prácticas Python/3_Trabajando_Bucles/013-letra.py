# Escribe un programa que recorra una lista de palabras y cuente cuántas empiezan con
# una letra específica utilizando un bucle for.

palabras = ["Oc", "Melón", "Sevilla", "Guacamole", "Ostras", "Olivo"]

letra_especifica = "O"
contador = 0

for palabra in palabras:
    if palabra.startswith(letra_especifica):
        contador += 1
print(f"Número de palabras que empiezan con la letra '{letra_especifica}': {contador}")


