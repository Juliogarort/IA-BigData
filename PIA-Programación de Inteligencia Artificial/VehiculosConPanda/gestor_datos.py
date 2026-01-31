import pandas as pd
from typing import Optional


class GestorDatos:
    """Maneja la carga, verificación y procesamiento de datos"""

    def __init__(self, archivo: str):
        self.archivo = archivo
        self.df: Optional[pd.DataFrame] = None
        self.df_procesado: Optional[pd.DataFrame] = None

    def cargar(self) -> bool:
        """Carga los datos desde el archivo Excel"""
        print("=" * 80)
        print("CARGANDO DATOS DE VEHICULOS")
        print("=" * 80)

        try:
            self.df = pd.read_excel(self.archivo, engine="openpyxl")
            print(f"\n[OK] Datos cargados: {len(self.df)} registros")
            return True
        except FileNotFoundError:
            print(f"\n[ERROR] Archivo '{self.archivo}' no encontrado")
            return False
        except Exception as e:
            print(f"\n[ERROR] {e}")
            return False

    def verificar(self) -> None:
        """Verifica la integridad de los datos"""
        if self.df is None:
            print("[ERROR] No hay datos cargados")
            return

        print("\n" + "=" * 80)
        print("VERIFICACION DE DATOS")
        print("=" * 80)

        print(f"\nRegistros: {len(self.df)}")
        print(f"\nColumnas ({len(self.df.columns)}):")
        for i, col in enumerate(self.df.columns, 1):
            print(f"  {i}. {col}")

        print("\nValores nulos:")
        nulos = self.df.isnull().sum()
        for col, count in nulos.items():
            if count > 0:
                porcentaje = (count / len(self.df)) * 100
                print(f"  {col}: {count} ({porcentaje:.1f}%)")

    def procesar_nulos(self) -> None:
        """Procesa valores nulos con estrategias específicas"""
        if self.df is None:
            return

        print("\n" + "=" * 80)
        print("PROCESAMIENTO DE VALORES NULOS")
        print("=" * 80)

        self.df_procesado = self.df.copy()

        # Kilómetros: mediana por año
        if self.df_procesado["Kilómetros"].isnull().any():
            for anyo in self.df_procesado["Anyo"].unique():
                mediana = self.df_procesado[self.df_procesado["Anyo"] == anyo][
                    "Kilómetros"
                ].median()
                mask = (self.df_procesado["Anyo"] == anyo) & (
                    self.df_procesado["Kilómetros"].isnull()
                )
                self.df_procesado.loc[mask, "Kilómetros"] = mediana
            print("  [OK] Kilómetros: rellenados con mediana por año")

        # Capacidad maletero: media
        if self.df_procesado["C_Maletero"].isnull().any():
            media = self.df_procesado["C_Maletero"].mean()
            self.df_procesado["C_Maletero"] = self.df_procesado["C_Maletero"].fillna(
                media
            )
            print(f"  [OK] C_Maletero: rellenado con media ({media:.0f} L)")

        # Emisiones: media por combustible
        if self.df_procesado["Emisiones"].isnull().any():
            for combustible in self.df_procesado["Combustible"].unique():
                media = self.df_procesado[
                    self.df_procesado["Combustible"] == combustible
                ]["Emisiones"].mean()
                mask = (self.df_procesado["Combustible"] == combustible) & (
                    self.df_procesado["Emisiones"].isnull()
                )
                self.df_procesado.loc[mask, "Emisiones"] = media
            print("  [OK] Emisiones: rellenadas con media por combustible")

        # Autonomía: mediana por combustible
        if self.df_procesado["Autonomía"].isnull().any():
            for combustible in self.df_procesado["Combustible"].unique():
                mediana = self.df_procesado[
                    self.df_procesado["Combustible"] == combustible
                ]["Autonomía"].median()
                mask = (self.df_procesado["Combustible"] == combustible) & (
                    self.df_procesado["Autonomía"].isnull()
                )
                self.df_procesado.loc[mask, "Autonomía"] = mediana
            print("  [OK] Autonomía: rellenada con mediana por combustible")

        nulos_restantes = self.df_procesado.isnull().sum().sum()
        print(f"\n[OK] Nulos restantes: {nulos_restantes}")

    def obtener_datos(self) -> Optional[pd.DataFrame]:
        """Retorna el DataFrame procesado o el original"""
        return self.df_procesado if self.df_procesado is not None else self.df
