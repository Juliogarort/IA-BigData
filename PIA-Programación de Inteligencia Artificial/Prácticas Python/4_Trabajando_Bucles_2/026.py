#  Imprimir los primeros N números primos: Usa bucles y condicionales para imprimir los 
# primeros N números primos.

n = int(input("¿Cuántos números primos quieres ver? "))
contador = 0
num = 2

while contador < n:
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num)
        contador += 1
    num += 1
