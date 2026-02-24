# FacetGrid con múltiples gráficos de distribución:
# Trabaja con el dataset fmri.
# Convierte las columnas de tiempo y respuesta a arrays de NumPy.
# Crea una cuadrícula de gráficos de KDE por sujeto para comparar
# patrones de respuesta.
# Personaliza la disposición de las subparcelas.

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = sns.load_dataset("fmri")

# Convertir columnas a arrays de NumPy
timepoint = data["timepoint"].to_numpy()
signal    = data["signal"].to_numpy()

g = sns.FacetGrid(data, col="region", row="event", height=3.5, aspect=1.2)
g.map_dataframe(sns.kdeplot, x="signal", fill=True, alpha=0.5, bw_adjust=1.0)
g.map_dataframe(sns.rugplot, x="signal", height=0.08, alpha=0.4, color="gray")
g.set_axis_labels("Señal de respuesta", "Densidad")
g.set_titles(col_template="Región: {col_name}", row_template="Evento: {row_name}")
g.figure.suptitle("FacetGrid: KDE por región y evento - FMRI", y=1.02)
plt.tight_layout()
plt.show()

