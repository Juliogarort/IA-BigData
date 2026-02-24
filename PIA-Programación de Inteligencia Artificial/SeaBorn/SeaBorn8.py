# Pairplot para el análisis multivariado:
# Usa el dataset iris.
# Convierte todas las columnas numéricas a arrays.
# Genera un pairplot con diferentes tipos de gráficos en la diagonal y
# fuera de la diagonal.
# Cambia los estilos y agrega una regresión lineal a las relaciones.

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = sns.load_dataset("iris")

# Convertir columnas numéricas a arrays de NumPy
sepal_length = data["sepal_length"].to_numpy()
sepal_width  = data["sepal_width"].to_numpy()
petal_length = data["petal_length"].to_numpy()
petal_width  = data["petal_width"].to_numpy()

sns.pairplot(data, hue="species", diag_kind="kde",
             plot_kws={"alpha": 0.5},
             diag_kws={"fill": True})
plt.suptitle("Pairplot multivariado con KDE diagonal - Iris", y=1.02)
plt.show()

