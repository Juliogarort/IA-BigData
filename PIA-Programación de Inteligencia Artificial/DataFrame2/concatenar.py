import pandas as pd
import numpy as np


class ConcatenadorDataFrames:
    """Concatena DataFrames con diferentes estrategias"""

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.columnas_notas = ["BD", "PR", "SI", "LM", "ED"]

    def crear_df_con_nulos(self, porcentaje_nulos: float = 0.3) -> pd.DataFrame:
        """Crea un nuevo DataFrame con valores nulos aleatorios"""
        df_nuevo = self.df.copy()

        # Introducir NaN aleatoriamente
        for col in self.columnas_notas:
            # Seleccionar índices aleatorios para poner NaN
            num_nulos = int(len(df_nuevo) * porcentaje_nulos)
            indices_nulos = np.random.choice(
                df_nuevo.index, size=num_nulos, replace=False
            )
            df_nuevo.loc[indices_nulos, col] = np.nan

        print(
            f"\nDataFrame con valores nulos (~{porcentaje_nulos * 100}% por columna):"
        )
        print(df_nuevo)
        print(f"\nNúmero de valores nulos por columna:")
        print(df_nuevo[self.columnas_notas].isnull().sum())

        return df_nuevo

    def concatenar_manteniendo_nan(self, df_nuevo: pd.DataFrame) -> pd.DataFrame:
        """Concatena DataFrames manteniendo valores NaN"""
        df_concatenado = pd.concat([self.df, df_nuevo], ignore_index=True)

        print("\nConcatenación manteniendo NaN:")
        print(f"Dimensiones: {df_concatenado.shape}")
        print(f"Total de valores nulos: {df_concatenado.isnull().sum().sum()}")
        print(df_concatenado)

        return df_concatenado

    def concatenar_eliminando_nan(self, df_nuevo: pd.DataFrame) -> pd.DataFrame:
        """Concatena DataFrames eliminando registros con NaN"""
        df_concatenado = pd.concat([self.df, df_nuevo], ignore_index=True)
        df_sin_nan = df_concatenado.dropna()

        print("\nConcatenación eliminando NaN:")
        print(f"Dimensiones antes de dropna: {df_concatenado.shape}")
        print(f"Dimensiones después de dropna: {df_sin_nan.shape}")
        print(f"Registros eliminados: {len(df_concatenado) - len(df_sin_nan)}")
        print(df_sin_nan)

        return df_sin_nan

    def ejecutar_todos(self) -> None:
        """Ejecuta todas las concatenaciones"""
        print("\n" + "=" * 80)
        print("APARTADO 06: CONCATENAR DATAFRAMES")
        print("=" * 80)

        df_nuevo = self.crear_df_con_nulos()
        self.concatenar_manteniendo_nan(df_nuevo)
        self.concatenar_eliminando_nan(df_nuevo)
