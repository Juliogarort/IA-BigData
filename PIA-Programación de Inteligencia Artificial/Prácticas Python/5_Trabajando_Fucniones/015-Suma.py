# Suma de dos números. Crear una función lambda que sume dos números.


num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

suma = lambda a, b: a + b

print("La suma de", num1, "y", num2, "es", suma(num1, num2))
