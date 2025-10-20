# 1. Crea un diccionario llamado clase con la siguiente estructura:

# 2. Agrega un tercer estudiante llamado "Pedro", de 21 años, con las materias
# "Historia" y "Geografía".
# 3. Imprime el nombre y la edad de todos los estudiantes.
# 4. Cambia la edad de "Marta" a 21 años.
# 5. Elimina las materias de "Carlos".

# 1. Crear el diccionario clase
clase = {
    "estudiante1": {
    "nombre": "Carlos",
    "edad": 19,
    "materias": ["Matemáticas", "Física"]
    },
    "estudiante2": {
    "nombre": "Marta",
    "edad": 20,
    "materias": ["Química", "Biología"]
    }
}

# 2. Agregar un tercer estudiante
clase ["estudiante3"] = {
    "nombre": "Pedro",
    "edad": 21,
    "materias": ["Historia", "Geografía"]
    }

# 3. Imprimir el nombre y la edad de todos los estudiantes
for estudiante in clase.values():
    print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}")

# 4. Cambiar la edad de "Marta" a 21 años
clase["estudiante2"]["edad"] = 21

# 5. Eliminar las materias de "Carlos"
clase["estudiante1"]["materias"] = []
print("--------------------")
for estudiante in clase.values():
    print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Materias: {estudiante['materias']}")

print("--------------------")