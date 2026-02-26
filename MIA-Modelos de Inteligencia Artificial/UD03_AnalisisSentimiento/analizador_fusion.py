# =============================================================
# Analizador de Sentimiento - Fusión de Pipelines
# Combina: Enfoque Léxico + Enfoque Modelo
# =============================================================
# Este módulo fusiona las salidas del analizador léxico/reglas
# y del analizador basado en modelos para producir un análisis
# final robusto con salida JSON estructurada.
# =============================================================

import json
from analizador_lexico import AnalizadorLexico
from analizador_modelo import AnalizadorModelo


class AnalizadorFusion:
    """
    Analizador de fusión que combina los resultados del
    enfoque léxico y el enfoque basado en modelos.

    Ponderación por defecto:
    - 40% léxico (mejor para ironía y explicabilidad)
    - 60% modelo (mejor para contexto y emociones)
    """

    def __init__(self, peso_lexico=0.4, peso_modelo=0.6):
        """
        Inicializa ambos analizadores.

        Args:
            peso_lexico (float): Peso del analizador léxico (0-1).
            peso_modelo (float): Peso del analizador modelo (0-1).
        """
        self.peso_lexico = peso_lexico
        self.peso_modelo = peso_modelo

        print("\n" + "=" * 60)
        print("INICIALIZANDO SISTEMA DE ANÁLISIS DE SENTIMIENTO")
        print("=" * 60)
        print(f"  Pesos: Léxico={peso_lexico:.0%} | Modelo={peso_modelo:.0%}")
        print()

        print("  [1/2] Inicializando analizador léxico...")
        self.lexico = AnalizadorLexico()
        print("    ✓ Analizador léxico listo\n")

        print("  [2/2] Inicializando analizador de modelos...")
        self.modelo = AnalizadorModelo()
        print()

        print("=" * 60)
        print("✓ SISTEMA LISTO PARA ANALIZAR")
        print("=" * 60)

    def analizar(self, texto):
        """
        Analiza un texto fusionando ambos pipelines.

        Args:
            texto (str): Texto en español a analizar.

        Returns:
            dict: Resultado JSON estructurado con toda la información.
        """
        # Obtener resultados de ambos pipelines
        resultado_lexico = self.lexico.analizar(texto)
        resultado_modelo = self.modelo.analizar(texto)

        # --- Fusionar score de polaridad ---
        score_lexico = resultado_lexico["score"]
        score_modelo = resultado_modelo["score"]
        ironia = resultado_lexico["ironia"]

        # Si hay ironía, el léxico tiene prioridad (80/20)
        if ironia:
            peso_l = 0.8
            peso_m = 0.2
        else:
            peso_l = self.peso_lexico
            peso_m = self.peso_modelo

        score_fusionado = (score_lexico * peso_l) + (score_modelo * peso_m)
        score_fusionado = max(-1.0, min(1.0, score_fusionado))

        # --- Determinar polaridad final ---
        polaridad = self._determinar_polaridad(
            score_fusionado,
            resultado_lexico["polaridad"],
            resultado_modelo["polaridad"],
        )

        # --- Fusionar emociones ---
        emociones = self._fusionar_emociones(
            resultado_lexico.get("emociones", {}), resultado_modelo.get("emociones", {})
        )

        # --- Calcular intensidad fusionada ---
        intensidad_lexico = resultado_lexico.get("intensidad", 0)
        intensidad_modelo = abs(score_modelo)
        intensidad = (intensidad_lexico * peso_l) + (intensidad_modelo * peso_m)
        intensidad = min(1.0, intensidad)

        # --- Combinar explicaciones ---
        explicaciones = []
        explicaciones.append("📝 Análisis Léxico:")
        for exp in resultado_lexico["explicaciones"]:
            explicaciones.append(f"  • {exp}")
        explicaciones.append("🤖 Análisis Modelo:")
        for exp in resultado_modelo["explicaciones"]:
            explicaciones.append(f"  • {exp}")
        explicaciones.append(
            f"⚖️ Fusión: Léxico({peso_l:.0%}) × {score_lexico:+.4f} + "
            f"Modelo({peso_m:.0%}) × {score_modelo:+.4f} = {score_fusionado:+.4f}"
        )

        # --- Construir JSON final ---
        resultado_final = {
            "texto": texto,
            "polaridad": polaridad,
            "score_polaridad": round(score_fusionado, 4),
            "emociones": emociones,
            "intensidad": round(intensidad, 4),
            "ironia": ironia,
            "explicaciones": explicaciones,
            "detalle_lexico": resultado_lexico,
            "detalle_modelo": resultado_modelo,
        }

        return resultado_final

    def _determinar_polaridad(self, score, pol_lexico, pol_modelo):
        """
        Determina la polaridad final considerando ambos pipelines.
        Si hay desacuerdo, puede ser 'mixed'.
        """
        # Si ambos coinciden, usar esa polaridad
        if pol_lexico == pol_modelo:
            return pol_lexico

        # Si el score fusionado es claro, usar eso
        if score > 0.2:
            return "positive"
        elif score < -0.2:
            return "negative"
        elif abs(score) <= 0.1:
            return "neutral"
        else:
            # Los pipelines no coinciden y el score no es claro
            return "mixed"

    def _fusionar_emociones(self, emociones_lexico, emociones_modelo):
        """
        Fusiona las emociones de ambos pipelines.
        El modelo tiene prioridad pero se enriquece con el léxico.
        """
        emociones_fusionadas = {}

        # Tomar todas las emociones del modelo como base
        todas_emociones = set(
            list(emociones_modelo.keys()) + list(emociones_lexico.keys())
        )

        for emocion in todas_emociones:
            val_modelo = emociones_modelo.get(emocion, 0)
            val_lexico = emociones_lexico.get(emocion, 0)

            # Si la emoción aparece en ambos, ponderar
            if val_modelo > 0 and val_lexico > 0:
                valor = val_modelo * 0.6 + val_lexico * 0.4
            elif val_modelo > 0:
                valor = val_modelo
            else:
                valor = val_lexico * 0.5  # Menos confianza solo del léxico

            if valor > 0.01:  # Filtrar valores insignificantes
                emociones_fusionadas[emocion] = round(valor, 4)

        return emociones_fusionadas

    def analizar_lote(self, textos):
        """
        Analiza una lista de textos.

        Args:
            textos (list): Lista de textos a analizar.

        Returns:
            list: Lista de resultados JSON.
        """
        resultados = []
        for i, texto in enumerate(textos, 1):
            print(f"\n  Analizando texto {i}/{len(textos)}...")
            resultado = self.analizar(texto)
            resultados.append(resultado)
        return resultados


# =============================================================
# FUNCIÓN DE CONVENIENCIA
# =============================================================


def analizar_texto(texto):
    """
    Función de conveniencia para analizar un texto completo
    con el pipeline híbrido.

    Args:
        texto (str): Texto en español a analizar.

    Returns:
        dict: Resultado del análisis fusionado.
    """
    analizador = AnalizadorFusion()
    return analizador.analizar(texto)


# =============================================================
# PRUEBA RÁPIDA (solo si se ejecuta directamente)
# =============================================================

if __name__ == "__main__":
    textos = [
        "Me encanta este producto, es maravilloso",
        "No me gusta nada, es horrible",
    ]

    analizador = AnalizadorFusion()
    for texto in textos:
        resultado = analizador.analizar(texto)
        print(f"\n{'='*60}")
        print(json.dumps(resultado, ensure_ascii=False, indent=2))
