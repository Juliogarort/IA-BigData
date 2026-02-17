# =============================================================
# Ejercicio 5: Reconocimiento de Voz
# Librería: SpeechRecognition
# =============================================================

import speech_recognition as sr
import os

# Crear reconocedor
reconocedor = sr.Recognizer()

print("=" * 60)
print("RECONOCIMIENTO DE VOZ")
print("=" * 60)

# ----- OPCIÓN 1: Desde archivo WAV -----
print("\n--- Opción 1: Desde archivo WAV ---")

archivo_wav = "audio_prueba.wav"

if os.path.exists(archivo_wav):
    try:
        with sr.AudioFile(archivo_wav) as fuente:
            audio = reconocedor.record(fuente)
        texto = reconocedor.recognize_google(audio, language="es-ES")
        print(f"Texto reconocido: \"{texto}\"")
    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
    except sr.RequestError as e:
        print(f"Error con el servicio de Google: {e}")
else:
    print(f"No se encontró el archivo '{archivo_wav}'.")
    print("Coloca un archivo WAV en la misma carpeta para probarlo.")

# ----- OPCIÓN 2: Desde micrófono -----
print("\n--- Opción 2: Desde micrófono ---")
print("Se intentará grabar desde el micrófono durante 5 segundos...")

try:
    with sr.Microphone() as fuente:
        print("Ajustando ruido ambiente...")
        reconocedor.adjust_for_ambient_noise(fuente, duration=1)
        print("¡Habla ahora! (5 segundos)")
        audio = reconocedor.listen(fuente, timeout=5, phrase_time_limit=5)

    print("Procesando audio...")
    texto = reconocedor.recognize_google(audio, language="es-ES")
    print(f"\nTexto reconocido: \"{texto}\"")

except sr.WaitTimeoutError:
    print("No se detectó voz en el tiempo establecido.")
except sr.UnknownValueError:
    print("No se pudo entender el audio.")
except sr.RequestError as e:
    print(f"Error con el servicio de Google: {e}")
except OSError as e:
    print(f"No se pudo acceder al micrófono: {e}")
    print("Asegúrate de tener un micrófono conectado.")

print("\n¡Reconocimiento de voz completado!")
