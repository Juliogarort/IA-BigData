import pandas as pd


class PivotadorTabla:
    """Pivota el DataFrame de formato ancho a largo"""

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.columnas_notas = ["BD", "PR", "SI", "LM", "ED"]

    def pivotar(self) -> pd.DataFrame:
        """Pivota la tabla creando una columna 'Asignatura'"""
        print("\n" + "=" * 80)
        print("APARTADO 03: PIVOTAR TABLA")
        print("=" * 80)

        # Usar melt para transformar de formato ancho a largo
        df_pivotado = pd.melt(
            self.df,
            id_vars=["Alumno"],
            value_vars=self.columnas_notas,
            var_name="Asignatura",
            value_name="Nota",
        )

        print("\nFormato original (ancho):")
        print(f"Dimensiones: {self.df.shape}")
        print(self.df.head())

        print("\nFormato pivotado (largo):")
        print(f"Dimensiones: {df_pivotado.shape}")
        print(df_pivotado.head(15))

        return df_pivotado
