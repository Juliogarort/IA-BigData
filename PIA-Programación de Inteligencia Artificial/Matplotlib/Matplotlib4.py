# Ejercicio 04.
# Escribir una función que reciba una serie de Pandas con las notas de los alumnos
# de un curso y devuelva un diagrama de cajas con las notas. El diagrama debe tener
# el título “Distribución de Notas”

import matplotlib.pyplot as plt
import pandas as pd

def ejercicio_04(notas_s):
    print(f"\n--- Ejercicio 04: Diagrama de Cajas (Notas) ---")
    plt.figure(figsize=(8, 6))
    plt.boxplot(notas_s)
    plt.title('Distribución de Notas')
    plt.ylabel('Notas')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Ejemplo de uso
notas_serie = pd.Series([5, 6, 7.5, 8, 9, 4, 3, 10, 6.5, 7])
ejercicio_04(notas_serie)