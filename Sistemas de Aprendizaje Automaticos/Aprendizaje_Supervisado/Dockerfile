# Usa imagen base ligera de Python
FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar dependencias e instalarlas primero (cache de Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Entrenar el modelo durante el build
RUN python train.py

# Exponer el puerto 5000
EXPOSE 5000

# Ejecutar el servidor Flask
CMD ["python", "app.py"]
