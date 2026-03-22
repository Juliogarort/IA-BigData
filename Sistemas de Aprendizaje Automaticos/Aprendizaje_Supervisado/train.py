"""
train.py - Script de entrenamiento del clasificador de dígitos.
Usa el dataset digits de scikit-learn y Regresión Logística.
Autor: Julio García
"""

import pickle
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report


def main():
    # 1. Cargar el dataset digits (imágenes 8x8, valores 0-16)
    digits = load_digits()
    X = digits.data    # (1797, 64)
    y = digits.target  # (1797,)

    print(f"Dataset: {X.shape[0]} muestras | rango valores: {X.min():.0f}-{X.max():.0f}")

    # 2. Split estratificado 80/20
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"Train: {X_train.shape[0]} | Test: {X_test.shape[0]}")

    # 3. Pipeline: StandardScaler + Regresión Logística
    #    StandardScaler normaliza cada pixel a media=0, std=1.
    #    Necesario para que el modelo sea robusto frente a diferencias
    #    de intensidad entre el dataset y los dibujos del usuario.
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model',  LogisticRegression(solver='lbfgs', max_iter=10000, random_state=42))
    ])
    pipeline.fit(X_train, y_train)

    # 4. Evaluar
    y_pred   = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nPrecisión: {accuracy * 100:.2f}%")
    print(classification_report(y_test, y_pred))

    # 5. Guardar el pipeline completo (scaler + modelo juntos)
    #    Al guardar el pipeline, la normalización se aplica automáticamente
    #    en cada llamada a predict() sin código extra en app.py
    with open('model.pkl', 'wb') as f:
        pickle.dump({'model': pipeline, 'accuracy': accuracy}, f)

    print("Pipeline guardado en model.pkl")


if __name__ == '__main__':
    main()