#  Números perfectos: Escribe un programa que encuentre todos los números perfectos 
# entre 1 y 1000 (un número perfecto es igual a la suma de sus divisores propios).

for n in range(1, 1001):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    if suma == n:
        print(n, "es un número perfecto")
