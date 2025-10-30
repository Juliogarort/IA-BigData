# Factorial de un número: Escribe un programa que calcule el factorial de un número
# usando un bucle.

numero = int(input("Introduce un número para calcular su factorial: "))
factorial = 1

for i in range(1, numero + 1):
    factorial *= i
print(f"El factorial de {numero} es {factorial}")
