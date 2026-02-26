import json
import os
from analizador_fusion import AnalizadorFusion

DIR_PROYECTO = os.path.dirname(os.path.abspath(__file__))

EJEMPLOS = [
    ("POSITIVO",    "Fernando Alonso ha hecho una carrera increible, que pilotazo"),
    ("POSITIVO",    "Carlos Sainz ha ganado el Gran Premio, estoy muy contento"),
    ("NEGATIVO",    "Que desastre de estrategia, han arruinado la carrera de Sainz"),
    ("NEGATIVO",    "Alonso ha abandonado por un fallo mecanico, estoy furioso"),
    ("NEGACION",    "No me gusta nada como ha pilotado hoy, ha sido un desastre"),
    ("IRONIA",      "Si, claro... 'fantastica' estrategia del muro, como siempre..."),
    ("NEUTRO",      "La proxima carrera del campeonato es en Monza el domingo"),
    ("MIXTO",       "Alonso ha hecho una gran clasificacion pero la carrera ha sido horrible"),
    ("INTENSIF.",   "Estoy super emocionado con el fichaje de Alonso por Aston Martin"),
    ("ATENUADOR",   "Me gusto un poco la carrera, fue algo aburrida en general"),
]


def mostrar_resultado(r):
    traducciones = {"positive": "POSITIVO", "negative": "NEGATIVO", "neutral": "NEUTRO", "mixed": "MIXTO"}
    pol = traducciones.get(r["polaridad"], r["polaridad"].upper())
    score = r["score_polaridad"]
    ironia = r["ironia"]

    barra_len = 20
    pos = int(max(0, score) * barra_len)
    neg = int(max(0, -score) * barra_len)
    barra = "." * (barra_len - neg) + "#" * neg + "|" + "#" * pos + "." * (barra_len - pos)

    print(f"\n  Resultado:")
    print(f"    Polaridad:  {pol}")
    print(f"    Score:      {score:+.4f}  [{barra}]")
    if ironia:
        print(f"    Ironia:     SI (detectada)")
    if r["emociones"]:
        top = sorted(r["emociones"].items(), key=lambda x: x[1], reverse=True)[:3]
        for emo, val in top:
            if val > 0.01:
                b = "#" * int(val * 15) + "." * (15 - int(val * 15))
                print(f"    {emo:<12} [{b}] {val:.0%}")


def main():
    print("\n" + "=" * 60)
    print("  ANALISIS DE SENTIMIENTO - F1")
    print("=" * 60)

    analizador = AnalizadorFusion()

    print("Ejemplos de frases que el sistema puede analizar:")
    print("-" * 60)
    for tipo, texto in EJEMPLOS:
        print(f"  [{tipo:<10}] {texto}")
    print("-" * 60)

    resultados = []

    while True:
        print()
        texto = input("Escribe una frase (o 'salir' para terminar): ").strip()

        if texto.lower() in ("salir", "exit", "q", ""):
            break

        r = analizador.analizar(texto)
        resultados.append(r)
        print()
        mostrar_resultado(r)

    if resultados:
        archivo = os.path.join(DIR_PROYECTO, "resultados_analisis.json")
        datos = [{
            "texto": r["texto"],
            "polaridad": r["polaridad"],
            "score": r["score_polaridad"],
            "emociones": r["emociones"],
            "intensidad": r["intensidad"],
            "ironia": r["ironia"],
        } for r in resultados]

        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)

        print(f"\n  {len(resultados)} resultados guardados en: {archivo}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
