# MCD: Escribir una función que encuentre el MCD (Máximo Común Divisor) de dos
# números utilizando el algoritmo de Euclides.

# MCD: Calcular el Máximo Común Divisor de dos números.

a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("El MCD de", a, "y", b, "es", mcd(a, b))
