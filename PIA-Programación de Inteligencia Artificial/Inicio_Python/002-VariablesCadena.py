# Crea un programa que:
# 1. Declare dos variables de tipo cadena: nombre con el valor "Juan" y apellido con el
# valor "Pérez".
# 2. Concatenar las dos cadenas en una nueva variable nombre_completo, separadas por
# un espacio.
# 3. Imprime la longitud de la cadena nombre_completo.
# 4. Convierte nombre_completo a mayúsculas y minúsculas

nombre = "Juan"
apellido = "Perez"

nombre_completo = nombre + " " + apellido
longitud = len(nombre_completo)
mayusculas = nombre_completo.upper()

print("Nombre completo:", nombre_completo)
print("Longitud del nombre completo:", longitud)