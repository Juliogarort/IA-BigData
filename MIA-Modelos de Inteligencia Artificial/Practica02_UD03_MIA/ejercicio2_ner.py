# =============================================================
# Ejercicio 2: Reconocimiento de Entidades Nombradas (NER)
# Librería: spaCy
# =============================================================

import spacy

# Texto de prueba
texto = "El fundador de Tesla, Elon Musk, ha invertido en inteligencia artificial."

# Cargar modelo en español
nlp = spacy.load("es_core_news_sm")
doc = nlp(texto)

# ----- Mostrar entidades encontradas -----
print("=" * 60)
print("RECONOCIMIENTO DE ENTIDADES NOMBRADAS (NER)")
print("=" * 60)
print(f"\nTexto: \"{texto}\"\n")

if doc.ents:
    print(f"{'Entidad':<20} {'Etiqueta':<10} {'Descripción':<30}")
    print("-" * 60)
    for ent in doc.ents:
        print(f"{ent.text:<20} {ent.label_:<10} {spacy.explain(ent.label_):<30}")
else:
    print("No se encontraron entidades en el texto.")

# ----- Mostrar el contexto de cada entidad -----
print("\n" + "=" * 60)
print("CONTEXTO DE LAS ENTIDADES")
print("=" * 60)
for ent in doc.ents:
    print(f"\n- '{ent.text}' es una entidad de tipo {ent.label_} ({spacy.explain(ent.label_)})")
    print(f"  Posición en el texto: caracteres {ent.start_char} a {ent.end_char}")

print("\n¡Análisis NER completado!")
