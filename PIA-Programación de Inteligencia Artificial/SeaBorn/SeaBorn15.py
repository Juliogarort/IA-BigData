# Mapa de calor de confusión para clasificación:
# Simula un DataFrame con resultados de clasificación, conviértelo a
# array.
# Crea un mapa de calor con las tasas de falsos positivos y negativos.
# Ajusta la escala de colores y anota la matriz


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Simular resultados de un clasificador de 4 clases
np.random.seed(7)
clases    = ["Clase A", "Clase B", "Clase C", "Clase D"]
y_real    = np.random.choice(clases, size=200, p=[0.3, 0.3, 0.2, 0.2])
y_pred    = y_real.copy()
errores   = np.random.choice(200, size=50, replace=False)
for i in errores:
    y_pred[i] = np.random.choice([c for c in clases if c != y_real[i]])

# Construir la matriz de confusión manualmente con NumPy
n = len(clases)
matriz = np.zeros((n, n), dtype=int)
for real, pred in zip(y_real, y_pred):
    i = clases.index(real)
    j = clases.index(pred)
    matriz[i][j] += 1

# Convertir a array y normalizar por fila
matriz_array = np.array(matriz)
matriz_norm  = matriz_array.astype(float) / matriz_array.sum(axis=1, keepdims=True)

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Valores absolutos
sns.heatmap(matriz_array, annot=True, fmt="d", cmap="Blues",
            xticklabels=clases, yticklabels=clases, linewidths=0.5, ax=axes[0])
axes[0].set_title("Matriz de confusión (valores absolutos)")
axes[0].set_xlabel("Predicción")
axes[0].set_ylabel("Real")

# Tasas normalizadas
sns.heatmap(matriz_norm, annot=True, fmt=".2f", cmap="RdYlGn",
            vmin=0, vmax=1, xticklabels=clases, yticklabels=clases,
            linewidths=0.5, ax=axes[1])
axes[1].set_title("Matriz de confusión (tasas por clase real)")
axes[1].set_xlabel("Predicción")
axes[1].set_ylabel("Real")

plt.suptitle("Mapa de calor de confusión - Clasificación simulada")
plt.tight_layout()
plt.show()

