# PASOS: Crear una función que calcule la distancia aproximada recorrida, dado un
# número de pasos, asumiendo que la longitud media de un paso es de 0.78 metros
# (promedio para adultos). Convertir la cantidad de pasos a kilómetros.


pasos = int(input("Ingresa el número de pasos dados: "))

def pasos_a_kilometros(p):
    metros = p * 0.78
    kilometros = metros / 1000
    return kilometros

print("Has recorrido aproximadamente", pasos_a_kilometros(pasos), "kilómetros.")
