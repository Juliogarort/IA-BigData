# ============================================================
#           Julio García Ortiz
# ============================================================

import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn import tree
import matplotlib.pyplot as plt


directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_csv = os.path.join(directorio_actual, "clientes_marketing.csv")
df = pd.read_csv(ruta_csv)

print("=" * 60)
print("ARBOL DE DECISION - PREDICCION DE COMPRA EN E-COMMERCE")
print("=" * 60)
print(f"\nDataset cargado correctamente. Registros: {len(df)}")
print(f"Columnas: {list(df.columns)}\n")
print(df.head(10))


print("\n" + "=" * 60)
print("EXPLORACION DE DATOS")
print("=" * 60)
print("\nEstadisticas generales del dataset:")
print(df.describe())
print(f"\nDistribucion de la variable objetivo (Compra):")
print(df["Compra"].value_counts())


# Eliminar Cliente_ID (identificador, no aporta valor predictivo)
df = df.drop("Cliente_ID", axis=1)

# Convertir la variable objetivo de texto (Si/No) a numerico (1/0)
df["Compra"] = df["Compra"].map({"Si": 1, "No": 0})

print("\nDatos tras preprocesamiento:")
print(df.head())


X = df.drop("Compra", axis=1)
y = df["Compra"]

print(f"\nVariables predictoras: {list(X.columns)}")
print(f"Variable objetivo: Compra (0=No compra, 1=Compra)")


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nDatos de entrenamiento: {len(X_train)} registros")
print(f"Datos de prueba: {len(X_test)} registros")


modelo = DecisionTreeClassifier(
    max_depth=4,
    min_samples_split=5,
    min_samples_leaf=3,
    random_state=42
)

modelo.fit(X_train, y_train)
print("\nModelo entrenado correctamente.")


y_pred = modelo.predict(X_test)


print("\n" + "=" * 60)
print("RESULTADOS DEL MODELO")
print("=" * 60)

exactitud = accuracy_score(y_test, y_pred)
print(f"\nExactitud (Accuracy): {exactitud:.4f} ({exactitud * 100:.2f}%)")

print("\nMatriz de Confusion:")
cm = confusion_matrix(y_test, y_pred)
print(cm)
print(f"  - Verdaderos Negativos: {cm[0][0]}")
print(f"  - Falsos Positivos: {cm[0][1]}")
print(f"  - Falsos Negativos: {cm[1][0]}")
print(f"  - Verdaderos Positivos: {cm[1][1]}")

print("\nReporte de Clasificacion:")
print(classification_report(y_test, y_pred, target_names=["No Compra", "Compra"]))


print("\n" + "=" * 60)
print("IMPORTANCIA DE LAS CARACTERISTICAS")
print("=" * 60)

importancias = pd.DataFrame({
    "Caracteristica": X.columns,
    "Importancia": modelo.feature_importances_
}).sort_values(by="Importancia", ascending=False)

print(importancias.to_string(index=False))


print("\n" + "=" * 60)
print("REGLAS DEL ARBOL DE DECISION")
print("=" * 60)
reglas = export_text(modelo, feature_names=list(X.columns))
print(reglas)


plt.figure(figsize=(20, 10))
tree.plot_tree(
    modelo,
    feature_names=list(X.columns),
    class_names=["No Compra", "Compra"],
    filled=True,
    rounded=True,
    fontsize=9
)
plt.title("Arbol de Decision - Prediccion de Compra tras Campana de Marketing", fontsize=14)
plt.tight_layout()
ruta_arbol = os.path.join(directorio_actual, "arbol_decision.png")
plt.savefig(ruta_arbol, dpi=150, bbox_inches='tight')
plt.show()
print(f"\nArbol guardado en: {ruta_arbol}")


plt.figure(figsize=(10, 6))
colores = plt.cm.viridis(np.linspace(0.3, 0.9, len(importancias)))
bars = plt.barh(
    importancias["Caracteristica"],
    importancias["Importancia"],
    color=colores
)
plt.xlabel("Importancia")
plt.ylabel("Caracteristica")
plt.title("Importancia de las Caracteristicas en la Decision de Compra")
plt.gca().invert_yaxis()
for bar, val in zip(bars, importancias["Importancia"]):
    plt.text(bar.get_width() + 0.005, bar.get_y() + bar.get_height() / 2,
             f'{val:.4f}', va='center', fontsize=10)
plt.tight_layout()
ruta_importancia = os.path.join(directorio_actual, "importancia_variables.png")
plt.savefig(ruta_importancia, dpi=150, bbox_inches='tight')
plt.show()
print(f"Grafico de importancia guardado en: {ruta_importancia}")


fig, ax = plt.subplots(figsize=(7, 5))
im = ax.imshow(cm, cmap="Blues")
ax.set_xticks([0, 1])
ax.set_yticks([0, 1])
ax.set_xticklabels(["No Compra", "Compra"])
ax.set_yticklabels(["No Compra", "Compra"])
ax.set_xlabel("Prediccion")
ax.set_ylabel("Valor Real")
ax.set_title("Matriz de Confusion")
for i in range(2):
    for j in range(2):
        ax.text(j, i, str(cm[i][j]), ha="center", va="center",
                fontsize=16, fontweight="bold",
                color="white" if cm[i][j] > cm.max() / 2 else "black")
plt.colorbar(im)
plt.tight_layout()
ruta_confusion = os.path.join(directorio_actual, "matriz_confusion.png")
plt.savefig(ruta_confusion, dpi=150, bbox_inches='tight')
plt.show()
print(f"Matriz de confusion guardada en: {ruta_confusion}")

print("\n" + "=" * 60)
print("ANALISIS COMPLETADO")
print("=" * 60)
