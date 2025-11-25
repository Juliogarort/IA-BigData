#  Calculadora simple: Solicita dos números y una operación (+, -, *, /) al usuario y realiza 
# la operación usando condicionales.


num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operacion = input("Ingresa la operación (+, -, *, /): ")

if operacion == "+":
    print("Resultado:", num1 + num2)
elif operacion == "-":
    print("Resultado:", num1 - num2)
elif operacion == "*":
    print("Resultado:", num1 * num2)
elif operacion == "/":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Error: división entre cero.")
else:
    print("Operación no válida.")
