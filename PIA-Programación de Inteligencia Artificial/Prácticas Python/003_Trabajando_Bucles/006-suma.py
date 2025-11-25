# Escribe un programa que sume los dígitos de un número utilizando un bucle while.

numero = input("Introduce un número: ")
suma = 0
i = 0

while i < len(numero):
    suma += int(numero[i])
    i += 1
print(f"La suma de los dígitos del número {numero} es: {suma}")
