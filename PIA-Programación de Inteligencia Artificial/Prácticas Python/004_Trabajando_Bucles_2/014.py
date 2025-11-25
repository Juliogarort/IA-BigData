#  Determinar el mayor de tres números: Dado tres números ingresados por el usuario, 
# usa condicionales para determinar cuál es el mayor.

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))

if a >= b and a >= c:
    print("El número mayor es:", a)
elif b >= a and b >= c:
    print("El número mayor es:", b)
else:
    print("El número mayor es:", c)
