import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"


class AnalizadorModelo:

    def __init__(self):
        from pysentimiento import create_analyzer
        self.analizador_sentimiento = create_analyzer(task="sentiment", lang="es")
        self.analizador_emociones = create_analyzer(task="emotion", lang="es")

    def analizar(self, texto):
        resultado_sent = self.analizador_sentimiento.predict(texto)
        etiqueta = resultado_sent.output
        probas_sent = resultado_sent.probas

        mapa_pol = {"POS": "positive", "NEG": "negative", "NEU": "neutral"}
        polaridad = mapa_pol.get(etiqueta, "neutral")
        score = probas_sent.get("POS", 0) - probas_sent.get("NEG", 0)

        explicaciones = [
            f"Modelo sentimiento: {polaridad} "
            f"(POS={probas_sent.get('POS', 0):.3f}, NEG={probas_sent.get('NEG', 0):.3f}, NEU={probas_sent.get('NEU', 0):.3f})"
        ]

        resultado_emo = self.analizador_emociones.predict(texto)
        etiqueta_emo = resultado_emo.output
        probas_emo = resultado_emo.probas

        mapa_emo = {
            "joy": "alegria", "sadness": "tristeza", "anger": "ira",
            "fear": "miedo", "surprise": "sorpresa", "disgust": "asco", "others": "otros",
        }

        emociones = {}
        for emo_en, prob in probas_emo.items():
            emociones[mapa_emo.get(emo_en, emo_en)] = round(prob, 4)

        emocion_dom = mapa_emo.get(etiqueta_emo, etiqueta_emo)
        explicaciones.append(f"Emocion dominante: {emocion_dom} ({probas_emo.get(etiqueta_emo, 0):.3f})")

        return {
            "polaridad": polaridad,
            "score": round(score, 4),
            "emociones": emociones,
            "emocion_dominante": emocion_dom,
            "probabilidades_sentimiento": {k: round(v, 4) for k, v in probas_sent.items()},
            "explicaciones": explicaciones,
        }
