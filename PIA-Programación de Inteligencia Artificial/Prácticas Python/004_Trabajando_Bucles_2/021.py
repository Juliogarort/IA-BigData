#  Suma de números pares en un rango: Usa un bucle para sumar todos los números pares 
# en un rango dado.

inicio = int(input("Inicio del rango: "))
fin = int(input("Fin del rango: "))
suma = 0

for i in range(inicio, fin + 1):
    if i % 2 == 0:
        suma += i

print("La suma de los números pares es:", suma)
