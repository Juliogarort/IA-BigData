# Analisis de Sentimiento en Espanol - Informe de Resultados

**Asignatura:** Modelos de Inteligencia Artificial (MIA) - UD03 PLN  
**Alumno:** Julio Garcia  
**Fecha:** 26/02/2026  

## 1. Descripcion del proyecto

Sistema de analisis de sentimiento en espanol que combina dos enfoques:

- **Analizador lexico (40%):** Basado en reglas linguisticas, diccionario de sentimientos en espanol (~200 palabras), deteccion de negaciones, intensificadores, atenuadores e ironia. Usa spaCy para procesamiento linguistico.
- **Analizador de modelos (60%):** Basado en modelos preentrenados de Hugging Face (pysentimiento). Detecta polaridad (positivo/negativo/neutro) y emociones (alegria, tristeza, ira, miedo, sorpresa, asco).

La **fusion** pondera ambos resultados. Si se detecta ironia, el lexico tiene prioridad (80/20).

## 2. Textos analizados

Se han analizado 12 textos tematicos de Formula 1 que cubren distintos escenarios:

| # | Texto | Tipo esperado |
|---|-------|---------------|
| 1 | Fernando Alonso ha hecho una carrera increible, que pilotazo | Positivo |
| 2 | Carlos Sainz ha ganado el Gran Premio, estoy muy contento | Positivo (intensificador) |
| 3 | Que salida tan brillante de Alonso, ha adelantado a tres coches | Positivo |
| 4 | Que desastre de estrategia del equipo, han arruinado la carrera de Sainz | Negativo |
| 5 | Alonso ha abandonado por un fallo mecanico, estoy furioso | Negativo (intensificador) |
| 6 | No me gusta nada como ha pilotado hoy, ha sido un desastre | Negativo (negacion) |
| 7 | Si, claro... 'fantastica' estrategia del muro, como siempre... | Ironia |
| 8 | Genial, otro abandono por fiabilidad... que sorpresa | Ironia |
| 9 | La proxima carrera del campeonato es en Monza el domingo | Neutro |
| 10 | Alonso ha hecho una gran clasificacion pero la carrera ha sido horrible | Mixto |
| 11 | Estoy super emocionado con el fichaje de Alonso por Aston Martin | Positivo (intensificador) |
| 12 | Me gusto un poco la carrera, fue algo aburrida en general | Atenuador |

## 3. Resultados

### 3.1 Tabla resumen

| # | Polaridad | Score | Intensidad | Ironia | Emocion principal |
|---|-----------|-------|------------|--------|-------------------|
| 1 | POSITIVE | +0.558 | 0.558 | No | alegria (0.91) |
| 2 | POSITIVE | +0.969 | 0.969 | No | alegria (1.00) |
| 3 | POSITIVE | +0.859 | 0.859 | No | alegria (0.71) |
| 4 | NEGATIVE | -0.868 | 0.868 | No | ira (0.90) |
| 5 | NEGATIVE | -0.985 | 0.985 | No | sorpresa (0.79) |
| 6 | NEGATIVE | -0.744 | 0.744 | No | otros (0.75) |
| 7 | MIXED | -0.151 | 0.151 | Si | otros (0.94) |
| 8 | MIXED | -0.191 | 0.831 | No | sorpresa (0.93) |
| 9 | NEUTRAL | +0.019 | 0.019 | No | otros (0.98) |
| 10 | NEGATIVE | -0.911 | 0.911 | No | ira (0.34) / tristeza (0.34) |
| 11 | POSITIVE | +0.938 | 0.938 | No | alegria (0.98) |
| 12 | NEGATIVE | -0.297 | 0.297 | No | otros (0.96) |

### 3.2 Distribucion por polaridad

- **Positivos:** 4 textos (33%)
- **Negativos:** 5 textos (42%)
- **Mixtos:** 2 textos (17%)
- **Neutros:** 1 texto (8%)

### 3.3 Deteccion de ironia

Se ha detectado ironia correctamente en el texto #7 ("Si, claro... 'fantastica' estrategia..."), donde el sistema identifica el patron ironico "si, claro" y las comillas alrededor de una palabra positiva.

El texto #8 ("Genial, otro abandono...") no ha sido detectado como ironia por el sistema lexico, aunque su score es negativo (-0.191) gracias al modelo de IA, lo que lo clasifica correctamente como mixto.

## 4. Analisis de los resultados

### Aciertos del sistema

- **Textos positivos claros (1, 2, 3, 11):** Detectados correctamente con scores altos (+0.55 a +0.97). La emocion dominante es "alegria" en todos los casos.
- **Textos negativos claros (4, 5):** Detectados correctamente con scores negativos altos (-0.87 a -0.99). Las emociones ira y sorpresa dominan.
- **Negacion (texto 6):** El sistema detecta correctamente "No me gusta nada" como negativo (-0.74).
- **Ironia con patron (texto 7):** El sistema detecta el patron ironico y lo clasifica como mixto con ironia.
- **Texto neutro (texto 9):** Correctamente identificado como neutro con score cercano a 0 (+0.019).
- **Texto mixto (texto 10):** Aunque clasificado como negativo, la parte negativa ("horrible") tiene mas peso que la positiva ("gran"), lo cual es razonable.
- **Intensificadores (textos 2, 11):** El intensificador "muy" y "super" amplifican el score positivo correctamente.
- **Atenuador (texto 12):** "Un poco" y "algo" atenuan el sentimiento, resultando en un score bajo (-0.30).

### Limitaciones observadas

- El texto #8 deberia detectarse como ironico pero no lo hace. El patron "que sorpresa" no esta en la lista de frases ironicas y no tiene comillas.
- El texto #12 se clasifica como negativo cuando el sentimiento real es ligeramente positivo ("me gusto un poco"). El atenuador reduce demasiado el score positivo y el modelo le da un sesgo negativo.
- El texto #5 muestra "sorpresa" como emocion dominante cuando deberia ser "ira" (el usuario dice "estoy furioso"). Esto se debe a que el modelo de emociones interpreta "abandonado" y "fallo" como sorpresa.

## 5. Arquitectura del sistema

```
Texto de entrada
    |
    v
+-------------------+     +--------------------+
| Analizador Lexico |     | Analizador Modelo  |
| (spaCy + reglas)  |     | (pysentimiento)    |
| Peso: 40%         |     | Peso: 60%          |
+-------------------+     +--------------------+
    |                           |
    v                           v
+---------------------------------------+
|         Analizador Fusion             |
| - Pondera scores                      |
| - Fusiona emociones                   |
| - Si ironia: lexico 80% / modelo 20% |
+---------------------------------------+
    |
    v
Resultado JSON (polaridad, score, emociones, ironia)
```

## 6. Librerias utilizadas

| Libreria | Uso |
|----------|-----|
| spaCy (es_core_news_sm) | Procesamiento linguistico (tokenizacion, lematizacion, dependencias) |
| pysentimiento | Modelos preentrenados para sentimiento y emociones en espanol |
| transformers (HuggingFace) | Backend de pysentimiento |
| torch | Backend de los modelos de IA |

## 7. Conclusiones

El sistema hibrido combina las ventajas de ambos enfoques:

- El **lexico** aporta explicabilidad y deteccion de ironia, negaciones e intensificadores.
- El **modelo** aporta comprension contextual profunda y deteccion de emociones.
- La **fusion ponderada** produce resultados mas robustos que cualquiera de los dos por separado.

El sistema clasifica correctamente la mayoria de los textos analizados. Las principales areas de mejora son la deteccion de ironia sin patrones explicitos y el balance entre atenuadores y el sesgo del modelo.
