# =============================================================
# Ejercicio 3: Análisis de Sentimiento
# Librería: textblob
# =============================================================

from textblob import TextBlob

# Texto de prueba
texto = "Me encanta aprender sobre inteligencia artificial, es fascinante."

# ----- Análisis de sentimiento -----
print("=" * 60)
print("ANÁLISIS DE SENTIMIENTO")
print("=" * 60)
print(f"\nTexto: \"{texto}\"\n")

# Crear objeto TextBlob (usamos traducción al inglés para mejor precisión)
blob = TextBlob(texto)

# Traducir al inglés para analizar con TextBlob (más preciso en inglés)
try:
    blob_en = blob.translate(from_lang='es', to='en')
    print(f"Texto traducido: \"{blob_en}\"\n")
except Exception:
    # Si falla la traducción, usar el texto original
    blob_en = blob
    print("(Análisis sobre texto original)\n")

# Obtener polaridad y subjetividad
polaridad = blob_en.sentiment.polarity
subjetividad = blob_en.sentiment.subjectivity

# Clasificar el sentimiento
if polaridad > 0.1:
    sentimiento = "POSITIVO"
elif polaridad < -0.1:
    sentimiento = "NEGATIVO"
else:
    sentimiento = "NEUTRO"

# Mostrar resultados
print(f"Polaridad:    {polaridad:.4f}  (rango: -1 negativo a +1 positivo)")
print(f"Subjetividad: {subjetividad:.4f}  (rango: 0 objetivo a 1 subjetivo)")
print(f"\nSentimiento:  {sentimiento}")

# ----- Análisis con textos adicionales -----
print("\n" + "=" * 60)
print("ANÁLISIS CON TEXTOS ADICIONALES")
print("=" * 60)

textos_extra = [
    "Este producto es terrible, no funciona.",
    "El día está normal, ni bueno ni malo.",
    "¡Qué maravilla de espectáculo, increíble!"
]

for t in textos_extra:
    blob_t = TextBlob(t)
    pol = blob_t.sentiment.polarity
    if pol > 0.1:
        sent = "POSITIVO"
    elif pol < -0.1:
        sent = "NEGATIVO"
    else:
        sent = "NEUTRO"
    print(f"\n\"{t}\"")
    print(f"  -> Polaridad: {pol:.4f} | Sentimiento: {sent}")

print("\n¡Análisis de sentimiento completado!")
