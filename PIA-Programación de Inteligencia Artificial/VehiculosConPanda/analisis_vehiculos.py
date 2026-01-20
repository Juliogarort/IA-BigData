"""
Análisis de Datos de Vehículos del Mercado Español
Autor: Julio García Ortiz
Descripción: Script completo para análisis de datos de vehículos usando pandas
"""

import pandas as pd
import numpy as np
from datetime import datetime

# ============================================================================
# SECCIÓN 1: CARGA Y PROCESAMIENTO DE DATOS
# ============================================================================

def cargar_datos_vehiculos(archivo_excel):
    """
    Carga los datos de vehículos desde un archivo Excel
    
    Args:
        archivo_excel (str): Ruta del archivo Excel con los datos
        
    Returns:
        pd.DataFrame: DataFrame con los datos cargados
    """
    print("=" * 80)
    print("CARGANDO DATOS DE VEHICULOS")
    print("=" * 80)
    
    try:
        # Cargar datos desde Excel
        df = pd.read_excel(archivo_excel, engine='openpyxl')
        print(f"\n[OK] Datos cargados correctamente desde '{archivo_excel}'")
        print(f"[OK] Total de registros cargados: {len(df)}")
        
        return df
    except FileNotFoundError:
        print(f"\n[ERROR] No se encontro el archivo '{archivo_excel}'")
        return None
    except Exception as e:
        print(f"\n[ERROR] Error al cargar datos: {e}")
        return None


def verificar_datos(df):
    """
    Verifica la integridad de los datos cargados
    Comprueba el número de registros, columnas y tipos de datos
    
    Args:
        df (pd.DataFrame): DataFrame a verificar
    """
    print("\n" + "=" * 80)
    print("VERIFICACION DE DATOS")
    print("=" * 80)
    
    # Verificar número de registros
    print(f"\nNumero total de registros: {len(df)}")
    
    # Verificar columnas
    print(f"\nColumnas presentes ({len(df.columns)}):")
    for i, col in enumerate(df.columns, 1):
        print(f"  {i}. {col}")
    
    # Información general del DataFrame
    print("\nInformacion del DataFrame:")
    print(df.info())
    
    # Valores nulos por columna
    print("\nValores nulos por columna:")
    nulos = df.isnull().sum()
    for col, count in nulos.items():
        porcentaje = (count / len(df)) * 100
        print(f"  {col}: {count} ({porcentaje:.1f}%)")


def procesar_valores_nulos(df):
    """
    Procesa y transforma los valores nulos del DataFrame
    Aplica diferentes estrategias según el tipo de columna
    
    Args:
        df (pd.DataFrame): DataFrame con valores nulos
        
    Returns:
        pd.DataFrame: DataFrame con valores nulos procesados
    """
    print("\n" + "=" * 80)
    print("PROCESAMIENTO DE VALORES NULOS")
    print("=" * 80)
    
    df_procesado = df.copy()
    
    # Kilometros: rellenar con la mediana según el año
    if df_procesado['Kilómetros'].isnull().any():
        print("\nProcesando 'Kilometros'...")
        for anyo in df_procesado['Anyo'].unique():
            mediana_km = df_procesado[df_procesado['Anyo'] == anyo]['Kilómetros'].median()
            mask = (df_procesado['Anyo'] == anyo) & (df_procesado['Kilómetros'].isnull())
            df_procesado.loc[mask, 'Kilómetros'] = mediana_km
        print(f"  [OK] Valores nulos rellenados con mediana por año")
    
    # Capacidad maletero: rellenar con la media
    if df_procesado['C_Maletero'].isnull().any():
        print("\nProcesando 'C_Maletero'...")
        media_maletero = df_procesado['C_Maletero'].mean()
        df_procesado['C_Maletero'].fillna(media_maletero, inplace=True)
        print(f"  [OK] Valores nulos rellenados con media: {media_maletero:.0f} litros")
    
    # Emisiones: rellenar con la media según tipo de combustible
    if df_procesado['Emisiones'].isnull().any():
        print("\nProcesando 'Emisiones'...")
        for combustible in df_procesado['Combustible'].unique():
            media_emisiones = df_procesado[df_procesado['Combustible'] == combustible]['Emisiones'].mean()
            mask = (df_procesado['Combustible'] == combustible) & (df_procesado['Emisiones'].isnull())
            df_procesado.loc[mask, 'Emisiones'] = media_emisiones
        print(f"  [OK] Valores nulos rellenados con media por tipo de combustible")
    
    # Autonomía: rellenar con la mediana según tipo de combustible
    if df_procesado['Autonomía'].isnull().any():
        print("\nProcesando 'Autonomia'...")
        for combustible in df_procesado['Combustible'].unique():
            mediana_autonomia = df_procesado[df_procesado['Combustible'] == combustible]['Autonomía'].median()
            mask = (df_procesado['Combustible'] == combustible) & (df_procesado['Autonomía'].isnull())
            df_procesado.loc[mask, 'Autonomía'] = mediana_autonomia
        print(f"  [OK] Valores nulos rellenados con mediana por tipo de combustible")
    
    # Verificar que no quedan nulos
    nulos_restantes = df_procesado.isnull().sum().sum()
    print(f"\n[OK] Procesamiento completado. Valores nulos restantes: {nulos_restantes}")
    
    return df_procesado


# ============================================================================
# SECCIÓN 2: ANÁLISIS ESTADÍSTICO
# ============================================================================

def analisis_estadistico(df):
    """
    Genera un análisis estadístico completo de los datos
    Calcula promedios, medianas, desviaciones y otros indicadores
    
    Args:
        df (pd.DataFrame): DataFrame con los datos de vehículos
        
    Returns:
        dict: Diccionario con las estadísticas calculadas
    """
    print("\n" + "=" * 80)
    print("ANALISIS ESTADISTICO")
    print("=" * 80)
    
    estadisticas = {}
    
    # Estadísticas de precio
    print("\n--- ESTADISTICAS DE PRECIO ---")
    estadisticas['Precio_Promedio'] = df['Precio'].mean()
    estadisticas['Precio_Mediana'] = df['Precio'].median()
    estadisticas['Precio_Min'] = df['Precio'].min()
    estadisticas['Precio_Max'] = df['Precio'].max()
    estadisticas['Precio_Desviacion'] = df['Precio'].std()
    
    print(f"Promedio: {estadisticas['Precio_Promedio']:.2f} EUR")
    print(f"Mediana: {estadisticas['Precio_Mediana']:.2f} EUR")
    print(f"Minimo: {estadisticas['Precio_Min']:.2f} EUR")
    print(f"Maximo: {estadisticas['Precio_Max']:.2f} EUR")
    print(f"Desviacion estandar: {estadisticas['Precio_Desviacion']:.2f} EUR")
    
    # Estadísticas de kilometraje
    print("\n--- ESTADISTICAS DE KILOMETRAJE ---")
    estadisticas['Kilometros_Promedio'] = df['Kilómetros'].mean()
    estadisticas['Kilometros_Mediana'] = df['Kilómetros'].median()
    estadisticas['Kilometros_Min'] = df['Kilómetros'].min()
    estadisticas['Kilometros_Max'] = df['Kilómetros'].max()
    
    print(f"Promedio: {estadisticas['Kilometros_Promedio']:.0f} km")
    print(f"Mediana: {estadisticas['Kilometros_Mediana']:.0f} km")
    print(f"Minimo: {estadisticas['Kilometros_Min']:.0f} km")
    print(f"Maximo: {estadisticas['Kilometros_Max']:.0f} km")
    
    # Estadísticas de emisiones
    print("\n--- ESTADISTICAS DE EMISIONES CO2 ---")
    estadisticas['Emisiones_Promedio'] = df['Emisiones'].mean()
    estadisticas['Emisiones_Mediana'] = df['Emisiones'].median()
    
    print(f"Promedio: {estadisticas['Emisiones_Promedio']:.2f} g/km")
    print(f"Mediana: {estadisticas['Emisiones_Mediana']:.2f} g/km")
    
    # Estadísticas de autonomía
    print("\n--- ESTADISTICAS DE AUTONOMIA ---")
    estadisticas['Autonomia_Promedio'] = df['Autonomía'].mean()
    estadisticas['Autonomia_Mediana'] = df['Autonomía'].median()
    
    print(f"Promedio: {estadisticas['Autonomia_Promedio']:.0f} km")
    print(f"Mediana: {estadisticas['Autonomia_Mediana']:.0f} km")
    
    # Distribución por marca
    print("\n--- DISTRIBUCION POR MARCA ---")
    dist_marca = df['Marca'].value_counts()
    estadisticas['Distribucion_Marca'] = dist_marca.to_dict()
    print(dist_marca)
    
    # Distribución por tipo de combustible
    print("\n--- DISTRIBUCION POR TIPO DE COMBUSTIBLE ---")
    dist_combustible = df['Combustible'].value_counts()
    estadisticas['Distribucion_Combustible'] = dist_combustible.to_dict()
    print(dist_combustible)
    
    # Distribución por año
    print("\n--- DISTRIBUCION POR AÑO ---")
    dist_anyo = df['Anyo'].value_counts().sort_index()
    estadisticas['Distribucion_Anyo'] = dist_anyo.to_dict()
    print(dist_anyo)
    
    # Precio promedio por marca
    print("\n--- PRECIO PROMEDIO POR MARCA ---")
    precio_marca = df.groupby('Marca')['Precio'].mean().sort_values(ascending=False)
    estadisticas['Precio_Promedio_Marca'] = precio_marca.to_dict()
    for marca, precio in precio_marca.items():
        print(f"{marca}: {precio:.2f} EUR")
    
    return estadisticas


def exportar_estadisticas(estadisticas, df, archivo_salida='estadisticas_vehiculos.xlsx'):
    """
    Exporta las estadísticas a un archivo Excel
    
    Args:
        estadisticas (dict): Diccionario con estadísticas
        df (pd.DataFrame): DataFrame original
        archivo_salida (str): Nombre del archivo de salida
    """
    print("\n" + "=" * 80)
    print("EXPORTANDO ESTADISTICAS")
    print("=" * 80)
    
    # Crear un ExcelWriter
    with pd.ExcelWriter(archivo_salida, engine='openpyxl') as writer:
        
        # Hoja 1: Resumen estadístico
        resumen = pd.DataFrame({
            'Metrica': [
                'Precio Promedio (EUR)',
                'Precio Mediana (EUR)',
                'Precio Minimo (EUR)',
                'Precio Maximo (EUR)',
                'Kilometros Promedio',
                'Kilometros Mediana',
                'Emisiones Promedio (g/km)',
                'Autonomia Promedio (km)'
            ],
            'Valor': [
                f"{estadisticas['Precio_Promedio']:.2f}",
                f"{estadisticas['Precio_Mediana']:.2f}",
                f"{estadisticas['Precio_Min']:.2f}",
                f"{estadisticas['Precio_Max']:.2f}",
                f"{estadisticas['Kilometros_Promedio']:.0f}",
                f"{estadisticas['Kilometros_Mediana']:.0f}",
                f"{estadisticas['Emisiones_Promedio']:.2f}",
                f"{estadisticas['Autonomia_Promedio']:.0f}"
            ]
        })
        resumen.to_excel(writer, sheet_name='Resumen', index=False)
        
        # Hoja 2: Distribución por marca
        df_marca = pd.DataFrame({
            'Marca': list(estadisticas['Distribucion_Marca'].keys()),
            'Cantidad': list(estadisticas['Distribucion_Marca'].values())
        })
        df_marca.to_excel(writer, sheet_name='Distribucion_Marca', index=False)
        
        # Hoja 3: Distribución por combustible
        df_combustible = pd.DataFrame({
            'Combustible': list(estadisticas['Distribucion_Combustible'].keys()),
            'Cantidad': list(estadisticas['Distribucion_Combustible'].values())
        })
        df_combustible.to_excel(writer, sheet_name='Distribucion_Combustible', index=False)
        
        # Hoja 4: Precio promedio por marca
        df_precio_marca = pd.DataFrame({
            'Marca': list(estadisticas['Precio_Promedio_Marca'].keys()),
            'Precio_Promedio': list(estadisticas['Precio_Promedio_Marca'].values())
        })
        df_precio_marca.to_excel(writer, sheet_name='Precio_por_Marca', index=False)
        
        # Hoja 5: Estadísticas descriptivas completas
        df.describe().to_excel(writer, sheet_name='Estadisticas_Descriptivas')
    
    print(f"\n[OK] Estadisticas exportadas a '{archivo_salida}'")


# ============================================================================
# SECCIÓN 3: FILTRADO DE DATOS
# ============================================================================

def filtrar_por_marca(df, marca):
    """
    Filtra vehículos por marca
    
    Args:
        df (pd.DataFrame): DataFrame con los datos
        marca (str): Marca a filtrar
        
    Returns:
        pd.DataFrame: DataFrame filtrado
    """
    resultado = df[df['Marca'] == marca]
    print(f"\nFiltro por marca '{marca}': {len(resultado)} vehiculos encontrados")
    return resultado


def filtrar_por_modelo(df, modelo):
    """
    Filtra vehículos por modelo
    
    Args:
        df (pd.DataFrame): DataFrame con los datos
        modelo (str): Modelo a filtrar
        
    Returns:
        pd.DataFrame: DataFrame filtrado
    """
    resultado = df[df['Modelo'] == modelo]
    print(f"\nFiltro por modelo '{modelo}': {len(resultado)} vehiculos encontrados")
    return resultado


def filtrar_por_anyo(df, anyo_min, anyo_max=None):
    """
    Filtra vehículos por año o rango de años
    
    Args:
        df (pd.DataFrame): DataFrame con los datos
        anyo_min (int): Año mínimo
        anyo_max (int, optional): Año máximo. Si no se especifica, filtra solo por año exacto
        
    Returns:
        pd.DataFrame: DataFrame filtrado
    """
    if anyo_max is None:
        resultado = df[df['Anyo'] == anyo_min]
        print(f"\nFiltro por año {anyo_min}: {len(resultado)} vehiculos encontrados")
    else:
        resultado = df[(df['Anyo'] >= anyo_min) & (df['Anyo'] <= anyo_max)]
        print(f"\nFiltro por rango de años {anyo_min}-{anyo_max}: {len(resultado)} vehiculos encontrados")
    return resultado


def filtrar_por_precio(df, precio_min, precio_max):
    """
    Filtra vehículos por rango de precio
    
    Args:
        df (pd.DataFrame): DataFrame con los datos
        precio_min (float): Precio mínimo
        precio_max (float): Precio máximo
        
    Returns:
        pd.DataFrame: DataFrame filtrado
    """
    resultado = df[(df['Precio'] >= precio_min) & (df['Precio'] <= precio_max)]
    print(f"\nFiltro por precio {precio_min}-{precio_max} EUR: {len(resultado)} vehiculos encontrados")
    return resultado


def filtrar_por_color(df, color):
    """
    Filtra vehículos por color
    
    Args:
        df (pd.DataFrame): DataFrame con los datos
        color (str): Color a filtrar
        
    Returns:
        pd.DataFrame: DataFrame filtrado
    """
    resultado = df[df['Color'] == color]
    print(f"\nFiltro por color '{color}': {len(resultado)} vehiculos encontrados")
    return resultado


def filtrar_por_combustible(df, combustible):
    """
    Filtra vehículos por tipo de combustible
    
    Args:
        df (pd.DataFrame): DataFrame con los datos
        combustible (str): Tipo de combustible
        
    Returns:
        pd.DataFrame: DataFrame filtrado
    """
    resultado = df[df['Combustible'] == combustible]
    print(f"\nFiltro por combustible '{combustible}': {len(resultado)} vehiculos encontrados")
    return resultado


def aplicar_filtros_ejemplo(df):
    """
    Aplica varios ejemplos de filtrado para demostrar funcionalidad
    
    Args:
        df (pd.DataFrame): DataFrame con los datos
    """
    print("\n" + "=" * 80)
    print("EJEMPLOS DE FILTRADO")
    print("=" * 80)
    
    # Filtro 1: Vehículos SEAT
    print("\n1. Vehiculos de marca SEAT:")
    seat = filtrar_por_marca(df, 'SEAT')
    print(seat[['Marca', 'Modelo', 'Anyo', 'Precio']].head())
    
    # Filtro 2: Vehículos del año 2023
    print("\n2. Vehiculos del año 2023:")
    anyo_2023 = filtrar_por_anyo(df, 2023)
    print(anyo_2023[['Marca', 'Modelo', 'Anyo', 'Precio']].head())
    
    # Filtro 3: Vehículos entre 15000 y 20000 EUR
    print("\n3. Vehiculos entre 15000 y 20000 EUR:")
    rango_precio = filtrar_por_precio(df, 15000, 20000)
    print(rango_precio[['Marca', 'Modelo', 'Precio']].head())
    
    # Filtro 4: Vehículos blancos
    print("\n4. Vehiculos de color blanco:")
    blancos = filtrar_por_color(df, 'Blanco')
    print(blancos[['Marca', 'Modelo', 'Color', 'Precio']].head())
    
    # Filtro 5: Vehículos eléctricos
    print("\n5. Vehiculos electricos:")
    electricos = filtrar_por_combustible(df, 'Eléctrico')
    print(electricos[['Marca', 'Modelo', 'Combustible', 'Autonomía']].head())
    
    # Filtro combinado: SEAT del 2020 en adelante
    print("\n6. Vehiculos SEAT del 2020 en adelante:")
    seat_recientes = df[(df['Marca'] == 'SEAT') & (df['Anyo'] >= 2020)]
    print(f"Encontrados: {len(seat_recientes)} vehiculos")
    print(seat_recientes[['Marca', 'Modelo', 'Anyo', 'Precio']])


# ============================================================================
# SECCIÓN 4: ORDENAMIENTO DE DATOS
# ============================================================================

def ordenar_por_precio(df, ascendente=True):
    """
    Ordena vehículos por precio
    
    Args:
        df (pd.DataFrame): DataFrame con los datos
        ascendente (bool): True para orden ascendente, False para descendente
        
    Returns:
        pd.DataFrame: DataFrame ordenado
    """
    orden = "ascendente" if ascendente else "descendente"
    print(f"\nOrdenando por precio ({orden})...")
    return df.sort_values('Precio', ascending=ascendente)


def ordenar_por_anyo(df, ascendente=False):
    """
    Ordena vehículos por año
    
    Args:
        df (pd.DataFrame): DataFrame con los datos
        ascendente (bool): True para orden ascendente, False para descendente
        
    Returns:
        pd.DataFrame: DataFrame ordenado
    """
    orden = "ascendente" if ascendente else "descendente"
    print(f"\nOrdenando por año ({orden})...")
    return df.sort_values('Anyo', ascending=ascendente)


def ordenar_por_kilometros(df, ascendente=True):
    """
    Ordena vehículos por kilómetros
    
    Args:
        df (pd.DataFrame): DataFrame con los datos
        ascendente (bool): True para orden ascendente, False para descendente
        
    Returns:
        pd.DataFrame: DataFrame ordenado
    """
    orden = "ascendente" if ascendente else "descendente"
    print(f"\nOrdenando por kilometros ({orden})...")
    return df.sort_values('Kilómetros', ascending=ascendente)


def ordenar_por_emisiones(df, ascendente=True):
    """
    Ordena vehículos por emisiones de CO2
    
    Args:
        df (pd.DataFrame): DataFrame con los datos
        ascendente (bool): True para orden ascendente, False para descendente
        
    Returns:
        pd.DataFrame: DataFrame ordenado
    """
    orden = "ascendente" if ascendente else "descendente"
    print(f"\nOrdenando por emisiones ({orden})...")
    return df.sort_values('Emisiones', ascending=ascendente)


def aplicar_ordenamientos_ejemplo(df):
    """
    Aplica varios ejemplos de ordenamiento para demostrar funcionalidad
    
    Args:
        df (pd.DataFrame): DataFrame con los datos
    """
    print("\n" + "=" * 80)
    print("EJEMPLOS DE ORDENAMIENTO")
    print("=" * 80)
    
    # Ordenamiento 1: Por precio (más baratos primero)
    print("\n1. Vehiculos mas baratos:")
    baratos = ordenar_por_precio(df, ascendente=True)
    print(baratos[['Marca', 'Modelo', 'Anyo', 'Precio']].head(10))
    
    # Ordenamiento 2: Por precio (más caros primero)
    print("\n2. Vehiculos mas caros:")
    caros = ordenar_por_precio(df, ascendente=False)
    print(caros[['Marca', 'Modelo', 'Anyo', 'Precio']].head(10))
    
    # Ordenamiento 3: Por año (más recientes primero)
    print("\n3. Vehiculos mas recientes:")
    recientes = ordenar_por_anyo(df, ascendente=False)
    print(recientes[['Marca', 'Modelo', 'Anyo', 'Precio']].head(10))
    
    # Ordenamiento 4: Por kilómetros (menos km primero)
    print("\n4. Vehiculos con menos kilometros:")
    menos_km = ordenar_por_kilometros(df, ascendente=True)
    print(menos_km[['Marca', 'Modelo', 'Kilómetros', 'Precio']].head(10))
    
    # Ordenamiento 5: Por emisiones (más ecológicos primero)
    print("\n5. Vehiculos mas ecologicos (menos emisiones):")
    ecologicos = ordenar_por_emisiones(df, ascendente=True)
    print(ecologicos[['Marca', 'Modelo', 'Combustible', 'Emisiones']].head(10))


# ============================================================================
# SECCIÓN 5: TRANSFORMACIÓN DE DATOS
# ============================================================================

def calcular_depreciacion(df):
    """
    Calcula la depreciación de los vehículos según el año y kilómetros
    Fórmula: Depreciación = (Edad * 0.15) + (Kilómetros / 100000 * 0.10)
    
    Args:
        df (pd.DataFrame): DataFrame con los datos
        
    Returns:
        pd.DataFrame: DataFrame con columnas de depreciación añadidas
    """
    print("\n" + "=" * 80)
    print("CALCULANDO DEPRECIACION DE VEHICULOS")
    print("=" * 80)
    
    df_transformado = df.copy()
    
    # Calcular edad del vehículo
    anyo_actual = 2026
    df_transformado['Edad'] = anyo_actual - df_transformado['Anyo']
    
    # Calcular depreciación por edad (15% por año)
    df_transformado['Depreciacion_Edad'] = df_transformado['Edad'] * 0.15
    
    # Calcular depreciación por kilómetros (10% por cada 100,000 km)
    df_transformado['Depreciacion_Kilometros'] = (df_transformado['Kilómetros'] / 100000) * 0.10
    
    # Depreciación total (máximo 0.90 = 90%)
    df_transformado['Depreciacion_Total'] = (
        df_transformado['Depreciacion_Edad'] + 
        df_transformado['Depreciacion_Kilometros']
    ).clip(upper=0.90)
    
    # Calcular valor estimado actual
    df_transformado['Valor_Estimado'] = (
        df_transformado['Precio'] * (1 - df_transformado['Depreciacion_Total'])
    ).round(2)
    
    # Calcular pérdida de valor
    df_transformado['Perdida_Valor'] = (
        df_transformado['Precio'] - df_transformado['Valor_Estimado']
    ).round(2)
    
    print("\n[OK] Depreciacion calculada exitosamente")
    print("\nEjemplos de depreciacion:")
    print(df_transformado[['Marca', 'Modelo', 'Anyo', 'Edad', 'Kilómetros', 
                           'Precio', 'Depreciacion_Total', 'Valor_Estimado']].head(10))
    
    return df_transformado


def calcular_coste_por_km(df):
    """
    Calcula el coste por kilómetro recorrido
    
    Args:
        df (pd.DataFrame): DataFrame con los datos
        
    Returns:
        pd.DataFrame: DataFrame con columna de coste por km añadida
    """
    df_transformado = df.copy()
    
    # Evitar división por cero
    df_transformado['Coste_Por_Km'] = (
        df_transformado['Precio'] / df_transformado['Kilómetros'].replace(0, 1)
    ).round(2)
    
    print("\n[OK] Coste por kilometro calculado")
    return df_transformado


def clasificar_por_precio(df):
    """
    Clasifica vehículos en categorías según su precio
    
    Args:
        df (pd.DataFrame): DataFrame con los datos
        
    Returns:
        pd.DataFrame: DataFrame con columna de categoría añadida
    """
    df_transformado = df.copy()
    
    def categorizar_precio(precio):
        if precio < 15000:
            return 'Economico'
        elif precio < 25000:
            return 'Medio'
        elif precio < 35000:
            return 'Premium'
        else:
            return 'Lujo'
    
    df_transformado['Categoria_Precio'] = df_transformado['Precio'].apply(categorizar_precio)
    
    print("\n[OK] Vehiculos clasificados por categoria de precio")
    print("\nDistribucion por categoria:")
    print(df_transformado['Categoria_Precio'].value_counts())
    
    return df_transformado


def clasificar_por_emisiones(df):
    """
    Clasifica vehículos según su nivel de emisiones (etiqueta ambiental)
    
    Args:
        df (pd.DataFrame): DataFrame con los datos
        
    Returns:
        pd.DataFrame: DataFrame con columna de etiqueta ambiental añadida
    """
    df_transformado = df.copy()
    
    def obtener_etiqueta_ambiental(row):
        emisiones = row['Emisiones']
        combustible = row['Combustible']
        
        if combustible == 'Eléctrico':
            return 'CERO'
        elif combustible in ['Híbrido', 'Híbrido Enchufable']:
            return 'ECO'
        elif emisiones < 120:
            return 'C'
        elif emisiones < 160:
            return 'B'
        else:
            return 'SIN ETIQUETA'
    
    df_transformado['Etiqueta_Ambiental'] = df_transformado.apply(obtener_etiqueta_ambiental, axis=1)
    
    print("\n[OK] Etiquetas ambientales asignadas")
    print("\nDistribucion por etiqueta ambiental:")
    print(df_transformado['Etiqueta_Ambiental'].value_counts())
    
    return df_transformado


def aplicar_transformaciones(df):
    """
    Aplica todas las transformaciones a los datos
    
    Args:
        df (pd.DataFrame): DataFrame con los datos originales
        
    Returns:
        pd.DataFrame: DataFrame con todas las transformaciones aplicadas
    """
    print("\n" + "=" * 80)
    print("APLICANDO TRANSFORMACIONES")
    print("=" * 80)
    
    # Aplicar todas las transformaciones
    df_transformado = calcular_depreciacion(df)
    df_transformado = calcular_coste_por_km(df_transformado)
    df_transformado = clasificar_por_precio(df_transformado)
    df_transformado = clasificar_por_emisiones(df_transformado)
    
    print("\n[OK] Todas las transformaciones aplicadas exitosamente")
    
    return df_transformado


def exportar_a_csv(df, archivo_salida='vehiculos_transformados.csv'):
    """
    Exporta el DataFrame transformado a un archivo CSV
    
    Args:
        df (pd.DataFrame): DataFrame a exportar
        archivo_salida (str): Nombre del archivo de salida
    """
    print("\n" + "=" * 80)
    print("EXPORTANDO DATOS TRANSFORMADOS")
    print("=" * 80)
    
    df.to_csv(archivo_salida, index=False, encoding='utf-8-sig')
    print(f"\n[OK] Datos exportados a '{archivo_salida}'")
    print(f"[OK] Total de registros exportados: {len(df)}")
    print(f"[OK] Total de columnas: {len(df.columns)}")


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """
    Función principal que ejecuta todo el análisis
    """
    print("\n")
    print("=" * 80)
    print(" " * 20 + "ANALISIS DE VEHICULOS - MERCADO ESPAÑOL")
    print("=" * 80)
    print(f"Fecha de ejecucion: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
    # 1. Cargar datos
    archivo_excel = 'vehiculos_mercado_espanol.xlsx'
    df = cargar_datos_vehiculos(archivo_excel)
    
    if df is None:
        print("\n[ERROR] No se pudieron cargar los datos. Finalizando programa.")
        return
    
    # 2. Verificar datos
    verificar_datos(df)
    
    # 3. Procesar valores nulos
    df_procesado = procesar_valores_nulos(df)
    
    # 4. Análisis estadístico
    estadisticas = analisis_estadistico(df_procesado)
    
    # 5. Exportar estadísticas
    exportar_estadisticas(estadisticas, df_procesado)
    
    # 6. Ejemplos de filtrado
    aplicar_filtros_ejemplo(df_procesado)
    
    # 7. Ejemplos de ordenamiento
    aplicar_ordenamientos_ejemplo(df_procesado)
    
    # 8. Aplicar transformaciones
    df_final = aplicar_transformaciones(df_procesado)
    
    # 9. Exportar datos transformados a CSV
    exportar_a_csv(df_final)
    
    # Resumen final
    print("\n" + "=" * 80)
    print("RESUMEN FINAL")
    print("=" * 80)
    print(f"\n[OK] Analisis completado exitosamente")
    print(f"[OK] Registros procesados: {len(df_final)}")
    print(f"[OK] Archivos generados:")
    print(f"     - estadisticas_vehiculos.xlsx")
    print(f"     - vehiculos_transformados.csv")
    print("\n" + "=" * 80)
    print(" " * 25 + "FIN DEL ANALISIS")
    print("=" * 80 + "\n")


# Ejecutar programa principal
if __name__ == "__main__":
    main()
