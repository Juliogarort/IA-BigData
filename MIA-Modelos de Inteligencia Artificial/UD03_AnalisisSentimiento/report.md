# Analisis de Sentimiento en Espanol - Informe

**Asignatura:** Modelos de Inteligencia Artificial (MIA) - UD03 PLN  
**Alumno:** Julio Garcia  
**Fecha:** 26/02/2026  

## 1. Descripcion

Sistema hibrido de analisis de sentimiento en espanol que combina dos enfoques:

- **Lexico (40%):** Reglas linguisticas con spaCy, diccionario de ~200 palabras, deteccion de negaciones, intensificadores, atenuadores e ironia.
- **Modelo (60%):** Modelos preentrenados de Hugging Face (pysentimiento) para polaridad y emociones.

La fusion pondera ambos resultados. Si se detecta ironia, el lexico tiene prioridad (80/20).

## 2. Modo de uso

El programa es interactivo. Al ejecutar `main.py`:

1. Se cargan los modelos de IA
2. Se muestran ejemplos de frases F1 que ilustran cada tipo de sentimiento
3. El usuario escribe frases por consola y obtiene el analisis al instante
4. Al escribir "salir" se guardan los resultados en `resultados_analisis.json`

## 3. Ejemplos incluidos

| Tipo | Ejemplo |
|------|---------|
| POSITIVO | Fernando Alonso ha hecho una carrera increible, que pilotazo |
| POSITIVO | Carlos Sainz ha ganado el Gran Premio, estoy muy contento |
| NEGATIVO | Que desastre de estrategia, han arruinado la carrera de Sainz |
| NEGATIVO | Alonso ha abandonado por un fallo mecanico, estoy furioso |
| NEGACION | No me gusta nada como ha pilotado hoy, ha sido un desastre |
| IRONIA | Si, claro... 'fantastica' estrategia del muro, como siempre... |
| NEUTRO | La proxima carrera del campeonato es en Monza el domingo |
| MIXTO | Alonso ha hecho una gran clasificacion pero la carrera ha sido horrible |
| INTENSIF. | Estoy super emocionado con el fichaje de Alonso por Aston Martin |
| ATENUADOR | Me gusto un poco la carrera, fue algo aburrida en general |

## 4. Resultados de prueba

Resultados obtenidos al analizar los ejemplos:

| # | Polaridad | Score | Ironia | Emocion principal |
|---|-----------|-------|--------|-------------------|
| 1 | POSITIVE | +0.558 | No | alegria (0.91) |
| 2 | POSITIVE | +0.969 | No | alegria (1.00) |
| 3 | NEGATIVE | -0.868 | No | ira (0.90) |
| 4 | NEGATIVE | -0.985 | No | sorpresa (0.79) |
| 5 | NEGATIVE | -0.744 | No | otros (0.75) |
| 6 | MIXED | -0.151 | Si | otros (0.94) |
| 7 | NEUTRAL | +0.019 | No | otros (0.98) |
| 8 | NEGATIVE | -0.911 | No | ira (0.34) |
| 9 | POSITIVE | +0.938 | No | alegria (0.98) |
| 10 | NEGATIVE | -0.297 | No | otros (0.96) |

### Distribucion

- Positivos: 3 (30%)
- Negativos: 5 (50%)
- Mixtos: 1 (10%)
- Neutros: 1 (10%)

## 5. Arquitectura

```
Texto del usuario (consola)
        |
        v
+------------------+     +------------------+
| Analizador       |     | Analizador       |
| Lexico (spaCy)   |     | Modelo (pysent.) |
| Peso: 40%        |     | Peso: 60%        |
+------------------+     +------------------+
        |                         |
        v                         v
+------------------------------------+
|        Analizador Fusion           |
| Pondera scores, fusiona emociones  |
| Si ironia: lexico 80% / modelo 20% |
+------------------------------------+
        |
        v
  Resultado (polaridad, score, emociones, ironia)
```

## 6. Librerias

| Libreria | Uso |
|----------|-----|
| spaCy (es_core_news_sm) | Procesamiento linguistico |
| pysentimiento | Modelos de sentimiento y emociones |
| transformers | Backend de pysentimiento |
| torch | Backend de los modelos |

## 7. Conclusiones

- El sistema clasifica correctamente textos positivos, negativos y neutros
- Detecta negaciones e invierte correctamente la polaridad
- Los intensificadores y atenuadores modifican la intensidad del sentimiento
- La deteccion de ironia funciona con patrones conocidos (comillas, frases ironicas)
- La fusion ponderada produce resultados mas robustos que cualquier enfoque individual

## 8. Estructura del proyecto

```
UD03_AnalisisSentimiento/
  main.py                  -> Programa principal (interactivo)
  analizador_lexico.py     -> Analisis lexico con spaCy
  analizador_modelo.py     -> Analisis con modelos de IA
  analizador_fusion.py     -> Fusion de ambos enfoques
  resultados_analisis.json -> Resultados guardados
  report.md                -> Este informe
  requirements.txt         -> Dependencias
```
