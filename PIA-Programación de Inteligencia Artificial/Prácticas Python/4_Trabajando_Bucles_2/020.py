# Número primo: Escribe un programa que determine si un número es primo.


n = int(input("Ingresa un número: "))
es_primo = True

if n <= 1:
    es_primo = False
else:
    for i in range(2, n):
        if n % i == 0:
            es_primo = False
            break

if es_primo:
    print(n, "es primo.")
else:
    print(n, "no es primo.")
