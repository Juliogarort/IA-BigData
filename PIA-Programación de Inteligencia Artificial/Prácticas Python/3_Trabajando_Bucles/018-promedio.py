# Escribe un programa que calcule el promedio de una lista de números utilizando un bucle for 

numeros = []

cantidad = int(input("¿Cuántos números deseas ingresar? "))
for _ in range(cantidad):
    num = float(input("Ingresa un número: "))
    numeros.append(num)
promedio = sum(numeros) / cantidad

print(f"El promedio de los números ingresados es: {promedio}")
