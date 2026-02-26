# =============================================================
# Analizador de Sentimiento - Enfoque Basado en Modelos
# Librería principal: pysentimiento (Hugging Face Transformers)
# =============================================================
# Este módulo usa modelos preentrenados en español para detectar
# polaridad y emociones con comprensión contextual profunda.
# =============================================================

import warnings

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"


class AnalizadorModelo:
    """
    Analizador de sentimiento basado en modelos preentrenados.
    Usa pysentimiento para analizar polaridad y emociones
    en texto en español con comprensión contextual.
    """

    def __init__(self):
        """
        Inicializa los modelos de sentimiento y emociones.
        La primera ejecución descargará los modelos (~500MB).
        """
        from pysentimiento import create_analyzer

        print("    Cargando modelo de sentimiento...")
        self.analizador_sentimiento = create_analyzer(task="sentiment", lang="es")
        print("    Cargando modelo de emociones...")
        self.analizador_emociones = create_analyzer(task="emotion", lang="es")
        print("    ✓ Modelos cargados correctamente")

    def analizar(self, texto):
        """
        Analiza el sentimiento y las emociones de un texto
        usando modelos preentrenados.

        Args:
            texto (str): Texto en español a analizar.

        Returns:
            dict: Resultado con polaridad, score, emociones
                  y probabilidades detalladas.
        """
        explicaciones = []

        # --- Análisis de sentimiento (polaridad) ---
        resultado_sent = self.analizador_sentimiento.predict(texto)
        etiqueta_sent = resultado_sent.output  # POS, NEG, NEU
        probas_sent = resultado_sent.probas  # {'POS': 0.8, 'NEG': 0.1, 'NEU': 0.1}

        # Convertir a formato estándar
        mapa_polaridad = {"POS": "positive", "NEG": "negative", "NEU": "neutral"}
        polaridad = mapa_polaridad.get(etiqueta_sent, "neutral")

        # Calcular score continuo: P(pos) - P(neg)
        score = probas_sent.get("POS", 0) - probas_sent.get("NEG", 0)

        explicaciones.append(
            f"🤖 Modelo de sentimiento: {polaridad} "
            f"(POS={probas_sent.get('POS', 0):.3f}, "
            f"NEG={probas_sent.get('NEG', 0):.3f}, "
            f"NEU={probas_sent.get('NEU', 0):.3f})"
        )

        # --- Análisis de emociones ---
        resultado_emo = self.analizador_emociones.predict(texto)
        etiqueta_emo = resultado_emo.output
        probas_emo = resultado_emo.probas

        # Mapear nombres de emociones al español
        mapa_emociones = {
            "joy": "alegria",
            "sadness": "tristeza",
            "anger": "ira",
            "fear": "miedo",
            "surprise": "sorpresa",
            "disgust": "asco",
            "others": "otros",
        }

        emociones = {}
        for emo_en, prob in probas_emo.items():
            emo_es = mapa_emociones.get(emo_en, emo_en)
            emociones[emo_es] = round(prob, 4)

        # Emoción dominante
        emocion_dominante = mapa_emociones.get(etiqueta_emo, etiqueta_emo)
        explicaciones.append(
            f"🤖 Emoción dominante: {emocion_dominante} "
            f"({probas_emo.get(etiqueta_emo, 0):.3f})"
        )

        return {
            "polaridad": polaridad,
            "score": round(score, 4),
            "emociones": emociones,
            "emocion_dominante": emocion_dominante,
            "probabilidades_sentimiento": {
                k: round(v, 4) for k, v in probas_sent.items()
            },
            "explicaciones": explicaciones,
        }


# =============================================================
# FUNCIÓN DE CONVENIENCIA
# =============================================================


def analizar_modelo(texto):
    """
    Función de conveniencia para analizar un texto sin
    instanciar la clase manualmente.

    Args:
        texto (str): Texto en español a analizar.

    Returns:
        dict: Resultado del análisis basado en modelos.
    """
    analizador = AnalizadorModelo()
    return analizador.analizar(texto)


# =============================================================
# PRUEBA RÁPIDA (solo si se ejecuta directamente)
# =============================================================

if __name__ == "__main__":
    import json

    textos_prueba = [
        "Me encanta este producto, es maravilloso",
        "No me gusta nada, es horrible",
        "Sí, claro... 'excelente' servicio 😒",
        "Me gustó un poco la película",
        "Estoy muy contento con el resultado!!!",
    ]

    print("=" * 60)
    print("ANALIZADOR BASADO EN MODELOS (pysentimiento)")
    print("=" * 60)

    analizador = AnalizadorModelo()
    for texto in textos_prueba:
        print(f"\n{'='*60}")
        print(f'Texto: "{texto}"')
        resultado = analizador.analizar(texto)
        print(json.dumps(resultado, ensure_ascii=False, indent=2))
