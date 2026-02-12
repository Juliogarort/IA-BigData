# Ejercicio 09.
# El fichero “titanic.csv” contiene información sobre los pasajeros del Titanic. Crear
# un dataframe con Pandas y a partir del mismo, generar los siguientes diagramas;
#   1. Diagrama de Sectores con los fallecidos y supervivientes
#   2. Histograma con las edades
#   3. Diagrama de Barras con el número de personas en cada clase
#   4. Diagrama de Barras con el número de personas fallecidas y
#      supervivientes en cada clase.
#   5. Diagrama de Barras con el número de personas fallecidas y
#      supervivientes acumuladas en cada clase.
    
import matplotlib.pyplot as plt
import pandas as pd
import os

def ejercicio_09(csv_path):
    print(f"\n--- Ejercicio 09: Análisis del Titanic ---")
    try:
        df = pd.read_csv(csv_path)
        
        # Configurar subplots
        fig, axs = plt.subplots(2, 3, figsize=(18, 10))
        fig.suptitle('Análisis de Pasajeros del Titanic', fontsize=16)
        
        # 1. Diagrama de Sectores: Fallecidos vs Supervivientes
        survived_counts = df['Survived'].value_counts()
        axs[0, 0].pie(survived_counts, labels=['Fallecidos', 'Supervivientes'], 
                      autopct='%1.1f%%', startangle=90, colors=['red', 'green'])
        axs[0, 0].set_title('Fallecidos vs Supervivientes')
        
        # 2. Histograma de Edades
        axs[0, 1].hist(df['Age'].dropna(), bins=20, color='skyblue', edgecolor='black')
        axs[0, 1].set_title('Distribución de Edades')
        axs[0, 1].set_xlabel('Edad')
        axs[0, 1].set_ylabel('Frecuencia')
        
        # 3. Diagrama de Barras: Personas por Clase
        class_counts = df['Pclass'].value_counts().sort_index()
        axs[0, 2].bar(class_counts.index.astype(str), class_counts.values, color='orange')
        axs[0, 2].set_title('Personas por Clase')
        axs[0, 2].set_xlabel('Clase')
        axs[0, 2].set_ylabel('Cantidad')
        
        # Preparar datos para gráficos por clase y supervivencia
        survived_by_class = pd.crosstab(df['Pclass'], df['Survived'])
        # 0: Fallecidos, 1: Supervivientes
        
        # 4. Diagrama de Barras: Fallecidos y Supervivientes por Clase
        survived_by_class.plot(kind='bar', ax=axs[1, 0], color=['red', 'green'])
        axs[1, 0].set_title('Supervivencia por Clase')
        axs[1, 0].set_xlabel('Clase')
        axs[1, 0].set_ylabel('Cantidad')
        axs[1, 0].legend(['Fallecidos', 'Supervivientes'])
        
        # 5. Diagrama de Barras Acumuladas: Fallecidos y Supervivientes por Clase
        survived_by_class.plot(kind='bar', stacked=True, ax=axs[1, 1], color=['red', 'green'])
        axs[1, 1].set_title('Supervivencia Acumulada por Clase')
        axs[1, 1].set_xlabel('Clase')
        axs[1, 1].set_ylabel('Cantidad')
        axs[1, 1].legend(['Fallecidos', 'Supervivientes'])
        
        # Ocultar el último subplot vacío si sobra
        axs[1, 2].axis('off')
        
        plt.tight_layout()
        plt.subplots_adjust(top=0.9)
        plt.show()
        
    except FileNotFoundError:
        print(f"Error: El fichero {csv_path} no se encuentra.")

# Obtener la ruta del directorio actual donde se encuentra el script
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta completa al archivo CSV
ruta_titanic = os.path.join(directorio_actual, 'titanic.csv')

# Ejecutar el ejercicio
ejercicio_09(ruta_titanic)
