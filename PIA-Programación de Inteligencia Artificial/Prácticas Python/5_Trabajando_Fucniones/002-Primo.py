#  Primo: : Crear una función que determine si un número es primo

num = int(input("Ingrese un número para ver si es primo o no: "))

def es_primo(num):
    if num <= 1:
        return " jefeee introduce un numero positivo xfa"
    for i in range(2, num):
        if num % i == 0:
            return "no es primo"
    return "es primo"

print("El número", num, "es", es_primo(num))