# Analisis de Sentimiento en Espanol

Proyecto de la asignatura MIA (UD03 - PLN) que analiza el sentimiento de textos en espanol usando un sistema hibrido.

## Como funciona

Combina dos enfoques:

- **Lexico (40%):** Diccionario de palabras con puntuacion + reglas de negacion, intensificadores, atenuadores e ironia (spaCy)
- **Modelo IA (60%):** Modelos preentrenados de Hugging Face para sentimiento y emociones (pysentimiento)

## Uso

```
python main.py
```

El programa muestra ejemplos de frases y luego permite escribir cualquier texto por consola para analizarlo. Escribe `salir` para terminar.

## Instalacion

```
pip install spacy pysentimiento
python -m spacy download es_core_news_sm
```

## Archivos

| Archivo | Descripcion |
|---------|-------------|
| main.py | Programa principal (interactivo) |
| analizador_lexico.py | Analisis basado en reglas y diccionario |
| analizador_modelo.py | Analisis con modelos de IA |
| analizador_fusion.py | Fusion ponderada de ambos enfoques |
| report.md | Informe con resultados |
