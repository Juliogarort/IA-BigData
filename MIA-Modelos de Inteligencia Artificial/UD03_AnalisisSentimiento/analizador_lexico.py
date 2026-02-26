# =============================================================
# Analizador de Sentimiento - Enfoque Léxico/Reglas
# Librería principal: spaCy
# =============================================================
# Este módulo implementa un análisis de sentimiento basado en
# reglas lingüísticas y un diccionario de sentimientos en español.
# Es rápido, explicable y detecta negaciones, intensificadores,
# atenuadores e ironía básica.
# =============================================================

import spacy
import re
try:
    import emoji
    EMOJI_DISPONIBLE = True
except ImportError:
    EMOJI_DISPONIBLE = False

# Cargar modelo de spaCy en español
nlp = spacy.load("es_core_news_sm")

# =============================================================
# LÉXICO DE SENTIMIENTO EN ESPAÑOL
# Diccionario con ~200 palabras y sus puntuaciones (-1 a +1)
# =============================================================

LEXICO_POSITIVO = {
    # --- Alegría / Satisfacción ---
    "bueno": 0.5, "bien": 0.4, "mejor": 0.6, "genial": 0.8,
    "excelente": 0.9, "maravilloso": 0.9, "fantástico": 0.9,
    "increíble": 0.8, "estupendo": 0.8, "perfecto": 0.9,
    "magnífico": 0.9, "espléndido": 0.8, "brillante": 0.8,
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

    # --- Aprobación / Calidad ---
    "útil": 0.4, "eficaz": 0.5, "eficiente": 0.5,
    "recomendable": 0.6, "recomendar": 0.6, "aprobar": 0.5,
    "mejorar": 0.4, "avanzar": 0.4, "progresar": 0.4,
    "lograr": 0.5, "conseguir": 0.5, "triunfar": 0.7,
    "éxito": 0.7, "victoria": 0.7, "ganar": 0.6,
    "acertar": 0.5, "destacar": 0.6, "sobresalir": 0.7,
    "impresionar": 0.7, "sorprender": 0.5, "asombrar": 0.6,
    "interesante": 0.5, "fascinante": 0.7, "apasionante": 0.7,
    "divertido": 0.6, "entretenido": 0.5, "gracioso": 0.5,
    "especial": 0.5, "único": 0.5, "excepcional": 0.8,
    "favorito": 0.7, "ideal": 0.7, "justo": 0.4,
    "correcto": 0.3, "adecuado": 0.3, "apropiado": 0.3,
    "rápido": 0.3, "cómodo": 0.5, "fácil": 0.3,
}

LEXICO_NEGATIVO = {
    # --- Tristeza / Dolor ---
    "malo": -0.5, "mal": -0.5, "peor": -0.7, "pésimo": -0.9,
    "horrible": -0.9, "terrible": -0.9, "espantoso": -0.9,
    "horroroso": -0.9, "desastroso": -0.8, "catastrófico": -0.9,
    "nefasto": -0.8, "lamentable": -0.7, "deplorable": -0.8,
    "penoso": -0.7, "patético": -0.7, "miserable": -0.8,
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

    # --- Ira / Rechazo ---
    "furioso": -0.9, "enfadado": -0.7, "enfurecer": -0.8,
    "irritado": -0.6, "indignado": -0.7, "enojado": -0.6,
    "rabioso": -0.8, "airado": -0.7, "iracundo": -0.8,
    "harto": -0.6, "cansado": -0.3, "agotado": -0.4,

    # --- Miedo / Preocupación ---
    "miedo": -0.6, "temor": -0.6, "terror": -0.9,
    "pánico": -0.8, "horror": -0.8, "pavor": -0.8,
    "asustado": -0.6, "aterrorizado": -0.9, "atemorizado": -0.7,
    "preocupado": -0.4, "ansioso": -0.5, "inquieto": -0.4,
    "nervioso": -0.4, "tenso": -0.4, "estresado": -0.5,

    # --- Calidad negativa ---
    "inútil": -0.6, "ineficaz": -0.5, "ineficiente": -0.5,
    "fracaso": -0.7, "fallar": -0.6, "fracasar": -0.7,
    "perder": -0.5, "derrota": -0.6, "error": -0.4,
    "problema": -0.4, "defecto": -0.5, "fallo": -0.5,
    "romper": -0.5, "destruir": -0.7, "arruinar": -0.7,
    "estropear": -0.6, "dañar": -0.6, "perjudicar": -0.5,
    "lento": -0.3, "incómodo": -0.4, "difícil": -0.3,
    "imposible": -0.6, "insoportable": -0.8, "intolerable": -0.8,
    "aburrido": -0.4, "tedioso": -0.5, "monótono": -0.4,
}

# =============================================================
# EMOCIONES ASOCIADAS A PALABRAS
# =============================================================

EMOCIONES_LEXICO = {
    # alegría
    "feliz": "alegria", "contento": "alegria", "alegre": "alegria",
    "encantado": "alegria", "disfrutar": "alegria", "divertido": "alegria",
    "genial": "alegria", "maravilloso": "alegria", "fantástico": "alegria",
    "encantar": "alegria", "amar": "alegria", "adorar": "alegria",
    # tristeza
    "triste": "tristeza", "deprimido": "tristeza", "llorar": "tristeza",
    "desolado": "tristeza", "abatido": "tristeza", "lamentar": "tristeza",
    "sufrir": "tristeza", "doler": "tristeza", "devastado": "tristeza",
    # ira
    "furioso": "ira", "enfadado": "ira", "enfurecer": "ira",
    "irritado": "ira", "indignado": "ira", "rabioso": "ira",
    "odiar": "ira", "harto": "ira", "iracundo": "ira",
    # miedo
    "miedo": "miedo", "temor": "miedo", "terror": "miedo",
    "asustado": "miedo", "aterrorizado": "miedo", "pánico": "miedo",
    "nervioso": "miedo", "ansioso": "miedo", "inquieto": "miedo",
    # sorpresa
    "sorprender": "sorpresa", "asombrar": "sorpresa", "impresionar": "sorpresa",
    "increíble": "sorpresa", "inesperado": "sorpresa", "insólito": "sorpresa",
    # asco
    "asqueroso": "asco", "repugnante": "asco", "nauseabundo": "asco",
    "repulsivo": "asco", "grotesco": "asco", "vomitivo": "asco",
}

# =============================================================
# MODIFICADORES LINGÜÍSTICOS
# =============================================================

NEGADORES = {"no", "nunca", "jamás", "tampoco", "ni", "sin", "ningún",
             "ninguno", "ninguna", "nada", "nadie", "apenas"}

INTENSIFICADORES = {
    "muy": 1.5, "mucho": 1.4, "muchísimo": 2.0, "bastante": 1.3,
    "demasiado": 1.5, "súper": 1.6, "super": 1.6, "extremadamente": 1.8,
    "increíblemente": 1.7, "tremendamente": 1.6, "enormemente": 1.5,
    "absolutamente": 1.7, "completamente": 1.5, "totalmente": 1.5,
    "verdaderamente": 1.4, "realmente": 1.3, "sumamente": 1.6,
    "extraordinariamente": 1.7, "excesivamente": 1.5,
}

ATENUADORES = {
    "algo": 0.5, "poco": 0.4, "ligeramente": 0.4, "levemente": 0.4,
    "apenas": 0.3, "casi": 0.5, "medio": 0.5, "relativamente": 0.6,
    "moderadamente": 0.6, "parcialmente": 0.5, "mínimamente": 0.3,
}

# =============================================================
# EMOJIS Y SUS SENTIMIENTOS
# =============================================================

EMOJI_SENTIMIENTO = {
    "😊": 0.6, "😃": 0.7, "😄": 0.7, "😁": 0.6, "😍": 0.8,
    "🥰": 0.8, "😘": 0.7, "❤️": 0.7, "💕": 0.7, "💖": 0.7,
    "👍": 0.5, "👏": 0.6, "🎉": 0.7, "✨": 0.5, "🌟": 0.5,
    "😀": 0.6, "🤩": 0.8, "😎": 0.5, "🥳": 0.8, "💪": 0.5,
    "😢": -0.6, "😭": -0.8, "😞": -0.6, "😔": -0.5, "😟": -0.5,
    "😠": -0.7, "😡": -0.8, "🤬": -0.9, "💔": -0.7, "👎": -0.6,
    "😤": -0.6, "😰": -0.5, "😨": -0.6, "😱": -0.7, "🤮": -0.8,
    "😒": -0.5, "🙄": -0.4, "😑": -0.3, "😐": 0.0, "🤔": 0.0,
}

# =============================================================
# PATRONES DE IRONÍA
# =============================================================

PATRON_COMILLAS = re.compile(r'["\u201c\u201d\u00ab\u00bb\'](.*?)["\u201c\u201d\u00ab\u00bb\']')
PATRON_PUNTOS_SUSPENSIVOS = re.compile(r'\.{3,}|…')
PATRON_EXCLAMACION_MULTIPLE = re.compile(r'!{2,}')
PATRON_INTERROGACION_EXCLAMACION = re.compile(r'[¿?]+.*[!¡]+|[!¡]+.*[¿?]+')

FRASES_IRONICAS = [
    "sí, claro", "si, claro", "sí claro", "si claro",
    "ya, claro", "claro que sí", "claro que si",
    "por supuesto", "cómo no", "como no",
    "anda ya", "venga ya", "no me digas",
    "qué bien", "que bien", "genial...",
    "vaya vaya", "menos mal",
]


# =============================================================
# CLASE PRINCIPAL: AnalizadorLexico
# =============================================================

class AnalizadorLexico:
    """
    Analizador de sentimiento basado en reglas léxicas.
    Usa spaCy para procesamiento lingüístico y un diccionario
    de sentimientos en español para determinar polaridad.
    """

    def __init__(self):
        """Inicializa el analizador con el modelo de spaCy."""
        self.nlp = nlp

    def analizar(self, texto):
        """
        Analiza el sentimiento de un texto usando reglas léxicas.

        Args:
            texto (str): Texto en español a analizar.

        Returns:
            dict: Resultado con polaridad, score, intensidad,
                  ironía, emociones y explicaciones.
        """
        doc = self.nlp(texto)
        explicaciones = []

        # 1. Detectar emojis
        score_emojis, explicaciones_emojis = self._analizar_emojis(texto)

        # 2. Detectar ironía
        ironia, explicaciones_ironia = self._detectar_ironia(texto, doc)

        # 3. Calcular score léxico con negaciones, intensificadores, atenuadores
        score_lexico, explicaciones_lexico, emociones_detectadas = self._calcular_score(doc)

        # 4. Combinar scores
        score_total = score_lexico + score_emojis
        explicaciones = explicaciones_lexico + explicaciones_emojis + explicaciones_ironia

        # Si hay ironía, invertimos el score
        if ironia:
            score_total = -score_total
            explicaciones.append(
                f"⚡ Ironía detectada: se invierte la polaridad (de {score_total * -1:.2f} a {score_total:.2f})"
            )

        # 5. Normalizar score a rango [-1, 1]
        score_normalizado = max(-1.0, min(1.0, score_total))

        # 6. Calcular intensidad (0-1)
        intensidad = min(1.0, abs(score_normalizado))

        # 7. Determinar polaridad
        if score_normalizado > 0.1:
            polaridad = "positive"
        elif score_normalizado < -0.1:
            polaridad = "negative"
        else:
            polaridad = "neutral"

        return {
            "polaridad": polaridad,
            "score": round(score_normalizado, 4),
            "intensidad": round(intensidad, 4),
            "ironia": ironia,
            "emociones": emociones_detectadas,
            "explicaciones": explicaciones,
        }

    def _calcular_score(self, doc):
        """
        Calcula el score de sentimiento recorriendo los tokens
        y aplicando reglas de negación, intensificación y atenuación.
        """
        score_total = 0.0
        explicaciones = []
        emociones = {}
        tokens_procesados = set()

        for i, token in enumerate(doc):
            lema = token.lemma_.lower()
            texto_token = token.text.lower()

            # Saltar tokens ya procesados
            if i in tokens_procesados:
                continue

            # Buscar en el léxico (por lema o por texto)
            score_palabra = None
            palabra_encontrada = None

            if lema in LEXICO_POSITIVO:
                score_palabra = LEXICO_POSITIVO[lema]
                palabra_encontrada = lema
            elif lema in LEXICO_NEGATIVO:
                score_palabra = LEXICO_NEGATIVO[lema]
                palabra_encontrada = lema
            elif texto_token in LEXICO_POSITIVO:
                score_palabra = LEXICO_POSITIVO[texto_token]
                palabra_encontrada = texto_token
            elif texto_token in LEXICO_NEGATIVO:
                score_palabra = LEXICO_NEGATIVO[texto_token]
                palabra_encontrada = texto_token

            if score_palabra is not None:
                score_original = score_palabra
                modificadores = []

                # --- Detectar negación ---
                negado = self._tiene_negacion(doc, token, i)
                if negado:
                    score_palabra = -score_palabra * 0.8  # Invertir con factor
                    modificadores.append("NEGACIÓN")

                # --- Detectar intensificadores/atenuadores ---
                factor = self._buscar_modificador(doc, i)
                if factor != 1.0:
                    score_palabra *= factor
                    if factor > 1.0:
                        modificadores.append(f"INTENSIFICADOR (×{factor})")
                    else:
                        modificadores.append(f"ATENUADOR (×{factor})")

                score_total += score_palabra

                # Registrar emoción
                if lema in EMOCIONES_LEXICO:
                    emocion = EMOCIONES_LEXICO[lema]
                    emociones[emocion] = emociones.get(emocion, 0) + abs(score_palabra)
                elif texto_token in EMOCIONES_LEXICO:
                    emocion = EMOCIONES_LEXICO[texto_token]
                    emociones[emocion] = emociones.get(emocion, 0) + abs(score_palabra)

                # Explicación
                mod_str = f" [{', '.join(modificadores)}]" if modificadores else ""
                explicaciones.append(
                    f"'{palabra_encontrada}' → score: {score_original:+.2f}"
                    f"{mod_str} → final: {score_palabra:+.2f}"
                )

        # Normalizar emociones a rango 0-1
        if emociones:
            max_emocion = max(emociones.values())
            if max_emocion > 0:
                emociones = {k: round(min(1.0, v / max_emocion), 4) for k, v in emociones.items()}

        return score_total, explicaciones, emociones

    def _tiene_negacion(self, doc, token, idx):
        """
        Detecta si un token está negado, buscando en el árbol
        de dependencias y en los tokens previos.
        """
        # Método 1: Buscar en los hijos del token por dependencia
        for child in token.children:
            if child.dep_ == "advmod" and child.text.lower() in NEGADORES:
                return True

        # Método 2: Buscar en el padre
        if token.head and token.head.text.lower() in NEGADORES:
            return True

        # Método 3: Buscar en los 3 tokens anteriores
        ventana = max(0, idx - 3)
        for j in range(ventana, idx):
            if doc[j].text.lower() in NEGADORES:
                return True

        return False

    def _buscar_modificador(self, doc, idx):
        """
        Busca intensificadores o atenuadores en los tokens cercanos.
        Devuelve el factor multiplicador (>1 intensifica, <1 atenúa).
        """
        factor = 1.0

        # Buscar en los 3 tokens anteriores
        ventana = max(0, idx - 3)
        for j in range(ventana, idx):
            texto_j = doc[j].text.lower()
            lema_j = doc[j].lemma_.lower()

            if texto_j in INTENSIFICADORES:
                factor *= INTENSIFICADORES[texto_j]
            elif lema_j in INTENSIFICADORES:
                factor *= INTENSIFICADORES[lema_j]
            elif texto_j in ATENUADORES:
                factor *= ATENUADORES[texto_j]
            elif lema_j in ATENUADORES:
                factor *= ATENUADORES[lema_j]

        # Detectar signos de exclamación como intensificador ligero
        if idx + 1 < len(doc) and doc[idx].text.endswith("!"):
            factor *= 1.2

        return factor

    def _analizar_emojis(self, texto):
        """
        Detecta emojis en el texto y asigna scores de sentimiento.
        """
        score_total = 0.0
        explicaciones = []

        for char in texto:
            if char in EMOJI_SENTIMIENTO:
                score = EMOJI_SENTIMIENTO[char]
                score_total += score
                explicaciones.append(f"Emoji '{char}' → score: {score:+.2f}")
            elif EMOJI_DISPONIBLE and emoji.is_emoji(char):
                # Emoji no catalogado, neutro
                pass

        return score_total, explicaciones

    def _detectar_ironia(self, texto, doc):
        """
        Detecta ironía básica usando heurísticas:
        - Comillas alrededor de palabras positivas
        - Frases irónicas conocidas
        - Contradicción entre texto positivo y emojis negativos
        - Puntos suspensivos excesivos con palabras positivas
        """
        explicaciones = []
        texto_lower = texto.lower()
        ironia = False

        # 1. Frases irónicas conocidas
        for frase in FRASES_IRONICAS:
            if frase in texto_lower:
                ironia = True
                explicaciones.append(
                    f"🔍 Patrón irónico detectado: '{frase}'"
                )
                break

        # 2. Comillas alrededor de palabras positivas
        comillas = PATRON_COMILLAS.findall(texto)
        for palabra_entrecomillada in comillas:
            p_lower = palabra_entrecomillada.lower().strip()
            if p_lower in LEXICO_POSITIVO:
                ironia = True
                explicaciones.append(
                    f"🔍 Palabra positiva entre comillas: '\"{p_lower}\"' "
                    f"(posible uso irónico)"
                )

        # 3. Contradicción emojis negativos + texto positivo
        emojis_negativos = [c for c in texto if c in EMOJI_SENTIMIENTO
                           and EMOJI_SENTIMIENTO[c] < -0.3]
        palabras_positivas = [t.lemma_.lower() for t in doc
                             if t.lemma_.lower() in LEXICO_POSITIVO]

        if emojis_negativos and palabras_positivas:
            ironia = True
            explicaciones.append(
                f"🔍 Contradicción: palabras positivas ({', '.join(palabras_positivas[:3])}) "
                f"con emojis negativos ({''.join(emojis_negativos[:3])})"
            )

        # 4. Puntos suspensivos + palabras positivas al inicio
        if PATRON_PUNTOS_SUSPENSIVOS.search(texto):
            lemas = [t.lemma_.lower() for t in doc[:5]]
            positivas_inicio = [l for l in lemas if l in LEXICO_POSITIVO]
            if positivas_inicio and any(f in texto_lower for f in ["claro", "sí", "si"]):
                ironia = True
                explicaciones.append(
                    "🔍 Puntos suspensivos con afirmación y palabras positivas "
                    "(posible ironía)"
                )

        return ironia, explicaciones


# =============================================================
# FUNCIÓN DE CONVENIENCIA
# =============================================================

def analizar_lexico(texto):
    """
    Función de conveniencia para analizar un texto sin
    necesidad de instanciar la clase manualmente.

    Args:
        texto (str): Texto en español a analizar.

    Returns:
        dict: Resultado del análisis léxico.
    """
    analizador = AnalizadorLexico()
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

    analizador = AnalizadorLexico()
    for texto in textos_prueba:
        print(f"\n{'='*60}")
        print(f"Texto: \"{texto}\"")
        resultado = analizador.analizar(texto)
        print(json.dumps(resultado, ensure_ascii=False, indent=2))
