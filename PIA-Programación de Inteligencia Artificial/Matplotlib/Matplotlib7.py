# Ejercicio 07.
# Escribir una función que reciba un dataframe de Pandas con los ingresos y gastos
# de una empresa por meses y devuelva un diagrama de líneas con dos líneas, la
# primera para los ingresos, y la segunda para los gastos. El diagrama debe tener una
# leyenda identificando la línea de los ingresos y la de los gastos, un título con el
# nombre “Evolución de Ingresos y Gastos” y el eje Y debe empezar en 0.

import matplotlib.pyplot as plt
import pandas as pd

def ejercicio_07(df):
    print(f"\n--- Ejercicio 07: Evolución de Ingresos y Gastos ---")
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Ingresos'], label='Ingresos', color='blue', marker='o')
    plt.plot(df.index, df['Gastos'], label='Gastos', color='red', marker='x')
    plt.title('Evolución de Ingresos y Gastos')
    plt.xlabel('Mes')
    plt.ylabel('Cantidad')
    plt.ylim(bottom=0)
    plt.legend()
    plt.grid(True)
    plt.show()

datos = {
    'Ingresos': [1000, 1500, 1400, 1800, 2000],
    'Gastos': [800, 900, 1200, 1100, 1050]
}
df_finanzas = pd.DataFrame(datos, index=['Ene', 'Feb', 'Mar', 'Abr', 'May'])
ejercicio_07(df_finanzas)
