# 1. Crea un diccionario llamado capitales que contenga las siguientes parejas clave-valor:
# o "España": "Madrid"
# o "Francia": "París"
# o "Italia": "Roma"
# 2. Agrega una nueva pareja clave-valor "Alemania": "Berlín".
# 3. Cambia el valor asociado a la clave "Francia" para que sea "Lyon".
# 4. Elimina la entrada correspondiente a "Italia".
# 5. Imprime todas las claves del diccionario.
# 6. Imprime todos los valores del diccionario.
# 7. Imprime el diccionario final.

# 1. diccionario
capitales = {
    "España": "Madrid",
    "Francia": "París",
    "Italia": "Roma"
}
print("Diccionario inicial:", capitales)
print("--------------------")

# 2. agregar nueva pareja clave-valor
capitales["Alemania"] = "Berlín"

# 3. cambiar valor asociado a "Francia"
capitales["Francia"] = "Lyon"

# 4. eliminar entrada
del capitales["Italia"]
# 5. imprimir todas las claves
print("Diccionario completo 'claves':", list(capitales.keys()))
print("--------------------")

# 6. imprimir todos los valores
print("Diccionario completo 'valores':", list(capitales.values()))
print("--------------------")

# 7. imprimir diccionario final
print("Diccionario final:", capitales)
print("--------------------")