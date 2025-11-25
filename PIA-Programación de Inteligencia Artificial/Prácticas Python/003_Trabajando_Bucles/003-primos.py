# Escribe un programa que determine si un número es primo utilizando un bucle for con una condición if.

numero = int(input("Introduce un numero para verificar si es primo: "))
es_primo = True
if numero <= 1:
    es_primo = False
else:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
if es_primo:
    print(f"El numero {numero} es primo.")
else:
    print(f"El numero {numero} no es primo.")
    