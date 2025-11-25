# Escribe un programa que sume números ingresados por el usuario hasta que ingrese un número negativo utilizando un bucle while

suma = 0
numero = 0

while numero >= 0:
    print("--------------------")
    numero = int(input("Introduce un número para sumar (número negativo para terminar): "))
    if numero >= 0:
        suma += numero
print(f"La suma total de los números ingresados es: {suma}")

