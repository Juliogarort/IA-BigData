# Histogramas superpuestos con diferentes bins:
# Crea un DataFrame con distribuciones normales simuladas,
# conviértelas a arrays.
# Genera histogramas superpuestos de diferentes grupos con ajuste de
# bins.
# Personaliza las transparencias y colores.

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Crear DataFrame con distribuciones normales simuladas
np.random.seed(0)
data = pd.DataFrame({
    "valor":  np.concatenate([
                  np.random.normal(50, 10, 300),
                  np.random.normal(65,  8, 300),
                  np.random.normal(40, 15, 300)
              ]),
    "grupo":  ["Grupo A"] * 300 + ["Grupo B"] * 300 + ["Grupo C"] * 300
})

# Convertir a arrays de NumPy
valores = data["valor"].to_numpy()
grupos  = data["grupo"].to_numpy()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Histograma con bins=20
sns.histplot(data=data, x="valor", hue="grupo", bins=20,
             multiple="layer", alpha=0.5, palette="Set1", ax=axes[0])
axes[0].set_title("Histogramas superpuestos (bins=20)")
axes[0].set_xlabel("Valor")

# Histograma con bins=40
sns.histplot(data=data, x="valor", hue="grupo", bins=40,
             multiple="layer", alpha=0.5, palette="Set2", ax=axes[1])
axes[1].set_title("Histogramas superpuestos (bins=40)")
axes[1].set_xlabel("Valor")

plt.suptitle("Comparación de grupos - Distribuciones normales simuladas")
plt.tight_layout()
plt.show()

