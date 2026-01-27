import pandas as pd


class TransformadorDatos:
    """Aplica transformaciones y cálculos sobre los datos"""
    
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.anyo_actual = 2026
    
    def calcular_depreciacion(self) -> pd.DataFrame:
        """Calcula depreciación de vehículos"""
        print("\n" + "=" * 80)
        print("CALCULANDO DEPRECIACION")
        print("=" * 80)
        
        df_trans = self.df.copy()
        
        # Edad y depreciación
        df_trans['Edad'] = self.anyo_actual - df_trans['Anyo']
        df_trans['Depreciacion_Edad'] = df_trans['Edad'] * 0.15
        df_trans['Depreciacion_Kilometros'] = (df_trans['Kilómetros'] / 100000) * 0.10
        df_trans['Depreciacion_Total'] = (
            df_trans['Depreciacion_Edad'] + df_trans['Depreciacion_Kilometros']
        ).clip(upper=0.90)
        
        # Valores
        df_trans['Valor_Estimado'] = (
            df_trans['Precio'] * (1 - df_trans['Depreciacion_Total'])
        ).round(2)
        df_trans['Perdida_Valor'] = (df_trans['Precio'] - df_trans['Valor_Estimado']).round(2)
        
        print("[OK] Depreciación calculada")
        print("\nEjemplos:")
        print(df_trans[['Marca', 'Modelo', 'Anyo', 'Edad', 'Precio', 'Valor_Estimado']].head())
        
        return df_trans
    
    def calcular_coste_por_km(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calcula coste por kilómetro"""
        df_trans = df.copy()
        df_trans['Coste_Por_Km'] = (
            df_trans['Precio'] / df_trans['Kilómetros'].replace(0, 1)
        ).round(2)
        print("[OK] Coste por km calculado")
        return df_trans
    
    def clasificar_por_precio(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clasifica vehículos por categoría de precio"""
        df_trans = df.copy()
        
        def categorizar(precio):
            if precio < 15000: return 'Economico'
            elif precio < 25000: return 'Medio'
            elif precio < 35000: return 'Premium'
            else: return 'Lujo'
        
        df_trans['Categoria_Precio'] = df_trans['Precio'].apply(categorizar)
        print("[OK] Clasificación por precio")
        print("\nDistribución:")
        print(df_trans['Categoria_Precio'].value_counts())
        return df_trans
    
    def clasificar_por_emisiones(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clasifica vehículos por etiqueta ambiental"""
        df_trans = df.copy()
        
        def etiqueta(row):
            if row['Combustible'] == 'Eléctrico': return 'CERO'
            elif row['Combustible'] in ['Híbrido', 'Híbrido Enchufable']: return 'ECO'
            elif row['Emisiones'] < 120: return 'C'
            elif row['Emisiones'] < 160: return 'B'
            else: return 'SIN ETIQUETA'
        
        df_trans['Etiqueta_Ambiental'] = df_trans.apply(etiqueta, axis=1)
        print("[OK] Etiquetas ambientales")
        print("\nDistribución:")
        print(df_trans['Etiqueta_Ambiental'].value_counts())
        return df_trans
    
    def aplicar_todas(self) -> pd.DataFrame:
        """Aplica todas las transformaciones"""
        print("\n" + "=" * 80)
        print("APLICANDO TODAS LAS TRANSFORMACIONES")
        print("=" * 80)
        
        df_result = self.calcular_depreciacion()
        df_result = self.calcular_coste_por_km(df_result)
        df_result = self.clasificar_por_precio(df_result)
        df_result = self.clasificar_por_emisiones(df_result)
        
        print("\n[OK] Todas las transformaciones aplicadas")
        return df_result