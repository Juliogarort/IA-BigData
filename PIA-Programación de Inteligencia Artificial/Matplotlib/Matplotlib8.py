# Ejercicio 08.
# El fichero “bancos.csv” contiene las cotizaciones de los principales bancos de
# España con los siguientes datos:
#   - Empresa: Nombre de la empresa
#   - Apertura: Precio de la acción a la apertura de la Bolsa
#   - Máximo: Precio máximo de la acción durante la jornada.
#   - Mínimo: Precio mínimo de la acción durante la jornada.
#   - Cierre: Precio de la acción al cierre de la Bolsa
#   - Volumen: Volumen de negocios al cierre de la Bolsa
# Construir una función que reciba el fichero “bancos.csv” y cree un diagrama de
# líneas con las series temporales de las cotizaciones de cierre de cada banco.

import matplotlib.pyplot as plt
import pandas as pd
import os
import matplotlib.dates as mdates

def ejercicio_08(csv_path):
    print(f"\n--- Ejercicio 08: Cotizaciones de Bancos ---")
    try:
        df = pd.read_csv(csv_path)
        df['Fecha'] = pd.to_datetime(df['Fecha'])
        
        empresas = df['Empresa'].unique()
        
        fig, ax = plt.subplots(figsize=(12, 6))
        
        for empresa in empresas:
            datos_empresa = df[df['Empresa'] == empresa]
            ax.plot(datos_empresa['Fecha'], datos_empresa['Cierre'], label=empresa)
        
        # Formatear las fechas en el eje X al formato español (dd/mm/yyyy)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
        
        # Rotar las etiquetas para mejor legibilidad
        plt.xticks(rotation=45, ha='right')
            
        plt.title('Cotización de Cierre por Banco')
        plt.xlabel('Fecha')
        plt.ylabel('Precio de Cierre')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()  # Ajustar el layout para que no se corten las fechas
        plt.show()
    except FileNotFoundError:
        print(f"Error: El fichero {csv_path} no se encuentra.")

# Obtener la ruta del directorio actual donde se encuentra el script
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta completa al archivo CSV
ruta_bancos = os.path.join(directorio_actual, 'bancos.csv')

# Ejecutar el ejercicio
ejercicio_08(ruta_bancos)
