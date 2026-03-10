import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

print("Cargando datos...")

# Cargamos el archivo csv
carpeta = os.path.dirname(os.path.abspath(__file__))
ruta_csv = os.path.join(carpeta, "fraude_data.csv")
df = pd.read_csv(ruta_csv)

print(f"Datos cargados correctamente. Tamaño del dataset: {df.shape}\n")

X = df[["Monto", "Frecuencia_Usuario", "Sospechosa"]]
y = df["Fraude"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

modelo = SVC(kernel="rbf", C=1, gamma="scale", class_weight="balanced", random_state=42)
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

# Matriz de confusión
cm = confusion_matrix(y_test, y_pred)
labels = ["Legítima", "Fraude"]

# Mostrar la matriz de forma más clara
print("Matriz de Confusión:")
print(f"{'':<12}" + "".join(f"{label:>10}" for label in labels))
for i, row in enumerate(cm):
    print(f"{labels[i]:<12}" + "".join(f"{val:>10}" for val in row))

# Visualización opcional
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
disp.plot(cmap="Blues")
plt.title("Matriz de Confusión - SVM Fraude Bancario")
plt.savefig(os.path.join(carpeta, "matriz_confusion.png"))
plt.show()