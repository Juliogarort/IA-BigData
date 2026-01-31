import pandas as pd


class AgrupadorDatos:
    """Agrupa y calcula estadísticas del DataFrame"""

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.columnas_notas = ["BD", "PR", "SI", "LM", "ED"]

    def promedio_por_alumno(self) -> pd.Series:
        """Calcula el promedio de notas de cada alumno"""
        promedios = self.df[self.columnas_notas].mean(axis=1)
        df_con_promedio = self.df.copy()
        df_con_promedio["Promedio"] = promedios.round(2)

        print("\nPromedio de notas por alumno:")
        print(
            df_con_promedio[["Alumno", "Promedio"]].sort_values(
                "Promedio", ascending=False
            )
        )

        return promedios

    def promedio_por_materia(self) -> pd.Series:
        """Calcula el promedio de notas de cada materia"""
        promedios = self.df[self.columnas_notas].mean()

        print("\nPromedio de notas por materia:")
        for materia, promedio in promedios.items():
            print(f"  {materia}: {promedio:.2f}")

        return promedios

    def mejor_alumno(self) -> str:
        """Identifica el alumno con mejor promedio"""
        promedios = self.df[self.columnas_notas].mean(axis=1)
        indice_mejor = promedios.idxmax()
        mejor_alumno = self.df.loc[indice_mejor, "Alumno"]
        mejor_promedio = promedios[indice_mejor]

        print("\nAlumno con mejor promedio:")
        print(f"  {mejor_alumno}: {mejor_promedio:.2f}")
        print(f"\nNotas de {mejor_alumno}:")
        print(self.df.loc[indice_mejor, self.columnas_notas])

        return mejor_alumno

    def ejecutar_todos(self) -> None:
        """Ejecuta todas las agrupaciones"""
        print("\n" + "=" * 80)
        print("APARTADO 05: AGRUPAR DATOS")
        print("=" * 80)

        self.promedio_por_alumno()
        self.promedio_por_materia()
        self.mejor_alumno()
