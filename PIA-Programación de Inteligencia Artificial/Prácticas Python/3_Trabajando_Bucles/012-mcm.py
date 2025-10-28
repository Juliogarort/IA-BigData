# Escribe un programa que encuentre el MCM de dos números utilizando un bucle while.

def mcm(num1, num2):
    mayor = max(num1, num2)
    mcm = mayor
    while True:
        if mcm % num1 == 0 and mcm % num2 == 0:
            return mcm
        mcm += mayor

print("--------------------")
numero1 = int(input("Ingresa el primer número: "))

print("--------------------")
numero2 = int(input("Ingresa el segundo número: "))

resultado = mcm(numero1, numero2)

print("--------------------")
print(f"El MCM de {numero1} y {numero2} es: {resultado}")
print("--------------------")