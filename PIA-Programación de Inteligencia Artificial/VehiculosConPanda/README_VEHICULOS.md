# 🚗 Análisis de Vehículos del Mercado Español con Pandas

Proyecto completo de análisis de datos de vehículos utilizando Python y pandas. Incluye generación de datos, procesamiento, análisis estadístico, filtrado, ordenamiento y transformaciones avanzadas.

## 📋 Descripción

Este proyecto implementa un sistema completo de análisis de datos para vehículos del mercado español, cumpliendo con los siguientes requisitos:

- ✅ Generación de datos realistas de 120+ vehículos
- ✅ Carga y procesamiento de datos desde Excel
- ✅ Tratamiento inteligente de valores nulos
- ✅ Análisis estadístico completo
- ✅ Filtrado por múltiples criterios
- ✅ Ordenamiento de datos
- ✅ Transformaciones avanzadas (depreciación, clasificaciones)
- ✅ Exportación a Excel y CSV
- ✅ Código completamente documentado

## 📁 Archivos del Proyecto

### Scripts Python

- **`generar_datos_vehiculos.py`** - Genera el dataset inicial con 120 vehículos
- **`analisis_vehiculos.py`** - Script principal con todas las funcionalidades de análisis

### Archivos de Datos Generados

- **`vehiculos_mercado_espanol.xlsx`** - Dataset original (120 registros, 16 columnas)
- **`estadisticas_vehiculos.xlsx`** - Análisis estadístico (5 hojas)
- **`vehiculos_transformados.csv`** - Datos transformados (120 registros, 25 columnas)

## 🚀 Instalación y Uso

### Requisitos

```bash
pip install pandas openpyxl
```

### Paso 1: Generar Datos Iniciales

```bash
python generar_datos_vehiculos.py
```

Este script genera `vehiculos_mercado_espanol.xlsx` con 120 vehículos del mercado español.

### Paso 2: Ejecutar Análisis Completo

```bash
python analisis_vehiculos.py
```

Este script realiza el análisis completo y genera:
- `estadisticas_vehiculos.xlsx` - Estadísticas detalladas
- `vehiculos_transformados.csv` - Datos con transformaciones aplicadas

## 📊 Características de los Datos

### Columnas Originales (16)

| Columna | Tipo | Descripción |
|---------|------|-------------|
| N_ID | int | Número de identificación |
| Marca | str | Marca del vehículo |
| Modelo | str | Modelo del vehículo |
| Anyo | int | Año de fabricación (2015-2024) |
| Color | str | Color del vehículo |
| Kilómetros | float | Kilometraje |
| Motor | str | Tipo de motor |
| Combustible | str | Tipo de combustible |
| Tamaño | str | Dimensiones (LxAxA en cm) |
| N_Ocupantes | int | Número de ocupantes |
| Peso | int | Peso en kg |
| C_Maletero | float | Capacidad del maletero (litros) |
| Potencia | str | Potencia (CV o kW) |
| Emisiones | float | Emisiones CO2 (g/km) |
| Autonomía | float | Autonomía (km) |
| Precio | float | Precio (EUR) |

### Marcas Incluidas (15)

SEAT, Renault, Peugeot, Volkswagen, Toyota, Opel, Citroën, Nissan, Ford, Hyundai, Kia, Dacia, BMW, Mercedes-Benz, Audi

### Tipos de Combustible (5)

Gasolina, Diésel, Eléctrico, Híbrido, Híbrido Enchufable

## 🔧 Funcionalidades Principales

### 1. Carga y Procesamiento

```python
# Cargar datos
df = cargar_datos_vehiculos('vehiculos_mercado_espanol.xlsx')

# Verificar integridad
verificar_datos(df)

# Procesar valores nulos
df_procesado = procesar_valores_nulos(df)
```

### 2. Análisis Estadístico

```python
# Generar estadísticas
estadisticas = analisis_estadistico(df_procesado)

# Exportar a Excel
exportar_estadisticas(estadisticas, df_procesado)
```

Estadísticas incluidas:
- Promedio, mediana, mín, máx de precios
- Promedio y mediana de kilometraje
- Emisiones promedio
- Distribución por marca, combustible y año
- Precio promedio por marca

### 3. Filtrado de Datos

```python
# Filtrar por marca
seat = filtrar_por_marca(df, 'SEAT')

# Filtrar por rango de precio
economicos = filtrar_por_precio(df, 15000, 20000)

# Filtrar por año
recientes = filtrar_por_anyo(df, 2020, 2024)

# Filtrar por color
blancos = filtrar_por_color(df, 'Blanco')

# Filtrar por combustible
electricos = filtrar_por_combustible(df, 'Eléctrico')

# Filtros combinados
seat_recientes = df[(df['Marca'] == 'SEAT') & (df['Anyo'] >= 2020)]
```

### 4. Ordenamiento de Datos

```python
# Ordenar por precio (ascendente/descendente)
baratos = ordenar_por_precio(df, ascendente=True)
caros = ordenar_por_precio(df, ascendente=False)

# Ordenar por año
recientes = ordenar_por_anyo(df, ascendente=False)

# Ordenar por kilómetros
menos_km = ordenar_por_kilometros(df, ascendente=True)

# Ordenar por emisiones
ecologicos = ordenar_por_emisiones(df, ascendente=True)
```

### 5. Transformaciones de Datos

```python
# Aplicar todas las transformaciones
df_transformado = aplicar_transformaciones(df)
```

**Transformaciones incluidas:**

#### a) Cálculo de Depreciación
- Edad del vehículo
- Depreciación por edad (15% anual)
- Depreciación por kilómetros (10% por 100,000 km)
- Depreciación total (máx 90%)
- Valor estimado actual
- Pérdida de valor

#### b) Coste por Kilómetro
- Cálculo de EUR/km recorrido

#### c) Clasificación por Precio
- **Económico**: < 15,000 EUR
- **Medio**: 15,000 - 25,000 EUR
- **Premium**: 25,000 - 35,000 EUR
- **Lujo**: > 35,000 EUR

#### d) Etiqueta Ambiental (DGT)
- **CERO**: Vehículos eléctricos
- **ECO**: Híbridos
- **C**: Emisiones < 120 g/km
- **B**: Emisiones < 160 g/km
- **SIN ETIQUETA**: Resto

### 6. Exportación de Datos

```python
# Exportar a CSV
exportar_a_csv(df_transformado, 'vehiculos_transformados.csv')
```

## 📈 Ejemplos de Resultados

### Vehículos Más Baratos
1. Dacia Jogger 2016: 7,024 EUR
2. Renault Kadjar 2015: 9,282 EUR
3. Renault Megane 2015: 10,159 EUR

### Vehículos Más Caros
1. Mercedes-Benz Clase A 2024: 52,065 EUR
2. Audi Q2 2023: 47,584 EUR
3. BMW X3 2024: 45,690 EUR

### Distribución por Categoría de Precio
- Económico: 16 vehículos
- Medio: 72 vehículos
- Premium: 20 vehículos
- Lujo: 12 vehículos

### Distribución por Etiqueta Ambiental
- CERO: 30 vehículos (eléctricos)
- ECO: 49 vehículos (híbridos)
- C: 14 vehículos
- B: 27 vehículos

## 📝 Documentación del Código

Todas las funciones incluyen:
- Docstrings detallados
- Descripción de parámetros
- Tipos de datos
- Valores de retorno
- Comentarios explicativos

Ejemplo:

```python
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
```

## 🎯 Estructura del Código

El script `analisis_vehiculos.py` está organizado en 5 secciones:

1. **Carga y Procesamiento de Datos**
   - `cargar_datos_vehiculos()`
   - `verificar_datos()`
   - `procesar_valores_nulos()`

2. **Análisis Estadístico**
   - `analisis_estadistico()`
   - `exportar_estadisticas()`

3. **Filtrado de Datos**
   - `filtrar_por_marca()`
   - `filtrar_por_modelo()`
   - `filtrar_por_anyo()`
   - `filtrar_por_precio()`
   - `filtrar_por_color()`
   - `filtrar_por_combustible()`

4. **Ordenamiento de Datos**
   - `ordenar_por_precio()`
   - `ordenar_por_anyo()`
   - `ordenar_por_kilometros()`
   - `ordenar_por_emisiones()`

5. **Transformación de Datos**
   - `calcular_depreciacion()`
   - `calcular_coste_por_km()`
   - `clasificar_por_precio()`
   - `clasificar_por_emisiones()`
   - `aplicar_transformaciones()`
   - `exportar_a_csv()`

## ✅ Cumplimiento de Requisitos

| Requisito | Estado |
|-----------|--------|
| Excel con 100+ registros | ✅ 120 registros |
| 16 características | ✅ Todas incluidas |
| Datos reales del mercado español | ✅ 15 marcas populares |
| Carga en DataFrame | ✅ Implementado |
| Procesamiento de nulos | ✅ 4 estrategias diferentes |
| Verificación de datos | ✅ Completa |
| Análisis estadístico | ✅ 8+ métricas |
| Excel con estadísticas | ✅ 5 hojas |
| Filtrado (5 criterios) | ✅ 6 funciones |
| Ordenamiento | ✅ 4 funciones |
| Transformaciones | ✅ 4 tipos |
| Cálculo de depreciación | ✅ Fórmula completa |
| CSV con datos transformados | ✅ 25 columnas |
| Comentarios en código | ✅ Todas las funciones |

## 🔍 Próximos Pasos Sugeridos

1. **Visualización**: Gráficos con matplotlib/seaborn
2. **Dashboard**: Interfaz interactiva con Streamlit
3. **Machine Learning**: Predicción de precios
4. **API REST**: Exposición de funcionalidades
5. **Base de datos**: Migración a SQL

## 👨‍💻 Autor

Julio García Ortiz  
Programación de Inteligencia Artificial  
Python + Pandas

## 📄 Licencia

Proyecto educativo - Libre uso para aprendizaje

---

**Proyecto completado exitosamente** ✨
