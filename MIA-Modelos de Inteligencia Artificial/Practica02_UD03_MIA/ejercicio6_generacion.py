# =============================================================
# Ejercicio 6: Generación de Texto con GPT-2
# Librería: transformers (Hugging Face)
# =============================================================

from transformers import pipeline

# Texto de entrada
entrada = "La inteligencia artificial está transformando el mundo porque"

print("=" * 60)
print("GENERACIÓN DE TEXTO CON GPT-2")
print("=" * 60)
print(f"\nTexto de entrada: \"{entrada}\"")
print("\nCargando modelo GPT-2 (puede tardar la primera vez)...")

# Crear pipeline de generación de texto con GPT-2
generador = pipeline("text-generation", model="gpt2")

# Generar texto
resultados = generador(
    entrada,
    max_length=100,        # Longitud máxima del texto generado
    num_return_sequences=3, # Generar 3 variaciones
    temperature=0.8,        # Controla la creatividad (más alto = más creativo)
    top_p=0.9,              # Nucleus sampling
    do_sample=True          # Activar muestreo para variedad
)

# Mostrar resultados
print("\n" + "=" * 60)
print("TEXTOS GENERADOS")
print("=" * 60)

for i, resultado in enumerate(resultados, 1):
    print(f"\n--- Variación {i} ---")
    print(resultado['generated_text'])

print("\n¡Generación de texto completada!")
