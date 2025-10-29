# Escribe un programa que verifique si un número es perfecto (igual a la suma de sus divisores) utilizando un bucle for.

def es_numero_perfecto(numero):
    if numero < 1:
        return False
    
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
            
    return suma_divisores == numero

# Solicitar al usuario un número
numero_usuario = int(input("Introduce un número para verificar si es perfecto: "))
if es_numero_perfecto(numero_usuario):
    print(f"{numero_usuario} es un número perfecto.")
else:
    print(f"{numero_usuario} no es un número perfecto.")
    