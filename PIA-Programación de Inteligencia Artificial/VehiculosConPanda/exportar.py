import os
import pandas as pd
from typing import Dict


class Exportador:
    """Maneja la exportación de datos y estadísticas"""
    
    @staticmethod
    def a_excel(estadisticas: Dict, df: pd.DataFrame, archivo: str = 'estadisticas_vehiculos.xlsx') -> None:
        """Exporta estadísticas a Excel con formato mejorado"""
        print("\n" + "=" * 80)
        print("EXPORTANDO A EXCEL")
        print("=" * 80)
        
        # Crear carpeta output si no existe
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(script_dir, 'output')
        os.makedirs(output_dir, exist_ok=True)
        
        # Guardar en la carpeta output
        ruta_completa = os.path.join(output_dir, archivo)
        
        with pd.ExcelWriter(ruta_completa, engine='openpyxl') as writer:
            # Resumen - con valores numéricos en lugar de strings
            resumen = pd.DataFrame({
                'Metrica': [
                    'Precio Promedio (EUR)',
                    'Precio Mediana (EUR)',
                    'Kilometros Promedio',
                    'Emisiones Promedio (g/km)'
                ],
                'Valor': [
                    estadisticas['Precio']['Promedio'],
                    estadisticas['Precio']['Mediana'],
                    estadisticas['Kilometros']['Promedio'],
                    estadisticas['Emisiones']['Promedio']
                ]
            })
            resumen.to_excel(writer, sheet_name='Resumen', index=False)
            
            # Aplicar formato a la hoja Resumen
            worksheet = writer.sheets['Resumen']
            
            # Formato para valores numéricos
            for row in range(2, 6):  # Filas 2-5 (después del encabezado)
                cell = worksheet[f'B{row}']
                if row <= 3:  # Precios
                    cell.number_format = '#,##0.00 €'
                elif row == 4:  # Kilómetros
                    cell.number_format = '#,##0'
                else:  # Emisiones
                    cell.number_format = '#,##0.00'
            
            # Ajustar ancho de columnas
            worksheet.column_dimensions['A'].width = 30
            worksheet.column_dimensions['B'].width = 20
            
            # Distribución por marca
            df_marca = pd.DataFrame({
                'Marca': list(estadisticas['Distribucion_Marca'].keys()),
                'Cantidad': list(estadisticas['Distribucion_Marca'].values())
            })
            df_marca.to_excel(writer, sheet_name='Distribucion_Marca', index=False)
            
            # Ajustar ancho de columnas en Distribución por Marca
            worksheet_marca = writer.sheets['Distribucion_Marca']
            worksheet_marca.column_dimensions['A'].width = 20
            worksheet_marca.column_dimensions['B'].width = 15
            
            # Estadísticas descriptivas
            df_stats = df.describe()
            df_stats.to_excel(writer, sheet_name='Estadisticas_Descriptivas')
            
            # Aplicar formato a estadísticas descriptivas
            worksheet_stats = writer.sheets['Estadisticas_Descriptivas']
            
            # Formato para columnas numéricas (Precio, Kilómetros, etc.)
            columnas_precio = ['Precio', 'Valor_Estimado', 'Perdida_Valor', 'Coste_Por_Km']
            columnas_kilometros = ['Kilómetros', 'Autonomía']
            
            # Obtener índices de columnas
            for col_idx, col_name in enumerate(df.columns, start=2):  # Empieza en B (2)
                col_letter = chr(64 + col_idx)  # Convertir número a letra (A, B, C...)
                
                if col_name in columnas_precio:
                    # Formato de moneda para precios
                    for row in range(2, 11):  # Filas de datos estadísticos
                        cell = worksheet_stats[f'{col_letter}{row}']
                        cell.number_format = '#,##0.00 €'
                elif col_name in columnas_kilometros:
                    # Formato de número entero para kilómetros
                    for row in range(2, 11):
                        cell = worksheet_stats[f'{col_letter}{row}']
                        cell.number_format = '#,##0'
                elif col_name in ['Emisiones', 'Potencia', 'Peso']:
                    # Formato con 2 decimales
                    for row in range(2, 11):
                        cell = worksheet_stats[f'{col_letter}{row}']
                        cell.number_format = '#,##0.00'
                
                # Ajustar ancho de columna
                worksheet_stats.column_dimensions[col_letter].width = 15
            
            # Ajustar primera columna (índice)
            worksheet_stats.column_dimensions['A'].width = 12
        
        print(f"[OK] Exportado a '{archivo}' con formato mejorado")
    
    @staticmethod
    def a_csv(df: pd.DataFrame, archivo: str = 'vehiculos_transformados.csv') -> None:
        """Exporta DataFrame a CSV"""
        print("\n" + "=" * 80)
        print("EXPORTANDO A CSV")
        print("=" * 80)
        
        # Crear carpeta output si no existe
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(script_dir, 'output')
        os.makedirs(output_dir, exist_ok=True)
        
        # Guardar en la carpeta output
        ruta_completa = os.path.join(output_dir, archivo)
        
        df.to_csv(ruta_completa, index=False, encoding='utf-8-sig')
        print(f"[OK] Exportado a '{ruta_completa}'")
        print(f"[OK] {len(df)} registros, {len(df.columns)} columnas")

