# Elevar una función al cuadrado. Utilizar una función lambda para elevar un número al
# cuadrado.


num = int(input("Ingresa un número para elevar al cuadrado: "))

cuadrado = lambda x: x ** 2

print("El cuadrado de", num, "es", cuadrado(num))
