#  Contar números positivos, negativos y ceros: Dado un conjunto de números ingresados 
# por el usuario, cuenta cuántos son positivos, negativos o ceros.

positivos = negativos = ceros = 0

for i in range(5):
    num = int(input("Ingresa un número: "))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        ceros += 1

print("Positivos:", positivos)
print("Negativos:", negativos)
print("Ceros:", ceros)
