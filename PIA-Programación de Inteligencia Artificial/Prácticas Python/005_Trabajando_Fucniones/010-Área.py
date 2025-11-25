# ÁREA: Escribir una función que calcule el área de un círculo dado su radio. 


radio = float(input("Ingresa el radio del círculo: "))

def area_circulo(r):
    pi = 3.1416
    return pi * r * r

print("El área del círculo es:", area_circulo(radio))
