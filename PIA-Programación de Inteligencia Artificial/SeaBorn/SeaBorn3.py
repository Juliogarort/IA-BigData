# Distribución de datos con KDE Plot y rug plot:
# A partir del dataset tips, convierte las columnas total_bill y tip a
# arrays.
# Genera un gráfico de densidad kernel (KDE) superpuesto con un
# gráfico de rug.
# Ajusta el ancho de banda y experimenta con diferentes estilos de
# visualización.

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = sns.load_dataset("tips")

# Convertir columnas a arrays de NumPy
total_bill = data["total_bill"].to_numpy()
tip        = data["tip"].to_numpy()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# KDE + Rug de total_bill
sns.kdeplot(x=total_bill, fill=True, bw_adjust=0.8, color="steelblue", ax=axes[0])
sns.rugplot(x=total_bill, color="steelblue", ax=axes[0])
axes[0].set_title("KDE + Rug: Cuenta total")
axes[0].set_xlabel("Total bill ($)")

# KDE + Rug de tip
sns.kdeplot(x=tip, fill=True, bw_adjust=1.2, color="coral", ax=axes[1])
sns.rugplot(x=tip, color="coral", ax=axes[1])
axes[1].set_title("KDE + Rug: Propina")
axes[1].set_xlabel("Tip ($)")

plt.suptitle("Distribución con KDE Plot y Rug Plot - Tips")
plt.tight_layout()
plt.show()

