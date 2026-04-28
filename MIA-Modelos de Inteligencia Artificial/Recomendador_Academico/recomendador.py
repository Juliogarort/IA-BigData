import pandas as pd
import subprocess
import os


def generar_hechos(fila):
    """
    Convierte una fila del CSV en hechos Prolog
    """
    id_alumno = int(fila["id_alumno"])

    hechos = [
        f"nota_media({id_alumno}, {fila['nota_media']}).",
        f"nota_matematicas({id_alumno}, {fila['nota_matematicas']}).",
        f"nota_programacion({id_alumno}, {fila['nota_programacion']}).",
        f"interes_tecnologia({id_alumno}, {fila['interes_tecnologia']}).",
        f"trabaja({id_alumno}, {fila['trabaja']}).",
        f"tiempo_disponible({id_alumno}, {'bajo' if fila['horas_estudio_semana'] < 10 else 'alto'})."
    ]

    return hechos


def ejecutar_sistema():

    # Ir a carpeta del script
    carpeta = os.path.dirname(os.path.abspath(__file__))
    os.chdir(carpeta)

    # Verificar CSV
    if not os.path.exists("alumnos.csv"):
        print("ERROR: No existe alumnos.csv")
        return

    try:
        df = pd.read_csv("alumnos.csv")
    except Exception as e:
        print("Error leyendo CSV:", e)
        return

    print("CSV cargado correctamente")
    print("Columnas detectadas:", df.columns.tolist())

    # Procesar alumnos
    for _, fila in df.iterrows():

        id_alumno = int(fila["id_alumno"])

        # Crear hechos
        hechos = generar_hechos(fila)

        # Guardar archivo temporal
        with open("hechos_temp.pl", "w", encoding="utf-8") as f:
            f.write("\n".join(hechos))

        # Consulta Prolog
        consulta = f"""
        consult('reglas.pl'),
        consult('hechos_temp.pl'),
        findall(R, recomendacion({id_alumno}, R), Lista),
        write(Lista),
        halt.
        """

        try:
            proceso = subprocess.run(
                ["swipl", "-g", consulta],
                capture_output=True,
                text=True
            )

            salida = proceso.stdout.strip()
            error = proceso.stderr.strip()

            print("====================================")
            print(f"Alumno: {id_alumno}")
            print("Datos:")
            print(f" - Nota media: {fila['nota_media']}")
            print(f" - Matemáticas: {fila['nota_matematicas']}")
            print(f" - Programación: {fila['nota_programacion']}")
            print(f" - Interés tecnología: {fila['interes_tecnologia']}")
            print(f" - Trabaja: {fila['trabaja']}")
            print(f" - Horas estudio: {fila['horas_estudio_semana']}")

            print("\nRecomendaciones:")

            if salida == "[]":
                print(" - Sin recomendaciones")
            else:
                recomendaciones = salida.replace("[", "").replace("]", "").split(",")

                for r in recomendaciones:
                    print(" -", r.strip())

            if error:
                print("\nErrores Prolog:")
                print(error)

        except FileNotFoundError:
            print("ERROR: SWI-Prolog no está instalado o no está en PATH.")
            return


if __name__ == "__main__":
    ejecutar_sistema()