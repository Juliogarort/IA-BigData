import os
import re
import pyttsx3
from langdetect import detect

# Carpeta del script
directorio = os.path.dirname(os.path.abspath(__file__))

# Buscar archivo TXT
archivos_txt = [f for f in os.listdir(directorio) if f.endswith(".txt")]
if not archivos_txt:
    print("No se encontró ningún archivo .txt")
    exit()

archivo_txt = archivos_txt[0]
ruta_txt = os.path.join(directorio, archivo_txt)

nombre_base = os.path.splitext(archivo_txt)[0]
ruta_mp3 = os.path.join(directorio, nombre_base + ".mp3")

# Leer texto
with open(ruta_txt, "r", encoding="utf-8") as f:
    texto = f.read()

# Preprocesado básico
texto = re.sub(r'\n+', '\n', texto)
texto = re.sub(r' +', ' ', texto)

# Detectar idioma (informativo)
idioma = detect(texto[:1000])
print(f"Idioma detectado: {idioma}")

# Inicializar motor TTS
engine = pyttsx3.init()

# Guardar audio
engine.save_to_file(texto, ruta_mp3)
engine.runAndWait()

print(f"Archivo generado correctamente: {ruta_mp3}")
