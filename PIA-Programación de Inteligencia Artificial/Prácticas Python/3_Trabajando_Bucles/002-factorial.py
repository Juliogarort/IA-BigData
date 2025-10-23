# Escribe un programa que calcule el factorial de un número dado utilizando un bucle while.

numero = int(input("Introduce un número para calcular su factorial: "))
factorial = 1
contador = 1
while contador <= numero:
    factorial *= contador
    contador += 1
print(f"El factorial de {numero} es {factorial}")
