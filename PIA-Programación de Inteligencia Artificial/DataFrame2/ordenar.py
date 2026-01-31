import pandas as pd


class OrdenadorDatos:
    """Ordena el DataFrame según diferentes criterios"""

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def ordenar_por_nombre(self) -> pd.DataFrame:
        """Ordena por nombre de alumno alfabéticamente"""
        resultado = self.df.sort_values("Alumno")
        print("\nOrdenado por nombre de alumno:")
        print(resultado)
        return resultado

    def ordenar_por_programacion_asc(self) -> pd.DataFrame:
        """Ordena por nota de Programación ascendente"""
        resultado = self.df.sort_values("PR", ascending=True)
        print("\nOrdenado por Programación (ascendente):")
        print(resultado[["Alumno", "PR"]])
        return resultado

    def ordenar_por_bd_desc(self) -> pd.DataFrame:
        """Ordena por nota de Base de Datos descendente"""
        resultado = self.df.sort_values("BD", ascending=False)
        print("\nOrdenado por Base de Datos (descendente):")
        print(resultado[["Alumno", "BD"]])
        return resultado

    def ejecutar_todos(self) -> None:
        """Ejecuta todos los ordenamientos"""
        print("\n" + "=" * 80)
        print("APARTADO 04: ORDENAR DATOS")
        print("=" * 80)

        self.ordenar_por_nombre()
        self.ordenar_por_programacion_asc()
        self.ordenar_por_bd_desc()
