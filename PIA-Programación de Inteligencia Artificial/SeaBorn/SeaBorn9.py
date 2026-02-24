# Gráfico de líneas con datos de series temporales:
# Crea un DataFrame simulado con datos de ventas diarias y
# conviértelos a arrays.
# Genera un gráfico de líneas para analizar las tendencias
# estacionales.
# Aplica un suavizado con Seaborn y personaliza las líneas con
# estilos diferenciados.


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Crear DataFrame simulado con ventas diarias de 3 productos
np.random.seed(42)
fechas = pd.date_range(start="2023-01-01", periods=365, freq="D")

ventas_a = 200 + 50 * np.sin(2 * np.pi * np.arange(365) / 365) + np.random.normal(0, 15, 365)
ventas_b = 150 + 30 * np.cos(2 * np.pi * np.arange(365) / 365) + np.random.normal(0, 10, 365)
ventas_c = 100 + 20 * np.sin(4 * np.pi * np.arange(365) / 365) + np.random.normal(0, 8,  365)

data = pd.DataFrame({
    "fecha":    list(fechas) * 3,
    "ventas":   np.concatenate([ventas_a, ventas_b, ventas_c]),
    "producto": ["Producto A"] * 365 + ["Producto B"] * 365 + ["Producto C"] * 365
})

# Convertir a arrays de NumPy
ventas   = data["ventas"].to_numpy()
producto = data["producto"].to_numpy()

# Agrupar por mes para suavizar
data["mes"] = data["fecha"].dt.to_period("M").dt.to_timestamp()

sns.lineplot(data=data, x="mes", y="ventas", hue="producto",
             estimator="mean", errorbar="sd",
             palette=["steelblue", "coral", "mediumseagreen"], linewidth=2)
plt.title("Tendencia de ventas mensuales por producto")
plt.xlabel("Mes")
plt.ylabel("Ventas ($)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

