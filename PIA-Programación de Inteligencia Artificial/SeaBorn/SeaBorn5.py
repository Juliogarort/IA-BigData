# Violin plot con categorización de datos:
# Utiliza el dataset iris.
# Convierte la columna de longitud del sépalo y la especie a arrays
# de NumPy.
# Genera un violin plot para analizar la distribución de la longitud del
# sépalo por cada especie.
# Ajusta la división interna y muestra puntos individuales.

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = sns.load_dataset("iris")

# Convertir columnas a arrays de NumPy
sepal_length = data["sepal_length"].to_numpy()
species      = data["species"].to_numpy()

sns.violinplot(data=data, x="species", y="sepal_length",
               inner="quart", palette="pastel")
sns.stripplot(data=data, x="species", y="sepal_length",
              color="black", alpha=0.4, size=3, jitter=True)
plt.title("Distribución de longitud del sépalo por especie (Violinplot)")
plt.xlabel("Especie")
plt.ylabel("Longitud del sépalo (cm)")
plt.show()

