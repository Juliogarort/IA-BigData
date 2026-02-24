# Análisis de correlación con mapa de calor:
# Carga el dataset penguins de Seaborn.
# Convierte todas las variables numéricas a arrays y calcula la matriz
# de correlación.
# Visualiza la correlación usando un mapa de calor con anotaciones
# y personalización de la paleta de colores

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = sns.load_dataset("penguins").dropna()

# Convertir variables numéricas a arrays de NumPy
bill_length    = data["bill_length_mm"].to_numpy()
bill_depth     = data["bill_depth_mm"].to_numpy()
flipper_length = data["flipper_length_mm"].to_numpy()
body_mass      = data["body_mass_g"].to_numpy()

# Calcular la matriz de correlación con NumPy
matriz = np.corrcoef([bill_length, bill_depth, flipper_length, body_mass])
etiquetas = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]

sns.heatmap(matriz, annot=True, fmt=".2f", cmap="coolwarm",
            xticklabels=etiquetas, yticklabels=etiquetas)
plt.title("Mapa de calor de correlación - Penguins")
plt.show()

