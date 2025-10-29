# Escribe un programa que compare dos cadenas carácter por carácter utilizando un bucle while.

cadena1 = input("Introduce la primera cadena: ")
cadena2 = input("Introduce la segunda cadena: ")

longitud_minima = min(len(cadena1), len(cadena2))
i = 0
while i < longitud_minima:
    if cadena1[i] == cadena2[i]:
        print(f"Carácter {i}: '{cadena1[i]}' es igual en ambas cadenas.")
    else:
        print(f"Carácter {i}: '{cadena1[i]}' en la primera cadena es diferente de '{cadena2[i]}' en la segunda cadena.")
    i += 1
if len(cadena1) != len(cadena2):
    print("Las cadenas tienen longitudes diferentes.")
else:
    print("Las cadenas son iguales en longitud.")
    