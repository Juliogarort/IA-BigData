import pandas as pd
import subprocess
import os

ARCHIVO_SALIDA = "resultados.txt"

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

def generar_consulta_prolog(fila):
    id_alumno = int(fila["id_alumno"])
    interes = str(fila["interes_tecnologia"]).strip().lower()
    trabaja = str(fila["trabaja"]).strip().lower()
    tiempo = "bajo" if float(fila["horas_estudio_semana"]) < 10 else "alto"

    consulta = f"""
    consult('reglas.pl'),
    assertz(nota_media({id_alumno}, {float(fila['nota_media'])})),
    assertz(nota_matematicas({id_alumno}, {float(fila['nota_matematicas'])})),
    assertz(nota_programacion({id_alumno}, {float(fila['nota_programacion'])})),
    assertz(interes_tecnologia({id_alumno}, {interes})),
    assertz(trabaja({id_alumno}, {trabaja})),
    assertz(tiempo_disponible({id_alumno}, {tiempo})),
    findall(R, recomendacion({id_alumno}, R), Lista),
    write(Lista),
    halt.
    """
    return consulta

def ejecutar():
    carpeta = os.path.dirname(os.path.abspath(__file__))
    os.chdir(carpeta)

    df = pd.read_csv("alumnos.csv")
    df.columns = df.columns.str.strip().str.lower()

    with open(ARCHIVO_SALIDA, "w", encoding="utf-8") as salida_txt:
        for _, fila in df.iterrows():
            id_alumno = int(fila["id_alumno"])
            consulta = generar_consulta_prolog(fila)

            proceso = subprocess.run(
                ["swipl", "-g", consulta],
                capture_output=True,
                text=True
            )

            salida = proceso.stdout.strip()

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

            if salida == "[]":
                texto += " - Sin recomendaciones\n"
            else:
                recomendaciones = [r.strip() for r in salida.replace("[", "").replace("]", "").split(",") if r.strip()]
                for r in recomendaciones:
                    texto += f" - {r}\n"
                texto += "\nExplicación:\n"
                for r in recomendaciones:
                    texto += f" - {r}: {explicar(r)}\n"

            print(texto)
            salida_txt.write(texto)

    print("\nArchivo generado:", ARCHIVO_SALIDA)

if __name__ == "__main__":
    ejecutar()