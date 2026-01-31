import pandas as pd
import numpy as np
from datetime import datetime
from renombrar import RenombradorColumnas
from filtrar import FiltradorDatos
from pivotar import PivotadorTabla
from ordenar import OrdenadorDatos
from agrupar import AgrupadorDatos
from concatenar import ConcatenadorDataFrames


def main():
    """Función principal que ejecuta todos los apartados"""
    print("\n" + "=" * 80)
    print(" " * 20 + "OPERACIONES CON DATAFRAME - ALUMNOS")
    print("=" * 80)
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    # Configuración de pandas
    pd.set_option("display.max_rows", 300)
    pd.set_option("display.max_columns", 500)
    pd.set_option("display.width", 1000)

    # Nombres de alumnos
    nombres_alumnos = [
        "Juan Pérez",
        "María López",
        "Carlos García",
        "Ana Fernández",
        "Luis Martínez",
        "Sofía Gómez",
        "Miguel Rodríguez",
        "Laura Sánchez",
        "José Torres",
        "Lucía Morales",
        "Andrés Herrera",
        "Carmen Ruiz",
        "Raúl Castro",
        "Elena Jiménez",
        "Javier Gil",
        "Isabel Romero",
        "Hugo Ortiz",
        "Sara Delgado",
        "Pablo Ramírez",
        "Marta Vargas",
    ]

    # Generar notas aleatorias (fijar semilla para reproducibilidad)
    np.random.seed(42)
    notas = {
        "Alumno": nombres_alumnos,
        "Base de Datos": np.random.uniform(1, 10, 20).round(1),
        "Programación": np.random.uniform(1, 10, 20).round(1),
        "Sistemas Informáticos": np.random.uniform(1, 10, 20).round(1),
        "Lenguajes de Marcas": np.random.uniform(1, 10, 20).round(1),
        "Entornos de Desarrollo": np.random.uniform(1, 10, 20).round(1),
    }

    # Crear DataFrame original
    df_original = pd.DataFrame(notas)

    print("\nDataFrame original:")
    print(df_original)

    # APARTADO 01: Renombrar
    renombrador = RenombradorColumnas(df_original)
    df_renombrado = renombrador.renombrar()

    # APARTADO 02: Filtrado
    filtrador = FiltradorDatos(df_renombrado)
    filtrador.ejecutar_todos()

    # APARTADO 03: Pivotar
    pivotador = PivotadorTabla(df_renombrado)
    pivotador.pivotar()

    # APARTADO 04: Ordenar
    ordenador = OrdenadorDatos(df_renombrado)
    ordenador.ejecutar_todos()

    # APARTADO 05: Agrupar
    agrupador = AgrupadorDatos(df_renombrado)
    agrupador.ejecutar_todos()

    # APARTADO 06: Concatenar
    concatenador = ConcatenadorDataFrames(df_renombrado)
    concatenador.ejecutar_todos()

    # Resumen final
    print("\n" + "=" * 80)
    print("RESUMEN FINAL")
    print("=" * 80)
    print("\n[OK] Todos los apartados completados")
    print(f"[OK] Total de alumnos: {len(df_renombrado)}")
    print("[OK] Total de asignaturas: 5")
    print("\n" + "=" * 80)
    print(" " * 30 + "FIN DEL ANÁLISIS")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
