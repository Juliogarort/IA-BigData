# Sumar solo los números positivos: Usa un bucle para sumar solo los números positivos 
# en una lista. 


numeros = [int(x) for x in input("Ingresa números separados por espacio: ").split()]
suma = 0

for n in numeros:
    if n > 0:
        suma += n

print("Suma de los positivos:", suma)
