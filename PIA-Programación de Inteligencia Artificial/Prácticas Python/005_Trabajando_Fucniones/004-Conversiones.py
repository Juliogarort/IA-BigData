# CONVERSIONES: Crear una función que convierta temperaturas de grados Celsius a 
# Fahrenheit.

num = int(input("Ingresa la temperatura en celsius para pasar a fahrenheit: "))


def celsius_a_fahrenheit(num):
    return (num * 9/5) + 32


print(num, "grados equivalen a ", celsius_a_fahrenheit(num), "fahrenheit")
