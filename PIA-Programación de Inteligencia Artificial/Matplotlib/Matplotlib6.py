# Ejercicio 06.
# Escribir una función que reciba una serie de Pandas con el número de ventas de un
# producto por años y una cadena con el tipo de gráfico a generar (líneas, barras,
# sectores, áreas) y devuelva un diagrama del tipo indicado con la evolución de las
# ventas por años y con el título “Evolución del Número de Ventas”

import matplotlib.pyplot as plt
import pandas as pd

def ejercicio_06(ventas_s, tipo_grafico):
    print(f"\n--- Ejercicio 06: Gráfico de {tipo_grafico} ---")
    plt.figure(figsize=(10, 6))
    
    if tipo_grafico.lower() == 'lineas':
        plt.plot(ventas_s.index, ventas_s.values, marker='o', linestyle='-', color='blue')
        plt.xlabel('Año')
        plt.ylabel('Número de Ventas')
    elif tipo_grafico.lower() == 'barras':
        plt.bar(ventas_s.index, ventas_s.values, color='green')
        plt.xlabel('Año')
        plt.ylabel('Número de Ventas')
    elif tipo_grafico.lower() == 'sectores':
        plt.pie(ventas_s, labels=ventas_s.index, autopct='%1.1f%%', startangle=90)
    elif tipo_grafico.lower() == 'areas':
        plt.fill_between(ventas_s.index, ventas_s.values, alpha=0.7, color='orange')
        plt.plot(ventas_s.index, ventas_s.values, marker='o', linestyle='-', color='red')
        plt.xlabel('Año')
        plt.ylabel('Número de Ventas')
    else:
        print(f"Tipo de gráfico '{tipo_grafico}' no reconocido.")
        return
    
    plt.title('Evolución del Número de Ventas')
    plt.grid(True if tipo_grafico.lower() != 'sectores' else False)
    plt.show()

# Ejemplo de uso
ventas_anuales = pd.Series([1200, 1500, 1100, 1800, 2000], index=[2020, 2021, 2022, 2023, 2024])
ejercicio_06(ventas_anuales, 'barras')

