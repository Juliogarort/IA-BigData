# Crea un programa que:
# 1. Declare un diccionario llamado estudiante con las siguientes claves y valores:
# o "nombre": "Ana"
# o "edad": 22
# o "curso": "Matemáticas"
# 2. Cambia el valor de "edad" a 23.
# 3. Agrega una nueva clave "promedio" con el valor 8.5.
# 4. Imprime todas las claves del diccionario.
# 5. Imprime el valor asociado a la clave "nombre".

# 1. Declarar el diccionario
estudiante = {
    "nombre": "Ana",
    "edad": 22,
    "curso": "Matemáticas"
}
print("--------------------")
print(estudiante)
# 2. Cambiar el valor de "edad"
estudiante["edad"] = 23
print("--------------------")
print(estudiante)

# 3. Agregar una nueva clave "promedio"
estudiante["promedio"] = 8.5
print("--------------------")
print(estudiante)
# 4. Imprimir todas las claves del diccionario
print("Claves del diccionario:", list(estudiante.keys()))

# 5. Imprimir el valor asociado a la clave "nombre"
print("Nombre del estudiante:", estudiante["nombre"])
print("--------------------")
