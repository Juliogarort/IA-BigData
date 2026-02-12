# Ejercicio 03.
# Escribir una función que reciba un diccionario con las notas de las asignaturas de
# un curso y una cadena con el nombre de un color y devuelva un diagrama de barras
# de las notas en el color dado.

import matplotlib.pyplot as plt

def ejercicio_03(notas, color):
    print(f"\n--- Ejercicio 03: Diagrama de Barras ---")
    plt.figure(figsize=(10, 6))
    plt.bar(notas.keys(), notas.values(), color=color)
    plt.title('Notas por Asignatura')
    plt.xlabel('Asignatura')
    plt.ylabel('Nota')
    plt.ylim(0, 10)  # Asumiendo notas sobre 10
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Ejemplo de uso
notas_ejemplo = {
    'Matemáticas': 7.5, 
    'Física': 6.0, 
    'Química': 8.2, 
    'Historia': 9.0, 
    'Lengua': 7.0
}
ejercicio_03(notas_ejemplo, 'purple')