# Obtener el mayor de dos números. Crear una función lambda que devuelva el mayor
# de dos números.


num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

mayor = lambda a, b: a if a > b else b

print("El número mayor es:", mayor(num1, num2))
