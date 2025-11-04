# Año bisiesto: Escribe un programa que determine si un año es bisiesto.

anio = int(input("Ingresa un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("El año", anio, "es bisiesto")
else:
    print("El año", anio, "no es bisiesto")