# Suma de los primeros N números: Usa un bucle para sumar los primeros N números
# (donde N es ingresado por el usuario)

N = int(input("Ingrese un número entero positivo: "))
suma = 0

for i in range(1, N + 1):
    suma += i
print(f"La suma de los primeros {N} números es: {suma}")
