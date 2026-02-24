#  Gráfico de dispersión avanzado con estilo personalizado:
#       Utiliza un dataset de automóviles (mpg) de Seaborn.
#       Convierte las columnas horsepower, weight y mpg a arrays de
#       NumPy y crea un gráfico de dispersión donde el tamaño de los
#       puntos represente el peso y el color la eficiencia de combustible.
#       Personaliza con temas y ajustes de tamaño.

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Cargar el dataset
dataset = sns.load_dataset("mpg")

# Convertir columnas a arrays de NumPy
hp = dataset["horsepower"].to_numpy()
wt = dataset["weight"].to_numpy()
mpg = dataset["mpg"].to_numpy()

# Crear el gráfico de dispersión
plt.figure(figsize=(10, 6))
sns.scatterplot(x=hp, y=mpg, size=wt, alpha=0.6, palette="viridis")

# Personalizar el gráfico
plt.title("Relación Potencia - Peso y Consumo de Combustible")
plt.xlabel("Caballitos de fuerza (horsepower)")
plt.ylabel("Millas por Galón (mpg)")
plt.legend(title="Peso")
plt.grid(True, alpha=0.3)

# Mostrar el gráfico
plt.show()
