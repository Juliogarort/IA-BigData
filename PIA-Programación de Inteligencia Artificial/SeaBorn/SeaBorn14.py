# Plot de violin combinado con stripplot:
# Usa el dataset titanic.
# Convierte la columna de edad y clase a arrays de NumPy.
# Superpone un stripplot sobre un violin plot para observar la distribución
# de edades por clase.


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = sns.load_dataset("titanic").dropna(subset=["age", "class"])

# Convertir columnas a arrays de NumPy
age    = data["age"].to_numpy()
pclass = data["class"].to_numpy()

sns.violinplot(data=data, x="class", y="age",
               order=["First", "Second", "Third"],
               palette="pastel", inner=None, linewidth=1.5)
sns.stripplot(data=data, x="class", y="age",
              order=["First", "Second", "Third"],
              color="black", alpha=0.3, size=3, jitter=True)
plt.title("Distribución de edades por clase - Titanic (Violin + Strip)")
plt.xlabel("Clase")
plt.ylabel("Edad")
plt.show()

