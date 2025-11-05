# Factorial: Escribir una función que calcule el factorial de un número dado

num = int(input("Ingrese un número positivo para calcular su factorial: "))

def factorial(num):
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado

print("El factorioal de", num, "es", factorial(num))