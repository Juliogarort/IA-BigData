# Escribe un programa que encuentre todos los múltiplos de un número en un rango dado utilizando un bucle for.

multiplo = int(input("Introduce el número para encontrar sus múltiplos: "))
rango_inicio = int(input("Introduce el inicio del rango: "))
rango_fin = int(input("Introduce el fin del rango: "))
print(f"Múltiplos de {multiplo} entre {rango_inicio} y {rango_fin}:")
for numero in range(rango_inicio, rango_fin + 1):
    if numero % multiplo == 0:
        print(numero)
            