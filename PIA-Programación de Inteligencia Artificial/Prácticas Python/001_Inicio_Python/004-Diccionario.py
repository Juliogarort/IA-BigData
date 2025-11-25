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
