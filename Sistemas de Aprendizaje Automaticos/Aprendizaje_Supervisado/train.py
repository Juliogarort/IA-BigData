"""
train.py - Script de entrenamiento del clasificador de dígitos.
Usa el dataset digits de scikit-learn y Regresión Logística.
Autor: Julio García
"""

import pickle
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


def main():
    # 1. Cargar el dataset digits de scikit-learn (imágenes 8x8)
    digits = load_digits()
    X = digits.data    # (1797, 64)
    y = digits.target  # (1797,)

    print(f"Dataset cargado: {X.shape[0]} muestras, {X.shape[1]} características")
    print(f"Clases: {list(range(10))}")

    # 2. Split estratificado (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    print(f"Train: {X_train.shape[0]} muestras | Test: {X_test.shape[0]} muestras")

    # 3. Entrenar modelo con Regresión Logística
    model = LogisticRegression(solver='lbfgs', max_iter=10000, random_state=42)
    model.fit(X_train, y_train)

    # 4. Evaluar el modelo
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print("\n--- Resultados ---")
    print(f"Precisión: {accuracy:.4f} ({accuracy * 100:.2f}%)")
    print("\nInforme de Clasificación:\n")
    print(classification_report(y_test, y_pred))

    # 5. Guardar el modelo entrenado en model.pkl
    with open('model.pkl', 'wb') as f:
        pickle.dump({'model': model, 'accuracy': accuracy}, f)

    print("Modelo guardado en model.pkl")


if __name__ == '__main__':
    main()
