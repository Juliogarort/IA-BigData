import pandas as pd
from typing import Dict


class AnalizadorEstadistico:
    """Realiza análisis estadísticos sobre los datos"""
    
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.estadisticas: Dict = {}
    
    def analizar_todo(self) -> Dict:
        """Ejecuta todos los análisis estadísticos"""
        print("\n" + "=" * 80)
        print("ANALISIS ESTADISTICO")
        print("=" * 80)
        
        self._analizar_precio()
        self._analizar_kilometraje()
        self._analizar_emisiones()
        self._analizar_autonomia()
        self._analizar_distribuciones()
        
        return self.estadisticas
    
    def _analizar_precio(self) -> None:
        """Analiza estadísticas de precio"""
        print("\n--- PRECIO ---")
        self.estadisticas['Precio'] = {
            'Promedio': self.df['Precio'].mean(),
            'Mediana': self.df['Precio'].median(),
            'Min': self.df['Precio'].min(),
            'Max': self.df['Precio'].max(),
            'Desviacion': self.df['Precio'].std()
        }
        
        for key, value in self.estadisticas['Precio'].items():
            print(f"{key}: {value:.2f} EUR")
    
    def _analizar_kilometraje(self) -> None:
        """Analiza estadísticas de kilometraje"""
        print("\n--- KILOMETRAJE ---")
        self.estadisticas['Kilometros'] = {
            'Promedio': self.df['Kilómetros'].mean(),
            'Mediana': self.df['Kilómetros'].median(),
            'Min': self.df['Kilómetros'].min(),
            'Max': self.df['Kilómetros'].max()
        }
        
        for key, value in self.estadisticas['Kilometros'].items():
            print(f"{key}: {value:.0f} km")
    
    def _analizar_emisiones(self) -> None:
        """Analiza estadísticas de emisiones"""
        print("\n--- EMISIONES CO2 ---")
        self.estadisticas['Emisiones'] = {
            'Promedio': self.df['Emisiones'].mean(),
            'Mediana': self.df['Emisiones'].median()
        }
        
        for key, value in self.estadisticas['Emisiones'].items():
            print(f"{key}: {value:.2f} g/km")
    
    def _analizar_autonomia(self) -> None:
        """Analiza estadísticas de autonomía"""
        print("\n--- AUTONOMIA ---")
        self.estadisticas['Autonomia'] = {
            'Promedio': self.df['Autonomía'].mean(),
            'Mediana': self.df['Autonomía'].median()
        }
        
        for key, value in self.estadisticas['Autonomia'].items():
            print(f"{key}: {value:.0f} km")
    
    def _analizar_distribuciones(self) -> None:
        """Analiza distribuciones por categorías"""
        print("\n--- DISTRIBUCIONES ---")
        
        # Por marca
        dist_marca = self.df['Marca'].value_counts()
        self.estadisticas['Distribucion_Marca'] = dist_marca.to_dict()
        print("\nPor Marca:")
        print(dist_marca)
        
        # Por combustible
        dist_combustible = self.df['Combustible'].value_counts()
        self.estadisticas['Distribucion_Combustible'] = dist_combustible.to_dict()
        print("\nPor Combustible:")
        print(dist_combustible)
        
        # Precio promedio por marca
        precio_marca = self.df.groupby('Marca')['Precio'].mean().sort_values(ascending=False)
        self.estadisticas['Precio_Promedio_Marca'] = precio_marca.to_dict()
        print("\nPrecio Promedio por Marca:")
        for marca, precio in precio_marca.items():
            print(f"  {marca}: {precio:.2f} EUR")
