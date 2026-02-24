# Swarmplot con ajuste de jitter:
# Usa el dataset penguins.
# Convierte el tamaño de las aletas y el peso corporal a arrays de
# NumPy.
# Genera un swarmplot mostrando la relación entre estos valores,
# ajustando el parámetro dodge.


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = sns.load_dataset("penguins").dropna()

# Convertir columnas a arrays de NumPy
flipper_length = data["flipper_length_mm"].to_numpy()
body_mass      = data["body_mass_g"].to_numpy()

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Con dodge=True: puntos separados por género dentro de cada especie
sns.swarmplot(data=data, x="species", y="flipper_length_mm",
              hue="sex", dodge=True, palette="Set1", size=4, ax=axes[0])
axes[0].set_title("Longitud de aleta por especie (dodge=True)")
axes[0].set_xlabel("Especie")
axes[0].set_ylabel("Longitud aleta (mm)")

# Con dodge=False: todos los puntos juntos por especie
sns.swarmplot(data=data, x="species", y="body_mass_g",
              hue="sex", dodge=False, palette="Set2", size=4, ax=axes[1])
axes[1].set_title("Peso corporal por especie (dodge=False)")
axes[1].set_xlabel("Especie")
axes[1].set_ylabel("Peso corporal (g)")

plt.suptitle("Swarmplot - Dataset Penguins")
plt.tight_layout()
plt.show()

