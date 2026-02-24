# Boxplot multivariado con ajuste de estilo:
# Trabaja con el dataset diamonds.
# Convierte las columnas carat, price y depth a arrays de NumPy.
# Crea un gráfico de caja para analizar la distribución de precios en
# diferentes rangos de quilates, segmentado por el tipo de corte.
# Personaliza el gráfico con diferentes estilos de borde y paletas.

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = sns.load_dataset("diamonds")

# Convertir columnas a arrays de NumPy
carat = data["carat"].to_numpy()
price = data["price"].to_numpy()
depth = data["depth"].to_numpy()

# Crear rangos de quilates para categorizar
data["carat_rango"] = pd.cut(data["carat"],
                             bins=[0, 0.5, 1.0, 1.5, 2.0, 5.0],
                             labels=["0-0.5", "0.5-1", "1-1.5", "1.5-2", "2+"])

sns.boxplot(data=data, x="carat_rango", y="price", hue="cut",
            palette="Set2", linewidth=1.2)
plt.title("Distribución de precios por rango de quilates y corte")
plt.xlabel("Rango de quilates")
plt.ylabel("Precio ($)")
plt.legend(title="Tipo de corte", bbox_to_anchor=(1.01, 1), loc="upper left")
plt.tight_layout()
plt.show()

