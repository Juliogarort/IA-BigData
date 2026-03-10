# UD03 - Sistemas de Aprendizaje Automatico (SAA)
# Ejercicio: Deteccion de Fraude con SVM
# Alumno:
# Fecha: Marzo 2026

import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
)

# Cargo el CSV desde la misma carpeta que este archivo
carpeta = os.path.dirname(os.path.abspath(__file__))
ruta_csv = os.path.join(carpeta, "fraude_data.csv")
df = pd.read_csv(ruta_csv)

print("Dataset cargado:", df.shape)
print(df.head())

# Separo las caracteristicas (X) y la etiqueta (y)
X = df[["Monto", "Frecuencia_Usuario", "Sospechosa"]]
y = df["Fraude"]

# Divido en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Escalo los datos (importante para que SVM funcione bien)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Creo y entreno el modelo SVM
modelo = SVC(kernel="rbf", C=1, gamma="scale", class_weight="balanced", random_state=42)
modelo.fit(X_train, y_train)

# Predigo sobre los datos de prueba
y_pred = modelo.predict(X_test)

# Muestro los resultados
print("\nInforme de clasificacion:")
print(classification_report(y_test, y_pred, target_names=["Legitima", "Fraude"]))

# Matriz de confusion
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm, display_labels=["Legitima", "Fraude"]
)
disp.plot(cmap="Blues")
plt.title("Matriz de Confusion - SVM Fraude Bancario")
plt.savefig(os.path.join(carpeta, "matriz_confusion.png"))
plt.show()

print("Grafico guardado en la carpeta del proyecto.")
