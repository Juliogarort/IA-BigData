# =============================================================
# Ejercicio 4: Traducción Automática
# Librería: googletrans
# =============================================================

from googletrans import Translator

# Texto de prueba
texto = "El aprendizaje profundo está revolucionando el procesamiento del lenguaje natural."

# Crear traductor
traductor = Translator()

# ----- Traducción español -> inglés -----
print("=" * 60)
print("TRADUCCIÓN AUTOMÁTICA")
print("=" * 60)

print(f"\nTexto original (ES): \"{texto}\"")

try:
    resultado = traductor.translate(texto, src='es', dest='en')
    print(f"Traducción   (EN): \"{resultado.text}\"")
    print(f"\nIdioma detectado: {resultado.src}")
    print(f"Idioma destino:   {resultado.dest}")
except Exception as e:
    print(f"\nError en la traducción: {e}")
    print("Nota: googletrans depende de la API de Google Translate y puede fallar.")

# ----- Traducciones adicionales a otros idiomas -----
print("\n" + "=" * 60)
print("TRADUCCIONES A OTROS IDIOMAS")
print("=" * 60)

idiomas = {'fr': 'Francés', 'de': 'Alemán', 'it': 'Italiano', 'pt': 'Portugués'}

for codigo, nombre in idiomas.items():
    try:
        res = traductor.translate(texto, src='es', dest=codigo)
        print(f"\n{nombre} ({codigo}): \"{res.text}\"")
    except Exception as e:
        print(f"\n{nombre} ({codigo}): Error - {e}")

print("\n¡Traducción completada!")
