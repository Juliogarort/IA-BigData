
import os

# Obtener la ruta del directorio donde está este script
DIRECTORIO_SCRIPT = os.path.dirname(os.path.abspath(__file__))

def leer_cotizaciones(fichero):
    # Creamos un diccionario vacío para guardar los datos
    datos = {}
    
    # Creamos la ruta completa del fichero
    ruta_completa = os.path.join(DIRECTORIO_SCRIPT, fichero)
    
    try:
        with open(ruta_completa, 'r', encoding='utf-8') as f:
            # Leemos la primera línea que contiene los nombres de las columnas
            primera_linea = f.readline().strip()
            columnas = primera_linea.split(';')
            
            # Inicializamos el diccionario con listas vacías para cada columna
            for columna in columnas:
                datos[columna] = []
            
            # Leemos el resto de líneas (los datos)
            for linea in f:
                linea = linea.strip()
                
                # Si la línea no está vacía
                if linea:
                    # Separamos los valores por punto y coma
                    valores = linea.split(';')
                    
                    # Añadimos cada valor a su columna correspondiente
                    for i, valor in enumerate(valores):
                        # Convertimos los números (reemplazamos coma por punto)
                        # y quitamos los puntos de los miles
                        if i > 0:  # Las columnas numéricas (excepto Nombre)
                            # Quitamos los puntos de los miles
                            valor = valor.replace('.', '')
                            # Reemplazamos la coma decimal por punto
                            valor = valor.replace(',', '.')
                            try:
                                valor = float(valor)
                            except ValueError:
                                pass  # Si no se puede convertir, dejamos el valor como está
                        
                        datos[columnas[i]].append(valor)
        
        print(f"Datos leídos correctamente de {fichero}")
        print(f"Total de empresas: {len(datos['Nombre'])}")
        return datos
        
    except FileNotFoundError:
        print(f"Error: No se encontró el fichero {fichero}")
        return None


def calcular_estadisticas(datos):

    if datos is None:
        return None
    
    estadisticas = {}
    
    # Recorremos cada columna del diccionario
    for columna, valores in datos.items():
        # Solo calculamos estadísticas para columnas numéricas
        if columna != 'Nombre' and len(valores) > 0:
            # Filtramos solo los valores numéricos (por si hay algún error)
            valores_numericos = [v for v in valores if isinstance(v, (int, float))]
            
            if valores_numericos:
                minimo = min(valores_numericos)
                maximo = max(valores_numericos)
                media = sum(valores_numericos) / len(valores_numericos)
                
                estadisticas[columna] = {
                    'Mínimo': minimo,
                    'Máximo': maximo,
                    'Media': media
                }
    
    return estadisticas


def guardar_estadisticas(estadisticas, fichero_salida):

    if estadisticas is None:
        print("No hay estadísticas para guardar")
        return
    
    try:
        # Creamos la ruta completa del fichero de salida
        ruta_completa = os.path.join(DIRECTORIO_SCRIPT, fichero_salida)
        
        with open(ruta_completa, 'w', encoding='utf-8') as f:
            # Escribimos la cabecera
            f.write("Columna;Mínimo;Máximo;Media\n")
            
            # Escribimos las estadísticas de cada columna
            for columna, stats in estadisticas.items():
                f.write(f"{columna};{stats['Mínimo']:.2f};{stats['Máximo']:.2f};{stats['Media']:.2f}\n")
        
        print(f"\nEstadísticas guardadas en {fichero_salida}")
        print(f"Ubicación: {DIRECTORIO_SCRIPT}")
        
    except Exception as e:
        print(f"Error al guardar el fichero: {e}")


def mostrar_estadisticas(estadisticas):

    if estadisticas is None:
        print("No hay estadísticas para mostrar")
        return
    
    print("\n" + "=" * 70)
    print("ESTADÍSTICAS DE COTIZACIONES DEL IBEX35")
    print("=" * 70)
    print(f"{'Columna':<20} {'Mínimo':>15} {'Máximo':>15} {'Media':>15}")
    print("-" * 70)
    
    for columna, stats in estadisticas.items():
        print(f"{columna:<20} {stats['Mínimo']:>15.2f} {stats['Máximo']:>15.2f} {stats['Media']:>15.2f}")
    
    print("=" * 70)


def menu():
    datos = None
    estadisticas = None
    
    while True:
        print("\n" + "=" * 70)
        print("EJERCICIO 03 - ANÁLISIS DE COTIZACIONES DEL IBEX35")
        print("=" * 70)
        print("1. Leer fichero de cotizaciones (cotizacion.csv)")
        print("2. Calcular y mostrar estadísticas")
        print("3. Guardar estadísticas en fichero CSV")
        print("4. Salir")
        print("=" * 70)
        
        opcion = input("Elige una opción (1-4): ")
        
        if opcion == '1':
            print("\n1. Leyendo fichero de cotizaciones...")
            print(f"Directorio de trabajo: {DIRECTORIO_SCRIPT}")
            datos = leer_cotizaciones('cotizacion.csv')
            if datos:
                # Reiniciamos las estadísticas porque los datos cambiaron
                estadisticas = None
                
        elif opcion == '2':
            if datos is None:
                print("\nError: Primero debes leer el fichero de cotizaciones (opción 1)")
            else:
                print("\n2. Calculando estadísticas...")
                estadisticas = calcular_estadisticas(datos)
                if estadisticas:
                    # Mostramos las estadísticas automáticamente
                    mostrar_estadisticas(estadisticas)
                    
        elif opcion == '3':
            if estadisticas is None:
                print("\nError: Primero debes calcular las estadísticas (opción 2)")
            else:
                print("\n3. Guardando estadísticas en fichero...")
                guardar_estadisticas(estadisticas, 'estadisticas.csv')
                
        elif opcion == '4':
            print("¡Hasta luego!")
            break
            
        else:
            print("Opción no válida. Elige entre 1 y 4.")


# Programa principal
if __name__ == "__main__":
    menu()
