import pickle
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


def main():
    # 1. Cargar el dataset digits (imágenes 8x8, valores 0-16)
    digits = load_digits()
    X = digits.data    
    y = digits.target  

    print(f"Dataset: {X.shape[0]} muestras | rango valores: {X.min():.0f} - {X.max():.0f}")

    # 2. Split estratificado 80/20
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"Train: {X_train.shape[0]} muestras | Test: {X_test.shape[0]} muestras")

    # 3. Entrenar Regresión Logística directamente sobre los valores 0-16

    model = LogisticRegression(solver='lbfgs', max_iter=10000, random_state=42)
    model.fit(X_train, y_train)

    # 4. Evaluar
    y_pred   = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nPrecisión: {accuracy * 100:.2f}%")
    print(classification_report(y_test, y_pred))

    # 5. Guardar modelo
    with open('model.pkl', 'wb') as f:
        pickle.dump({'model': model, 'accuracy': accuracy}, f)

    print("Modelo guardado en model.pkl")


if __name__ == '__main__':
    main()