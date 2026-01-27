import pandas as pd
from typing import Optional


class FiltradorDatos:
    """Aplica filtros y ordenamientos sobre los datos"""
    
    def __init__(self, df: pd.DataFrame):
        self.df = df
    
    # MÉTODOS DE FILTRADO
    def por_marca(self, marca: str) -> pd.DataFrame:
        """Filtra por marca"""
        resultado = self.df[self.df['Marca'] == marca]
        print(f"Filtro por marca '{marca}': {len(resultado)} vehículos")
        return resultado
    
    def por_modelo(self, modelo: str) -> pd.DataFrame:
        """Filtra por modelo"""
        resultado = self.df[self.df['Modelo'] == modelo]
        print(f"Filtro por modelo '{modelo}': {len(resultado)} vehículos")
        return resultado
    
    def por_anyo(self, anyo_min: int, anyo_max: Optional[int] = None) -> pd.DataFrame:
        """Filtra por año o rango de años"""
        if anyo_max is None:
            resultado = self.df[self.df['Anyo'] == anyo_min]
            print(f"Filtro por año {anyo_min}: {len(resultado)} vehículos")
        else:
            resultado = self.df[(self.df['Anyo'] >= anyo_min) & (self.df['Anyo'] <= anyo_max)]
            print(f"Filtro por rango {anyo_min}-{anyo_max}: {len(resultado)} vehículos")
        return resultado
    
    def por_precio(self, precio_min: float, precio_max: float) -> pd.DataFrame:
        """Filtra por rango de precio"""
        resultado = self.df[(self.df['Precio'] >= precio_min) & (self.df['Precio'] <= precio_max)]
        print(f"Filtro por precio {precio_min}-{precio_max} EUR: {len(resultado)} vehículos")
        return resultado
    
    def por_combustible(self, combustible: str) -> pd.DataFrame:
        """Filtra por tipo de combustible"""
        resultado = self.df[self.df['Combustible'] == combustible]
        print(f"Filtro por combustible '{combustible}': {len(resultado)} vehículos")
        return resultado
    
    def por_color(self, color: str) -> pd.DataFrame:
        """Filtra por color"""
        resultado = self.df[self.df['Color'] == color]
        print(f"Filtro por color '{color}': {len(resultado)} vehículos")
        return resultado
    
    # MÉTODOS DE ORDENAMIENTO
    def ordenar_por_precio(self, ascendente: bool = True) -> pd.DataFrame:
        """Ordena por precio"""
        orden = "ascendente" if ascendente else "descendente"
        print(f"Ordenando por precio ({orden})...")
        return self.df.sort_values('Precio', ascending=ascendente)
    
    def ordenar_por_anyo(self, ascendente: bool = False) -> pd.DataFrame:
        """Ordena por año"""
        orden = "ascendente" if ascendente else "descendente"
        print(f"Ordenando por año ({orden})...")
        return self.df.sort_values('Anyo', ascending=ascendente)
    
    def ordenar_por_kilometros(self, ascendente: bool = True) -> pd.DataFrame:
        """Ordena por kilómetros"""
        orden = "ascendente" if ascendente else "descendente"
        print(f"Ordenando por kilómetros ({orden})...")
        return self.df.sort_values('Kilómetros', ascending=ascendente)
    
    def ordenar_por_emisiones(self, ascendente: bool = True) -> pd.DataFrame:
        """Ordena por emisiones"""
        orden = "ascendente" if ascendente else "descendente"
        print(f"Ordenando por emisiones ({orden})...")
        return self.df.sort_values('Emisiones', ascending=ascendente)
    
    # EJEMPLOS DE USO
    def mostrar_ejemplos(self) -> None:
        """Muestra ejemplos de filtrado y ordenamiento"""
        print("\n" + "=" * 80)
        print("EJEMPLOS DE FILTRADO Y ORDENAMIENTO")
        print("=" * 80)
        
        print("\n1. Vehículos SEAT:")
        seat = self.por_marca('SEAT')
        print(seat[['Marca', 'Modelo', 'Anyo', 'Precio']].head())
        
        print("\n2. Vehículos 2023:")
        anyo_2023 = self.por_anyo(2023)
        print(anyo_2023[['Marca', 'Modelo', 'Anyo', 'Precio']].head())
        
        print("\n3. Precio 15000-20000 EUR:")
        rango = self.por_precio(15000, 20000)
        print(rango[['Marca', 'Modelo', 'Precio']].head())
        
        print("\n4. Vehículos más baratos:")
        baratos = self.ordenar_por_precio(ascendente=True)
        print(baratos[['Marca', 'Modelo', 'Precio']].head())
        
        print("\n5. Vehículos más ecológicos:")
        ecologicos = self.ordenar_por_emisiones(ascendente=True)
        print(ecologicos[['Marca', 'Modelo', 'Combustible', 'Emisiones']].head())

