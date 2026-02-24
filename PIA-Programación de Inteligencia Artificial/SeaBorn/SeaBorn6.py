# Gráfico de barras con agregación de datos:
# Carga el dataset titanic.
# Convierte la columna de clase (class) y tarifa (fare) a arrays.
# Crea un gráfico de barras que muestre el promedio de tarifas
# pagadas por clase, con desviaciones estándar indicadas.
# Aplica una paleta de color diferenciada por género.

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = sns.load_dataset("titanic").dropna(subset=["fare", "class", "sex"])

# Convertir columnas a arrays de NumPy
fare   = data["fare"].to_numpy()
pclass = data["class"].to_numpy()

sns.barplot(data=data, x="class", y="fare", hue="sex",
            palette={"male": "steelblue", "female": "salmon"},
            capsize=0.08, order=["First", "Second", "Third"])
plt.title("Promedio de tarifas por clase y género - Titanic")
plt.xlabel("Clase")
plt.ylabel("Tarifa promedio ($)")
plt.show()

