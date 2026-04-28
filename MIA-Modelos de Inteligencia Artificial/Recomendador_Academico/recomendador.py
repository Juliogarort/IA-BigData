import pandas as pd
import subprocess
import os

ARCHIVO_SALIDA = "resultados.txt"


def generar_hechos(fila):

    id_alumno = int(fila["id_alumno"])

    return [
        f"nota_media({id_alumno}, {fila['nota_media']}).",
        f"nota_matematicas({id_alumno}, {fila['nota_matematicas']}).",
        f"nota_programacion({id_alumno}, {fila['nota_programacion']}).",
        f"interes_tecnologia({id_alumno}, {fila['interes_tecnologia']}).",
        f"trabaja({id_alumno}, {fila['trabaja']}).",
        f"tiempo_disponible({id_alumno}, {'bajo' if fila['horas_estudio_semana'] < 10 else 'alto'})."
    ]


def explicar(rec):

    explicaciones = {
        "refuerzo_academico": "nota media inferior a 5",
        "refuerzo_matematicas": "nota matemáticas inferior a 5",
        "itinerario_tecnico": "interés tecnología y programación alta",
        "carga_reducida": "trabaja y poco tiempo disponible",
        "carga_intensiva": "nota alta y mucho tiempo disponible",
        "itinerario_general": "rendimiento medio general"
    }

    return explicaciones.get(rec, "sin explicación")


def ejecutar():

    carpeta = os.path.dirname(os.path.abspath(__file__))
    os.chdir(carpeta)

    df = pd.read_csv("alumnos.csv")

    with open(ARCHIVO_SALIDA, "w", encoding="utf-8") as salida_txt:

        for _, fila in df.iterrows():

            id_alumno = int(fila["id_alumno"])

            hechos = generar_hechos(fila)

            with open("hechos_temp.pl", "w", encoding="utf-8") as f:
                f.write("\n".join(hechos))

            consulta = f"""
            consult('reglas.pl'),
            consult('hechos_temp.pl'),
            findall(R, recomendacion({id_alumno},R), Lista),
            write(Lista),
            halt.
            """

            proceso = subprocess.run(
                ["swipl", "-g", consulta],
                capture_output=True,
                text=True
            )

            texto = "\n====================================\n"
            texto += f"Alumno: {id_alumno}\n"
            texto += "Datos:\n"
            texto += f" - Nota media: {fila['nota_media']}\n"
            texto += f" - Matemáticas: {fila['nota_matematicas']}\n"
            texto += f" - Programación: {fila['nota_programacion']}\n"
            texto += f" - Interés tecnología: {fila['interes_tecnologia']}\n"
            texto += f" - Trabaja: {fila['trabaja']}\n"
            texto += f" - Horas estudio: {fila['horas_estudio_semana']}\n"

            texto += "\nRecomendaciones:\n"

            salida = proceso.stdout.strip()

            if salida == "[]":
                texto += " - Sin recomendaciones\n"

            else:
                recomendaciones = salida.replace("[", "").replace("]", "").split(",")

                for r in recomendaciones:
                    rec = r.strip()
                    texto += f" - {rec}\n"

                texto += "\nExplicación:\n"

                for r in recomendaciones:
                    rec = r.strip()
                    texto += f" - {rec}: {explicar(rec)}\n"

            print(texto)
            salida_txt.write(texto)

    print("\nArchivo generado:", ARCHIVO_SALIDA)


if __name__ == "__main__":
    ejecutar()