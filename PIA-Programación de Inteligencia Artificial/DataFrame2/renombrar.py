import pandas as pd
from typing import List


class RenombradorColumnas:
    """Renombra las columnas del DataFrame"""

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.mapeo = {
            "Base de Datos": "BD",
            "Programación": "PR",
            "Sistemas Informáticos": "SI",
            "Lenguajes de Marcas": "LM",
            "Entornos de Desarrollo": "ED",
        }

    def renombrar(self) -> pd.DataFrame:
        """Renombra las columnas según el mapeo definido"""
        print("\n" + "=" * 80)
        print("APARTADO 01: RENOMBRAR COLUMNAS")
        print("=" * 80)

        df_renombrado = self.df.rename(columns=self.mapeo)

        print("\nColumnas originales:")
        print(list(self.df.columns))
        print("\nColumnas renombradas:")
        print(list(df_renombrado.columns))
        print("\nDataFrame renombrado:")
        print(df_renombrado)

        return df_renombrado
