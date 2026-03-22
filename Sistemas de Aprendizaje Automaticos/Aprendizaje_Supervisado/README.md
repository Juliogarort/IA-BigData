# 🔢 Clasificador de Dígitos — Machine Learning

Aplicación web para clasificar dígitos escritos a mano (0-9) utilizando Machine Learning.

## Autor

**Julio García**

---

## Descripción del Proyecto

Este proyecto implementa un clasificador de dígitos manuscritos utilizando el algoritmo de **Regresión Logística** de scikit-learn. El modelo se entrena con el dataset **digits** integrado en scikit-learn, que contiene **1.797 imágenes** de dígitos de **8×8 píxeles** en escala de grises.

La aplicación ofrece una **interfaz web interactiva** donde el usuario puede dibujar un número en un canvas con el ratón o pantalla táctil, y obtener la predicción del modelo en tiempo real junto con el porcentaje de confianza.

### ¿Cómo funciona internamente?

1. El usuario dibuja un número en un canvas de 280×280 píxeles (trazos blancos sobre fondo negro)
2. Al pulsar "Predecir", la imagen se envía al servidor como datos en formato base64
3. El servidor redimensiona la imagen a 8×8 píxeles, invierte los colores y escala los valores a 0-16 (formato del dataset)
4. El modelo de Regresión Logística clasifica la imagen y devuelve la predicción junto con las probabilidades de cada clase
5. El resultado aparece en pantalla con el número detectado y el porcentaje de confianza

---

## Tecnologías Utilizadas

| Tecnología | Versión | Uso |
|---|---|---|
| **Python** | 3.11 | Lenguaje principal del backend |
| **Flask** | 3.1.0 | Servidor web y API REST |
| **scikit-learn** | 1.6.1 | Entrenamiento y predicción del modelo de ML |
| **NumPy** | 2.2.3 | Manejo de arrays numéricos |
| **Pillow** | 11.1.0 | Procesamiento y redimensionado de imágenes |
| **Docker** | — | Contenerización de la aplicación |
| **HTML/CSS/JS** | — | Interfaz web con canvas interactivo |

---

## Estructura del Proyecto

```
digit-classifier/
├── train.py            # Script de entrenamiento del modelo
├── app.py              # Servidor Flask (API + web)
├── model.pkl           # Modelo entrenado (generado por train.py)
├── requirements.txt    # Dependencias de Python
├── Dockerfile          # Configuración para contenerización con Docker
├── README.md           # Documentación del proyecto
├── static/
│   └── style.css       # Estilos CSS de la interfaz web
└── templates/
    └── index.html      # Página web con canvas para dibujar
```

### Descripción detallada de cada archivo

#### `train.py` — Script de entrenamiento
- Carga el dataset **digits** de scikit-learn (1.797 imágenes de 8×8 píxeles)
- Divide los datos en **80% entrenamiento** y **20% test** con split estratificado (`stratify=y`) para mantener la proporción de cada clase
- Entrena un modelo de **Regresión Logística** con el solver `lbfgs` y un máximo de 10.000 iteraciones
- Evalúa el modelo mostrando la precisión y el informe de clasificación por consola
- Guarda el modelo entrenado y su precisión en el archivo `model.pkl` usando `pickle`

#### `app.py` — Servidor Flask
- Al iniciarse, carga el modelo desde `model.pkl`
- **Ruta `/`**: Sirve la página principal (`index.html`) pasándole la precisión del modelo
- **Ruta `/predict` (POST)**: Recibe una imagen en base64 del canvas, la procesa (convierte a escala de grises, redimensiona a 8×8, invierte y escala los valores) y devuelve la predicción en formato JSON con el número detectado, la confianza y las probabilidades de cada clase
- Se ejecuta en el puerto **5000**

#### `model.pkl` — Modelo entrenado
- Archivo binario generado por `train.py` que contiene un diccionario con el modelo de Regresión Logística ya entrenado y su precisión
- Se carga al iniciar `app.py` para poder hacer predicciones sin necesidad de reentrenar

#### `templates/index.html` — Interfaz web
- Página HTML con un **canvas** de 280×280 píxeles para dibujar dígitos
- Soporta dibujo con **ratón** y con **pantalla táctil**
- Botón "Predecir" que envía la imagen al servidor mediante `fetch` (API REST)
- Botón "Borrar" que limpia el canvas
- Muestra el resultado con el número predicho y el porcentaje de confianza

#### `static/style.css` — Estilos CSS
- Diseño moderno con **glassmorphism** (fondo translúcido con desenfoque)
- Gradiente de fondo oscuro y colores violeta/azul
- Diseño **responsive** adaptado a distintos tamaños de pantalla
- Animaciones y transiciones suaves en botones

#### `requirements.txt` — Dependencias
- Lista las librerías de Python necesarias con sus versiones exactas

#### `Dockerfile` — Contenerización
- Usa la imagen base `python:3.11-slim` (ligera)
- Instala las dependencias, entrena el modelo durante el build y ejecuta el servidor Flask

---

## Datos del Modelo

| Parámetro | Valor |
|---|---|
| **Dataset** | digits de scikit-learn |
| **Muestras** | 1.797 imágenes (8×8 píxeles, escala de grises) |
| **Clases** | 10 (dígitos del 0 al 9) |
| **Algoritmo** | Regresión Logística (`LogisticRegression`) |
| **Solver** | `lbfgs` |
| **Iteraciones máximas** | 10.000 |
| **Split** | 80% entrenamiento / 20% test (estratificado) |
| **Precisión esperada** | ~97% |

---

## Lanzar el Proyecto desde Cero

### Opción 1 — Sin Docker (ejecución local)

#### Requisitos previos
- Tener **Python 3.11** instalado
- Tener **pip** disponible

#### Paso 1: Instalar las dependencias

```bash
pip install -r requirements.txt
```

#### Paso 2: Entrenar el modelo

```bash
python train.py
```

Esto generará el archivo `model.pkl` con el modelo entrenado. Por consola verás la precisión y el informe de clasificación.

#### Paso 3: Lanzar el servidor

```bash
python app.py
```

#### Paso 4: Abrir la aplicación

Abrir el navegador en: **[http://localhost:5000](http://localhost:5000)**

---

### Opción 2 — Con Docker

#### Requisitos previos
- Tener **Docker** instalado y en ejecución

#### Paso 1: Construir la imagen Docker

```bash
docker build -t digit-classifier .
```

> Durante el build se ejecuta automáticamente `train.py`, que entrena el modelo y genera `model.pkl` dentro de la imagen.

#### Paso 2: Ejecutar el contenedor

```bash
docker run -p 5000:5000 digit-classifier
```

#### Paso 3: Abrir la aplicación

Abrir el navegador en: **[http://localhost:5000](http://localhost:5000)**

---

## Uso de la Aplicación

1. **Dibuja** un número (0-9) con el ratón o el dedo en el canvas negro
2. Pulsa el botón **"Predecir"** para enviar la imagen al modelo
3. Visualiza el **resultado** con el número detectado y el porcentaje de confianza
4. Pulsa **"Borrar"** para limpiar el canvas y probar con otro número

---

## Información Adicional

- El modelo usa **semilla fija** (`random_state=42`) para que los resultados sean reproducibles
- El split de datos es **estratificado**, lo que garantiza que cada clase (0-9) tenga la misma proporción en entrenamiento y test
- El preprocesamiento de la imagen del canvas incluye: conversión a escala de grises, redimensionado a 8×8 con interpolación LANCZOS, inversión de colores y escalado de 0-255 a 0-16
- La API devuelve las probabilidades de todas las clases, lo que permite evaluar la confianza del modelo en cada predicción
