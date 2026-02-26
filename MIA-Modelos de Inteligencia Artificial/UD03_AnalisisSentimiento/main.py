# =============================================================
# PROYECTO: Análisis de Sentimiento en Español
# UD03_PLN - Modelos de Inteligencia Artificial 2025/26
# =============================================================
# Pipeline híbrido que combina:
#   1. Enfoque léxico/reglas (spaCy + diccionario)
#   2. Enfoque basado en modelos (pysentimiento/Transformers)
# Produce un análisis final robusto con salida JSON estructurada.
# =============================================================
# Librerías: spaCy, NLTK, Transformers (vía pysentimiento),
#            emoji, rapidfuzz (opcionales)
# =============================================================

import json
import sys
from analizador_fusion import AnalizadorFusion


# =============================================================
# TEXTOS DE PRUEBA
# Cubren todos los requisitos del proyecto:
# - Positivo/negativo/neutro simple
# - Negaciones
# - Ironía
# - Intensificadores
# - Atenuadores
# - Texto mixto
# - Emojis
# =============================================================

TEXTOS_PRUEBA = [
    # 1. Positivo claro
    "Me encanta este producto, es absolutamente maravilloso y fantástico",
    # 2. Negativo claro
    "Este servicio es terrible, estoy muy decepcionado y furioso",
    # 3. Negación: "no me gusta" no puede interpretarse como positivo
    "No me gusta nada este restaurante, nunca fue bueno",
    # 4. Ironía con comillas y emoji
    "Sí, claro... 'excelente' servicio 😒",
    # 5. Intensificadores: "me encantó muchísimo!!!"
    "Me encantó muchísimo, estoy súper contento!!!",
    # 6. Atenuadores: "me gustó un poco"
    "Me gustó un poco la película, algo entretenida",
    # 7. Mixto: "Me encantó... pero llegó tarde"
    "Me encantó la comida pero el servicio fue horrible y lento",
    # 8. Emojis emocionales
    "Qué día más horrible 😭💔 no puedo más",
    # 9. Neutro
    "El edificio tiene tres plantas y un ascensor",
    # 10. Doble negación
    "No es que no me guste, pero tampoco me emociona demasiado",
    # 11. Ironía sin comillas
    "Genial, otra vez tarde... qué sorpresa",
    # 12. Emojis positivos
    "Hoy ha sido un día increíble 😊🎉 estoy muy feliz",
]


def mostrar_resultado(resultado, numero):
    """
    Muestra el resultado de un análisis de forma visual y clara.
    """
    print(f"\n{'═'*70}")
    print(f"  TEXTO #{numero}")
    print(f"{'═'*70}")
    print(f"  📄 \"{resultado['texto']}\"")
    print(f"{'─'*70}")

    # Polaridad con color/emoji
    emojis_polaridad = {
        "positive": "🟢",
        "negative": "🔴",
        "neutral": "⚪",
        "mixed": "🟡",
    }
    emoji_pol = emojis_polaridad.get(resultado["polaridad"], "⚪")

    print(f"  {emoji_pol} Polaridad:  {resultado['polaridad'].upper()}")
    print(f"  📊 Score:      {resultado['score_polaridad']:+.4f}  (rango: -1 a +1)")
    print(f"  🔥 Intensidad: {resultado['intensidad']:.4f}  (rango: 0 a 1)")
    print(f"  😏 Ironía:     {'Sí ⚠️' if resultado['ironia'] else 'No'}")

    # Emociones
    if resultado["emociones"]:
        print(f"  {'─'*50}")
        print(f"  🎭 Emociones detectadas:")
        emojis_emo = {
            "alegria": "😊",
            "tristeza": "😢",
            "ira": "😠",
            "miedo": "😨",
            "sorpresa": "😮",
            "asco": "🤢",
            "otros": "😐",
        }
        for emo, valor in sorted(
            resultado["emociones"].items(), key=lambda x: x[1], reverse=True
        ):
            if valor > 0.01:
                barra = "█" * int(valor * 20) + "░" * (20 - int(valor * 20))
                emoji_e = emojis_emo.get(emo, "❓")
                print(f"     {emoji_e} {emo:<12} {barra} {valor:.4f}")

    # Explicaciones
    print(f"  {'─'*50}")
    print(f"  💬 Explicaciones:")
    for exp in resultado["explicaciones"]:
        print(f"     {exp}")

    print()


def mostrar_json(resultado):
    """
    Muestra el JSON completo del resultado.
    """
    # Crear copia sin los detalles internos para el JSON limpio
    json_limpio = {
        "texto": resultado["texto"],
        "polaridad": resultado["polaridad"],
        "score_polaridad": resultado["score_polaridad"],
        "emociones": resultado["emociones"],
        "intensidad": resultado["intensidad"],
        "ironia": resultado["ironia"],
        "explicaciones": resultado["explicaciones"],
    }
    return json.dumps(json_limpio, ensure_ascii=False, indent=2)


def main():
    """
    Función principal: inicializa el sistema y analiza
    todos los textos de prueba.
    """
    print("\n" + "╔" + "═" * 68 + "╗")
    print("║" + " PROYECTO: ANÁLISIS DE SENTIMIENTO EN ESPAÑOL".center(68) + "║")
    print(
        "║" + " UD03_PLN - Modelos de Inteligencia Artificial 2025/26".center(68) + "║"
    )
    print("║" + " Pipeline Híbrido: Léxico + Modelo (Fusión)".center(68) + "║")
    print("╚" + "═" * 68 + "╝")

    # Inicializar el sistema de fusión
    analizador = AnalizadorFusion()

    # Analizar cada texto
    todos_resultados = []
    for i, texto in enumerate(TEXTOS_PRUEBA, 1):
        resultado = analizador.analizar(texto)
        todos_resultados.append(resultado)
        mostrar_resultado(resultado, i)

    # Mostrar resumen final
    print("\n" + "╔" + "═" * 68 + "╗")
    print("║" + " RESUMEN DE RESULTADOS".center(68) + "║")
    print("╚" + "═" * 68 + "╝")

    print(
        f"\n  {'#':<4} {'Polaridad':<12} {'Score':>8} {'Intensidad':>12} {'Ironía':>8}  Texto"
    )
    print(f"  {'─'*4} {'─'*12} {'─'*8} {'─'*12} {'─'*8}  {'─'*30}")

    for i, r in enumerate(todos_resultados, 1):
        texto_corto = r["texto"][:35] + "..." if len(r["texto"]) > 35 else r["texto"]
        ironia_str = "Sí" if r["ironia"] else "No"
        print(
            f"  {i:<4} {r['polaridad']:<12} {r['score_polaridad']:>+8.4f} "
            f"{r['intensidad']:>12.4f} {ironia_str:>8}  {texto_corto}"
        )

    # Exportar todos los resultados a JSON
    print(f"\n{'═'*70}")
    print("  📋 SALIDA JSON COMPLETA (ejemplo del primer texto):")
    print(f"{'═'*70}")
    print(mostrar_json(todos_resultados[0]))

    # Guardar todos los resultados en un archivo JSON
    archivo_json = "resultados_analisis.json"
    resultados_json = []
    for r in todos_resultados:
        resultados_json.append(
            {
                "texto": r["texto"],
                "polaridad": r["polaridad"],
                "score_polaridad": r["score_polaridad"],
                "emociones": r["emociones"],
                "intensidad": r["intensidad"],
                "ironia": r["ironia"],
                "explicaciones": r["explicaciones"],
            }
        )

    with open(archivo_json, "w", encoding="utf-8") as f:
        json.dump(resultados_json, f, ensure_ascii=False, indent=2)

    print(f"\n  ✅ Resultados guardados en '{archivo_json}'")
    print(f"\n{'═'*70}")
    print("  ✅ ANÁLISIS COMPLETADO - {0} textos procesados".format(len(TEXTOS_PRUEBA)))
    print(f"{'═'*70}\n")


if __name__ == "__main__":
    main()
