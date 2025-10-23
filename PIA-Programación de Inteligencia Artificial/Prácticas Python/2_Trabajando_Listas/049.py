# 49. Divide una lista de estudiantes en dos grupos de forma alterna (uno para cada grupo).

def dividir_estudiantes(estudiantes):
    grupo1 = []
    grupo2 = []
    
    for i, estudiante in enumerate(estudiantes):
        if i % 2 == 0:
            grupo1.append(estudiante)
        else:
            grupo2.append(estudiante)
    
    return grupo1, grupo2
# Ejemplo de uso
estudiantes = ["Oc", "José", "Joseca", "Antonio", "Paco", "Pepe", "Elena", "Ana"]

grupo1, grupo2 = dividir_estudiantes(estudiantes)

print("--------------------") 
print("Grupo 1:", grupo1)
print("--------------------") 
print("Grupo 2:", grupo2)
print("--------------------") 