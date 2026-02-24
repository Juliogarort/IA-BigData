# Catplot para variables categóricas con ajuste de orden:
# Usa el dataset exercise.
# Convierte la columna de duración y tipo de ejercicio a arrays.
# Crea un catplot de tipo stripplot para observar la dispersión de
# duración en diferentes tipos de ejercicio.
# Ajusta el orden de categorías y el ancho de puntos.


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = sns.load_dataset("exercise")

# Convertir columnas a arrays de NumPy
pulse = data["pulse"].to_numpy()
kind  = data["kind"].to_numpy()

sns.catplot(data=data, x="kind", y="pulse", kind="strip",
            order=["rest", "walking", "running"],
            hue="diet", palette="Set2",
            jitter=0.25, alpha=0.7, dodge=True, height=5, aspect=1.2)
plt.title("Dispersión del pulso por tipo de ejercicio (Stripplot)")
plt.show()

