# Ejercicio 05.
# Escribir una función que reciba una serie de Pandas con el número de ventas de un
# producto durante los meses de un trimestre y un título, y cree un diagrama de
# sectores con las ventas en formato PNG con el título dado. El diagrama debe
# guardarse en un fichero con el formato PNG y el título dado.

import matplotlib.pyplot as plt
import pandas as pd
import os

def ejercicio_05(ventas_s, titulo):
    print(f"\n--- Ejercicio 05: Diagrama de Sectores ({titulo}) ---")
    plt.figure(figsize=(8, 8))
    plt.pie(ventas_s, labels=ventas_s.index, autopct='%1.1f%%', startangle=90)
    plt.title(titulo)
    
    # Obtener la ruta del directorio actual donde se encuentra el script
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_guardado = os.path.join(directorio_actual, f"{titulo}.png")
    
    plt.savefig(ruta_guardado)
    print(f"Gráfico guardado como '{ruta_guardado}'")
    plt.show()

# Ejemplo de uso
ventas_trimestre = pd.Series([1500, 2300, 1800], index=['Enero', 'Febrero', 'Marzo'])
ejercicio_05(ventas_trimestre, "Ventas_Trimestre_1")