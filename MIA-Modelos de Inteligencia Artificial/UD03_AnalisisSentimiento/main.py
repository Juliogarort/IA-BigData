# =============================================================
# Analisis de Sentimiento en Espanol - UD03 PLN
# Pipeline hibrido: lexico + modelo (fusion)
# =============================================================

import json
import os
from analizador_fusion import AnalizadorFusion

DIR_PROYECTO = os.path.dirname(os.path.abspath(__file__))

# Textos de prueba tematica F1
TEXTOS = [
    # Positivos
    "Fernando Alonso ha hecho una carrera increible, que pilotazo",
    "Carlos Sainz ha ganado el Gran Premio, estoy muy contento",
    "Que salida tan brillante de Alonso, ha adelantado a tres coches",
    # Negativos
    "Que desastre de estrategia del equipo, han arruinado la carrera de Sainz",
    "Alonso ha abandonado por un fallo mecanico, estoy furioso",
    "No me gusta nada como ha pilotado hoy, ha sido un desastre",
    # Ironia
    "Si, claro... 'fantastica' estrategia del muro, como siempre...",
    "Genial, otro abandono por fiabilidad... que sorpresa",
    # Neutro
    "La proxima carrera del campeonato es en Monza el domingo",
    # Mixto
    "Alonso ha hecho una gran clasificacion pero la carrera ha sido horrible",
    # Intensificadores
    "Estoy super emocionado con el fichaje de Alonso por Aston Martin",
    # Atenuadores
    "Me gusto un poco la carrera, fue algo aburrida en general",
]


def main():
    print("\n" + "=" * 60)
    print("  ANALISIS DE SENTIMIENTO - TEXTOS F1")
    print("=" * 60)

    analizador = AnalizadorFusion()

    resultados = []
    for i, texto in enumerate(TEXTOS, 1):
        r = analizador.analizar(texto)
        resultados.append(r)

        pol = r["polaridad"].upper()
        score = r["score_polaridad"]
        ironia = "Si" if r["ironia"] else "No"

        print(f"\n  [{i}] \"{texto}\"")
        print(f"      Polaridad: {pol}  |  Score: {score:+.4f}  |  Ironia: {ironia}")

        if r["emociones"]:
            top = sorted(r["emociones"].items(), key=lambda x: x[1], reverse=True)[:3]
            emos = ", ".join(f"{e}({v:.2f})" for e, v in top if v > 0.01)
            if emos:
                print(f"      Emociones: {emos}")

    # Tabla resumen
    print("\n" + "=" * 60)
    print("  RESUMEN")
    print("=" * 60)
    print(f"  {'#':<3} {'Polaridad':<10} {'Score':>7} {'Ironia':>7}")
    print(f"  {'--':<3} {'--------':<10} {'-----':>7} {'-----':>7}")

    for i, r in enumerate(resultados, 1):
        pol = r["polaridad"]
        score = r["score_polaridad"]
        ironia = "Si" if r["ironia"] else "No"
        print(f"  {i:<3} {pol:<10} {score:>+7.3f} {ironia:>7}")

    # Guardar JSON
    archivo = os.path.join(DIR_PROYECTO, "resultados_analisis.json")
    datos = []
    for r in resultados:
        datos.append({
            "texto": r["texto"],
            "polaridad": r["polaridad"],
            "score": r["score_polaridad"],
            "emociones": r["emociones"],
            "intensidad": r["intensidad"],
            "ironia": r["ironia"],
        })

    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)

    print(f"\n  Guardado en: {archivo}")
    print(f"  {len(TEXTOS)} textos analizados")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
