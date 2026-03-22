"""
app.py - Servidor Flask para el clasificador de dígitos.
Sirve la web HTML y expone la API de predicción.
Autor: Julio García
"""

import pickle
import numpy as np
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    data    = pickle.load(f)
    model   = data['model']    # pipeline (StandardScaler + LogisticRegression)
    accuracy = data['accuracy']

print(f"Modelo cargado. Precisión: {accuracy * 100:.2f}%")


@app.route('/')
def index():
    return render_template('index.html', accuracy=f"{accuracy * 100:.2f}")


@app.route('/predict', methods=['POST'])
def predict():
    """
    Recibe un array de 64 floats (8x8, escala 0-16) preprocesado en el cliente
    y devuelve la predicción. El pipeline aplica StandardScaler internamente.
    """
    try:
        payload = request.get_json()
        pixels  = payload['pixels']

        if len(pixels) != 64:
            return jsonify({'error': f'Se esperaban 64 píxeles, llegaron {len(pixels)}'}), 400

        X    = np.array(pixels, dtype=np.float32).reshape(1, -1)
        pred = int(model.predict(X)[0])
        probs = model.predict_proba(X)[0]
        conf  = round(float(probs[pred]) * 100, 1)

        return jsonify({'prediction': pred, 'confidence': conf})

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)