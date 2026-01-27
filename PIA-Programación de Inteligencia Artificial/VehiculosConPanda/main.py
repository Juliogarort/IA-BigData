import os
from datetime import datetime
from gestor_datos import GestorDatos
from analizar import AnalizadorEstadistico
from filtro import FiltradorDatos
from transformar import TransformadorDatos
from exportar import Exportador


def main():
    """Función principal que ejecuta todo el análisis"""
    print("\n" + "=" * 80)
    print(" " * 15 + "ANALISIS DE VEHICULOS - MERCADO ESPAÑOL")
    print("=" * 80)
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
    # Obtener el directorio donde está el script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    archivo_excel = os.path.join(script_dir, 'vehiculos_mercado_espanol.xlsx')
    
    # 1. Cargar y procesar datos
    gestor = GestorDatos(archivo_excel)
    if not gestor.cargar():
        print("\n[ERROR] No se pudieron cargar los datos")
        return
    
    gestor.verificar()
    gestor.procesar_nulos()
    df = gestor.obtener_datos()
    
    # 2. Análisis estadístico
    analizador = AnalizadorEstadistico(df)
    estadisticas = analizador.analizar_todo()
    
    # 3. Filtrado y ordenamiento
    filtrador = FiltradorDatos(df)
    filtrador.mostrar_ejemplos()
    
    # 4. Transformaciones
    transformador = TransformadorDatos(df)
    df_final = transformador.aplicar_todas()
    
    # 5. Exportar resultados
    Exportador.a_excel(estadisticas, df)
    Exportador.a_csv(df_final)
    
    # Resumen final
    print("\n" + "=" * 80)
    print("RESUMEN FINAL")
    print("=" * 80)
    print(f"\n[OK] Análisis completado")
    print(f"[OK] Registros procesados: {len(df_final)}")
    print(f"[OK] Archivos generados:")
    print(f"     - estadisticas_vehiculos.xlsx")
    print(f"     - vehiculos_transformados.csv")
    print("\n" + "=" * 80)
    print(" " * 25 + "FIN DEL ANALISIS")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()