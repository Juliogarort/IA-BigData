# =============================================================
# Ejercicio 1: Tokenización y Análisis Morfológico
# Librerías: nltk, spaCy
# =============================================================

import nltk
import spacy

# Texto de prueba
texto = "El procesamiento del lenguaje natural es una rama de la inteligencia artificial."

# ----- PARTE 1: Tokenización con NLTK -----
print("=" * 60)
print("TOKENIZACIÓN CON NLTK")
print("=" * 60)

# Tokenización por palabras
tokens_palabras = nltk.word_tokenize(texto, language='spanish')
print(f"\nTokens (palabras): {tokens_palabras}")
print(f"Número de tokens: {len(tokens_palabras)}")

# Tokenización por oraciones
tokens_oraciones = nltk.sent_tokenize(texto, language='spanish')
print(f"\nTokens (oraciones): {tokens_oraciones}")
print(f"Número de oraciones: {len(tokens_oraciones)}")

# ----- PARTE 2: Análisis Morfológico con spaCy -----
print("\n" + "=" * 60)
print("ANÁLISIS MORFOLÓGICO CON spaCy")
print("=" * 60)

# Cargar modelo en español
nlp = spacy.load("es_core_news_sm")
doc = nlp(texto)

# Mostrar análisis de cada palabra
print(f"\n{'Palabra':<20} {'Lema':<20} {'POS':<10} {'Categoría':<15}")
print("-" * 65)
for token in doc:
    print(f"{token.text:<20} {token.lemma_:<20} {token.pos_:<10} {spacy.explain(token.pos_):<15}")

print("\n¡Análisis completado!")
