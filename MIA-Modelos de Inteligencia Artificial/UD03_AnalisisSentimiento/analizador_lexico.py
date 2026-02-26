import spacy
import re

try:
    import emoji
    EMOJI_DISPONIBLE = True
except ImportError:
    EMOJI_DISPONIBLE = False

nlp = spacy.load("es_core_news_sm")

LEXICO_POSITIVO = {
    "bueno": 0.5, "bien": 0.4, "mejor": 0.6, "genial": 0.8,
    "excelente": 0.9, "maravilloso": 0.9, "fantastico": 0.9,
    "increible": 0.8, "estupendo": 0.8, "perfecto": 0.9,
    "magnifico": 0.9, "esplendido": 0.8, "brillante": 0.8,
    "fenomenal": 0.9, "extraordinario": 0.9, "sensacional": 0.9,
    "fabuloso": 0.8, "grandioso": 0.8, "sublime": 0.9,
    "encantador": 0.7, "precioso": 0.7, "hermoso": 0.7,
    "bonito": 0.5, "lindo": 0.5, "bello": 0.6,
    "agradable": 0.5, "placentero": 0.6, "grato": 0.5,
    "gustar": 0.5, "encantar": 0.8, "amar": 0.9,
    "adorar": 0.8, "fascinar": 0.8, "disfrutar": 0.7,
    "divertir": 0.6, "alegrar": 0.7, "emocionar": 0.7,
    "feliz": 0.8, "contento": 0.7, "satisfecho": 0.7,
    "orgulloso": 0.6, "entusiasmado": 0.8, "emocionado": 0.7,
    "ilusionado": 0.7, "esperanzado": 0.6, "optimista": 0.6,
    "util": 0.4, "eficaz": 0.5, "eficiente": 0.5,
    "recomendable": 0.6, "recomendar": 0.6, "aprobar": 0.5,
    "mejorar": 0.4, "avanzar": 0.4, "progresar": 0.4,
    "lograr": 0.5, "conseguir": 0.5, "triunfar": 0.7,
    "exito": 0.7, "victoria": 0.7, "ganar": 0.6,
    "acertar": 0.5, "destacar": 0.6, "sobresalir": 0.7,
    "impresionar": 0.7, "sorprender": 0.5, "asombrar": 0.6,
    "interesante": 0.5, "fascinante": 0.7, "apasionante": 0.7,
    "divertido": 0.6, "entretenido": 0.5, "gracioso": 0.5,
    "especial": 0.5, "unico": 0.5, "excepcional": 0.8,
    "favorito": 0.7, "ideal": 0.7, "justo": 0.4,
    "correcto": 0.3, "adecuado": 0.3, "apropiado": 0.3,
    "rapido": 0.3, "comodo": 0.5, "facil": 0.3,
}

LEXICO_NEGATIVO = {
    "malo": -0.5, "mal": -0.5, "peor": -0.7, "pesimo": -0.9,
    "horrible": -0.9, "terrible": -0.9, "espantoso": -0.9,
    "horroroso": -0.9, "desastroso": -0.8, "catastrofico": -0.9,
    "nefasto": -0.8, "lamentable": -0.7, "deplorable": -0.8,
    "penoso": -0.7, "patetico": -0.7, "miserable": -0.8,
    "asqueroso": -0.9, "repugnante": -0.9, "nauseabundo": -0.8,
    "feo": -0.4, "desagradable": -0.6, "molesto": -0.5,
    "odiar": -0.9, "detestar": -0.8, "aborrecer": -0.8,
    "despreciar": -0.7, "repudiar": -0.7, "rechazar": -0.5,
    "triste": -0.7, "deprimido": -0.8, "desolado": -0.8,
    "abatido": -0.7, "desanimado": -0.6, "devastado": -0.9,
    "decepcionado": -0.6, "frustrado": -0.6, "desilusionado": -0.6,
    "amargado": -0.7, "resentido": -0.6, "dolido": -0.6,
    "sufrir": -0.7, "llorar": -0.6, "lamentar": -0.5,
    "doler": -0.6, "entristecer": -0.7, "angustiar": -0.7,
    "furioso": -0.9, "enfadado": -0.7, "enfurecer": -0.8,
    "irritado": -0.6, "indignado": -0.7, "enojado": -0.6,
    "rabioso": -0.8, "airado": -0.7, "iracundo": -0.8,
    "harto": -0.6, "cansado": -0.3, "agotado": -0.4,
    "miedo": -0.6, "temor": -0.6, "terror": -0.9,
    "panico": -0.8, "horror": -0.8, "pavor": -0.8,
    "asustado": -0.6, "aterrorizado": -0.9, "atemorizado": -0.7,
    "preocupado": -0.4, "ansioso": -0.5, "inquieto": -0.4,
    "nervioso": -0.4, "tenso": -0.4, "estresado": -0.5,
    "inutil": -0.6, "ineficaz": -0.5, "ineficiente": -0.5,
    "fracaso": -0.7, "fallar": -0.6, "fracasar": -0.7,
    "perder": -0.5, "derrota": -0.6, "error": -0.4,
    "problema": -0.4, "defecto": -0.5, "fallo": -0.5,
    "romper": -0.5, "destruir": -0.7, "arruinar": -0.7,
    "estropear": -0.6, "danar": -0.6, "perjudicar": -0.5,
    "lento": -0.3, "incomodo": -0.4, "dificil": -0.3,
    "imposible": -0.6, "insoportable": -0.8, "intolerable": -0.8,
    "aburrido": -0.4, "tedioso": -0.5, "monotono": -0.4,
}

EMOCIONES_LEXICO = {
    "feliz": "alegria", "contento": "alegria", "alegre": "alegria",
    "encantado": "alegria", "disfrutar": "alegria", "divertido": "alegria",
    "genial": "alegria", "maravilloso": "alegria", "fantastico": "alegria",
    "encantar": "alegria", "amar": "alegria", "adorar": "alegria",
    "triste": "tristeza", "deprimido": "tristeza", "llorar": "tristeza",
    "desolado": "tristeza", "abatido": "tristeza", "lamentar": "tristeza",
    "sufrir": "tristeza", "doler": "tristeza", "devastado": "tristeza",
    "furioso": "ira", "enfadado": "ira", "enfurecer": "ira",
    "irritado": "ira", "indignado": "ira", "rabioso": "ira",
    "odiar": "ira", "harto": "ira", "iracundo": "ira",
    "miedo": "miedo", "temor": "miedo", "terror": "miedo",
    "asustado": "miedo", "aterrorizado": "miedo", "panico": "miedo",
    "nervioso": "miedo", "ansioso": "miedo", "inquieto": "miedo",
    "sorprender": "sorpresa", "asombrar": "sorpresa", "impresionar": "sorpresa",
    "increible": "sorpresa", "inesperado": "sorpresa", "insolito": "sorpresa",
    "asqueroso": "asco", "repugnante": "asco", "nauseabundo": "asco",
    "repulsivo": "asco", "grotesco": "asco", "vomitivo": "asco",
}

NEGADORES = {"no", "nunca", "jamas", "tampoco", "ni", "sin", "ningun",
             "ninguno", "ninguna", "nada", "nadie", "apenas"}

INTENSIFICADORES = {
    "muy": 1.5, "mucho": 1.4, "muchisimo": 2.0, "bastante": 1.3,
    "demasiado": 1.5, "super": 1.6, "extremadamente": 1.8,
    "increiblemente": 1.7, "tremendamente": 1.6, "enormemente": 1.5,
    "absolutamente": 1.7, "completamente": 1.5, "totalmente": 1.5,
    "verdaderamente": 1.4, "realmente": 1.3, "sumamente": 1.6,
}

ATENUADORES = {
    "algo": 0.5, "poco": 0.4, "ligeramente": 0.4, "levemente": 0.4,
    "apenas": 0.3, "casi": 0.5, "medio": 0.5, "relativamente": 0.6,
    "moderadamente": 0.6, "parcialmente": 0.5, "minimamente": 0.3,
}

EMOJI_SENTIMIENTO = {
    "\U0001f60a": 0.6, "\U0001f603": 0.7, "\U0001f604": 0.7, "\U0001f601": 0.6, "\U0001f60d": 0.8,
    "\U0001f970": 0.8, "\U0001f618": 0.7, "\u2764\ufe0f": 0.7, "\U0001f495": 0.7, "\U0001f496": 0.7,
    "\U0001f44d": 0.5, "\U0001f44f": 0.6, "\U0001f389": 0.7, "\u2728": 0.5, "\U0001f31f": 0.5,
    "\U0001f600": 0.6, "\U0001f929": 0.8, "\U0001f60e": 0.5, "\U0001f973": 0.8, "\U0001f4aa": 0.5,
    "\U0001f622": -0.6, "\U0001f62d": -0.8, "\U0001f61e": -0.6, "\U0001f614": -0.5, "\U0001f61f": -0.5,
    "\U0001f620": -0.7, "\U0001f621": -0.8, "\U0001f92c": -0.9, "\U0001f494": -0.7, "\U0001f44e": -0.6,
    "\U0001f624": -0.6, "\U0001f630": -0.5, "\U0001f628": -0.6, "\U0001f631": -0.7, "\U0001f92e": -0.8,
    "\U0001f612": -0.5, "\U0001f644": -0.4, "\U0001f611": -0.3, "\U0001f610": 0.0, "\U0001f914": 0.0,
}

PATRON_COMILLAS = re.compile(r'["\u201c\u201d\u00ab\u00bb\'](.*?)["\u201c\u201d\u00ab\u00bb\']')
PATRON_PUNTOS_SUSPENSIVOS = re.compile(r'\.{3,}|\u2026')

FRASES_IRONICAS = [
    "si, claro", "si claro", "ya, claro", "claro que si",
    "por supuesto", "como no", "anda ya", "venga ya",
    "no me digas", "que bien", "genial...", "vaya vaya", "menos mal",
]


class AnalizadorLexico:

    def __init__(self):
        self.nlp = nlp

    def analizar(self, texto):
        doc = self.nlp(texto)
        explicaciones = []

        score_emojis, exp_emojis = self._analizar_emojis(texto)
        ironia, exp_ironia = self._detectar_ironia(texto, doc)
        score_lexico, exp_lexico, emociones = self._calcular_score(doc)

        score_total = score_lexico + score_emojis
        explicaciones = exp_lexico + exp_emojis + exp_ironia

        if ironia:
            score_total = -score_total
            explicaciones.append(
                f"Ironia detectada: se invierte la polaridad ({score_total * -1:.2f} -> {score_total:.2f})"
            )

        score_norm = max(-1.0, min(1.0, score_total))
        intensidad = min(1.0, abs(score_norm))

        if score_norm > 0.1:
            polaridad = "positive"
        elif score_norm < -0.1:
            polaridad = "negative"
        else:
            polaridad = "neutral"

        return {
            "polaridad": polaridad,
            "score": round(score_norm, 4),
            "intensidad": round(intensidad, 4),
            "ironia": ironia,
            "emociones": emociones,
            "explicaciones": explicaciones,
        }

    def _calcular_score(self, doc):
        score_total = 0.0
        explicaciones = []
        emociones = {}

        for i, token in enumerate(doc):
            lema = token.lemma_.lower()
            txt = token.text.lower()

            score_palabra = None
            palabra = None

            if lema in LEXICO_POSITIVO:
                score_palabra = LEXICO_POSITIVO[lema]
                palabra = lema
            elif lema in LEXICO_NEGATIVO:
                score_palabra = LEXICO_NEGATIVO[lema]
                palabra = lema
            elif txt in LEXICO_POSITIVO:
                score_palabra = LEXICO_POSITIVO[txt]
                palabra = txt
            elif txt in LEXICO_NEGATIVO:
                score_palabra = LEXICO_NEGATIVO[txt]
                palabra = txt

            if score_palabra is not None:
                original = score_palabra
                mods = []

                if self._tiene_negacion(doc, token, i):
                    score_palabra = -score_palabra * 0.8
                    mods.append("NEGACION")

                factor = self._buscar_modificador(doc, i)
                if factor != 1.0:
                    score_palabra *= factor
                    if factor > 1.0:
                        mods.append(f"INTENSIFICADOR (x{factor})")
                    else:
                        mods.append(f"ATENUADOR (x{factor})")

                score_total += score_palabra

                if lema in EMOCIONES_LEXICO:
                    emo = EMOCIONES_LEXICO[lema]
                    emociones[emo] = emociones.get(emo, 0) + abs(score_palabra)
                elif txt in EMOCIONES_LEXICO:
                    emo = EMOCIONES_LEXICO[txt]
                    emociones[emo] = emociones.get(emo, 0) + abs(score_palabra)

                mod_str = f" [{', '.join(mods)}]" if mods else ""
                explicaciones.append(f"'{palabra}' -> {original:+.2f}{mod_str} -> final: {score_palabra:+.2f}")

        if emociones:
            mx = max(emociones.values())
            if mx > 0:
                emociones = {k: round(min(1.0, v / mx), 4) for k, v in emociones.items()}

        return score_total, explicaciones, emociones

    def _tiene_negacion(self, doc, token, idx):
        for child in token.children:
            if child.dep_ == "advmod" and child.text.lower() in NEGADORES:
                return True
        if token.head and token.head.text.lower() in NEGADORES:
            return True
        for j in range(max(0, idx - 3), idx):
            if doc[j].text.lower() in NEGADORES:
                return True
        return False

    def _buscar_modificador(self, doc, idx):
        factor = 1.0
        for j in range(max(0, idx - 3), idx):
            txt = doc[j].text.lower()
            lema = doc[j].lemma_.lower()
            if txt in INTENSIFICADORES:
                factor *= INTENSIFICADORES[txt]
            elif lema in INTENSIFICADORES:
                factor *= INTENSIFICADORES[lema]
            elif txt in ATENUADORES:
                factor *= ATENUADORES[txt]
            elif lema in ATENUADORES:
                factor *= ATENUADORES[lema]
        if idx + 1 < len(doc) and doc[idx].text.endswith("!"):
            factor *= 1.2
        return factor

    def _analizar_emojis(self, texto):
        score = 0.0
        explicaciones = []
        for char in texto:
            if char in EMOJI_SENTIMIENTO:
                s = EMOJI_SENTIMIENTO[char]
                score += s
                explicaciones.append(f"Emoji detectado (U+{ord(char):04X}) -> score: {s:+.2f}")
            elif EMOJI_DISPONIBLE and emoji.is_emoji(char):
                pass
        return score, explicaciones

    def _detectar_ironia(self, texto, doc):
        explicaciones = []
        texto_lower = texto.lower()
        ironia = False

        for frase in FRASES_IRONICAS:
            if frase in texto_lower:
                ironia = True
                explicaciones.append(f"Patron ironico: '{frase}'")
                break

        comillas = PATRON_COMILLAS.findall(texto)
        for p in comillas:
            p_lower = p.lower().strip()
            if p_lower in LEXICO_POSITIVO:
                ironia = True
                explicaciones.append(f"Palabra positiva entre comillas: '{p_lower}' (posible ironia)")

        emojis_neg = [c for c in texto if c in EMOJI_SENTIMIENTO and EMOJI_SENTIMIENTO[c] < -0.3]
        palabras_pos = [t.lemma_.lower() for t in doc if t.lemma_.lower() in LEXICO_POSITIVO]
        if emojis_neg and palabras_pos:
            ironia = True
            explicaciones.append(f"Contradiccion: palabras positivas con emojis negativos")

        if PATRON_PUNTOS_SUSPENSIVOS.search(texto):
            lemas = [t.lemma_.lower() for t in doc[:5]]
            pos_inicio = [l for l in lemas if l in LEXICO_POSITIVO]
            if pos_inicio and any(f in texto_lower for f in ["claro", "si"]):
                ironia = True
                explicaciones.append("Puntos suspensivos con afirmacion y palabras positivas (posible ironia)")

        return ironia, explicaciones
