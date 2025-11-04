#  Contar números primos en un rango: Dado un rango de números, cuenta cuántos son 
# primos.

inicio = int(input("Inicio del rango: "))
fin = int(input("Fin del rango: "))
contador = 0

for n in range(inicio, fin + 1):
    if n > 1:
        es_primo = True
        for i in range(2, n):
            if n % i == 0:
                es_primo = False
                break
        if es_primo:
            contador += 1

print("Hay", contador, "números primos en el rango.")
