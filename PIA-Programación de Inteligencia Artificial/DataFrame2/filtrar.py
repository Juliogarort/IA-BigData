import pandas as pd
from typing import List


class FiltradorDatos:
    """Filtra datos del DataFrame según diferentes criterios"""

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.columnas_notas = ["BD", "PR", "SI", "LM", "ED"]

    def filtrar_suspensos_alguna_materia(self) -> pd.DataFrame:
        """Filtra alumnos con al menos un suspenso (nota < 5)"""
        resultado = self.df[self.df[self.columnas_notas].lt(5).any(axis=1)]
        print(f"\nAlumnos con suspensos en alguna materia: {len(resultado)}")
        print(resultado)
        return resultado

    def filtrar_suspensos_programacion(self) -> pd.DataFrame:
        """Filtra alumnos con suspenso en Programación"""
        resultado = self.df[self.df["PR"] < 5]
        print(f"\nAlumnos con suspenso en Programación: {len(resultado)}")
        print(resultado)
        return resultado

    def filtrar_sobresalientes(self) -> dict:
        """Filtra sobresalientes (nota > 9) en cada materia"""
        resultados = {}
        print("\nSobresalientes por materia (nota > 9):")

        for materia in self.columnas_notas:
            resultado = self.df[self.df[materia] > 9]
            resultados[materia] = resultado
            print(f"\n{materia}: {len(resultado)} alumnos")
            if len(resultado) > 0:
                print(resultado[["Alumno", materia]])

        return resultados

    def filtrar_alumnos_especificos(self, nombres: List[str]) -> pd.DataFrame:
        """Filtra alumnos específicos por nombre"""
        resultado = self.df[self.df["Alumno"].isin(nombres)]
        print(f"\nAlumnos filtrados: {nombres}")
        print(resultado)
        return resultado

    def ejecutar_todos(self) -> None:
        """Ejecuta todos los filtros"""
        print("\n" + "=" * 80)
        print("APARTADO 02: FILTRADO DE DATOS")
        print("=" * 80)

        self.filtrar_suspensos_alguna_materia()
        self.filtrar_suspensos_programacion()
        self.filtrar_sobresalientes()
        self.filtrar_alumnos_especificos(["Marta Vargas", "Carmen Ruiz"])
