# Regresión lineal múltiple con visualización avanzada:
# Usa el dataset mpg.
# Convierte las columnas de potencia (horsepower) y peso (weight) a
# arrays.
# Genera un gráfico de regresión múltiple mostrando la relación entre
# peso y potencia con diferentes niveles de confianza.


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = sns.load_dataset("mpg").dropna(subset=["horsepower", "weight"])

# Convertir columnas a arrays de NumPy
horsepower = data["horsepower"].to_numpy()
weight     = data["weight"].to_numpy()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Regresión con intervalo de confianza del 95%
sns.regplot(data=data, x="weight", y="horsepower",
            scatter_kws={"alpha": 0.4, "color": "steelblue"},
            line_kws={"color": "red"}, ci=95, ax=axes[0])
axes[0].set_title("Regresión peso vs potencia (IC 95%)")
axes[0].set_xlabel("Peso (lbs)")
axes[0].set_ylabel("Potencia (hp)")

# Regresión con intervalo de confianza del 68%
sns.regplot(data=data, x="weight", y="horsepower",
            scatter_kws={"alpha": 0.4, "color": "coral"},
            line_kws={"color": "darkred"}, ci=68, ax=axes[1])
axes[1].set_title("Regresión peso vs potencia (IC 68%)")
axes[1].set_xlabel("Peso (lbs)")
axes[1].set_ylabel("Potencia (hp)")

plt.suptitle("Regresión lineal - Dataset MPG")
plt.tight_layout()
plt.show()

