import pickle
import numpy as np
from flask import Flask, render_template, request, jsonify
from PIL import Image
import base64
import io

app = Flask(__name__)

# Cargar el modelo entrenado al iniciar
with open('model.pkl', 'rb') as f:
    data = pickle.load(f)
    model = data['model']
    accuracy = data['accuracy']

print(f"Modelo cargado. Precisión: {accuracy:.4f}")


@app.route('/')
def index():
    """Sirve la página principal con el canvas para dibujar."""
    return render_template('index.html', accuracy=f"{accuracy * 100:.2f}")


@app.route('/predict', methods=['POST'])
def predict():
    """Recibe una imagen base64 del canvas y devuelve la predicción."""
    try:
        # Obtener la imagen en base64 del request
        data = request.get_json()
        image_data = data['image']

        # Decodificar la imagen base64
        # El formato viene como: "data:image/png;base64,..."
        image_data = image_data.split(',')[1]
        image_bytes = base64.b64decode(image_data)

        # Abrir la imagen con Pillow
        image = Image.open(io.BytesIO(image_bytes))

        # Convertir a escala de grises
        image = image.convert('L')

        # Redimensionar a 8x8 píxeles (formato del dataset digits)
        image = image.resize((8, 8), Image.LANCZOS)

        # Convertir a array numpy
        img_array = np.array(image)

        # El dataset digits usa valores de 0-16 con fondo blanco (0) y trazo oscuro (16)
        # El canvas envía fondo negro (0) y trazo blanco (255)
        # Invertimos y escalamos: 0-255 -> 0-16
        img_array = (255 - img_array) / 255.0 * 16.0

        # Aplanar a un vector de 64 características
        img_flat = img_array.flatten().reshape(1, -1)

        # Realizar la predicción
        prediction = model.predict(img_flat)
        probabilities = model.predict_proba(img_flat)

        result = {
            'prediction': int(prediction[0]),
            'confidence': f"{float(probabilities[0][prediction[0]]) * 100:.1f}%",
            'probabilities': {str(i): round(float(p) * 100, 1) for i, p in enumerate(probabilities[0])}
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
