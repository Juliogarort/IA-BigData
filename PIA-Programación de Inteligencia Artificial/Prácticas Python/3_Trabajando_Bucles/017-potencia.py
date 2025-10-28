# Escribe un programa que calcule la potencia de un número dado utilizando un bucle  for

base = float(input("Introduce la base: "))

exponente = int(input("Introduce el exponente (entero no negativo): "))
resultado = 1
for _ in range(exponente):
    resultado *= base
print(f"{base} elevado a la {exponente} es {resultado}")
