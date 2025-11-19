import os
import re
from collections import Counter

# Obtener la ruta del directorio donde está este script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOMBRE_ARCHIVO = os.path.join(BASE_DIR, "el_quijote.txt")

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def cargar_archivo():
    try:
        with open(NOMBRE_ARCHIVO, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo 'el_quijote.txt' en {BASE_DIR}")
        return None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def contar_palabras_totales(contenido):
    # Separar por espacios y filtrar vacíos
    palabras = contenido.split()
    total = len(palabras)
    print(f"\n{'='*60}")
    print(f"1. TOTAL DE PALABRAS EN EL DOCUMENTO")
    print(f"{'='*60}")
    print(f"Total de palabras: {total}")
    return total

def contar_palabra_capitulo(contenido):
    # Convertir todo a minúsculas para ignorar el formato
    contenido_lower = contenido.lower()
    # Buscar la palabra "capítulo" (con tilde y sin tilde)
    count_con_tilde = contenido_lower.count("capítulo")
    count_sin_tilde = contenido_lower.count("capitulo")
    total = count_con_tilde + count_sin_tilde
    
    print(f"\n{'='*60}")
    print(f"2. CONTEO DE LA PALABRA 'CAPÍTULO'")
    print(f"{'='*60}")
    print(f"La palabra 'Capítulo' aparece: {total} veces")
    return total

def crear_archivos_por_capitulo(contenido):
    """3. Crea un archivo .txt por cada capítulo del documento"""
    print(f"\n{'='*60}")
    print(f"3. CREANDO ARCHIVOS POR CAPÍTULO")
    print(f"{'='*60}")
    
    patron = r'CAP[IÍ]TULO\s+[IVXLCDM]+|CAP[IÍ]TULO\s+\d+'
    capitulos = re.split(patron, contenido, flags=re.IGNORECASE)
    titulos_capitulos = re.findall(patron, contenido, flags=re.IGNORECASE)
    
    # El primer elemento suele ser texto antes del primer capítulo (prólogo, etc)
    if len(capitulos) > 0 and capitulos[0].strip():
        with open(os.path.join(BASE_DIR, "Capitulo_00_Prologo.txt"), 'w', encoding='utf-8') as f:
            f.write(capitulos[0])
        print(f"Creado: Capitulo_00_Prologo.txt")
    
    # Crear archivos para cada capítulo
    for i, (titulo, contenido_cap) in enumerate(zip(titulos_capitulos, capitulos[1:]), start=1):
        nombre_archivo = f"Capitulo_{i:02d}.txt"
        ruta_archivo = os.path.join(BASE_DIR, nombre_archivo)
        with open(ruta_archivo, 'w', encoding='utf-8') as f:
            f.write(f"{titulo}\n\n{contenido_cap}")
        print(f"Creado: {nombre_archivo}")
    
    print(f"\nTotal de archivos creados: {len(titulos_capitulos) + 1}")

def contar_palabras_especificas(contenido):
    print(f"\n{'='*60}")
    print(f"4. CONTEO DE PALABRAS ESPECÍFICAS")
    print(f"{'='*60}")
    
    contenido_lower = contenido.lower()
    
    palabras_buscar = ["dulcinea", "quijote", "sancho"]
    resultados = {}
    
    for palabra in palabras_buscar:
        count = contenido_lower.count(palabra)
        resultados[palabra] = count
        print(f"'{palabra.capitalize()}' aparece: {count} veces")
    
    return resultados

def palabras_mas_frecuentes(contenido, top=10):
    print(f"\n{'='*60}")
    print(f"5. TOP {top} PALABRAS MÁS FRECUENTES")
    print(f"{'='*60}")
    
    # Limpiar el texto: convertir a minúsculas y extraer solo palabras
    palabras = re.findall(r'\b[a-záéíóúñü]+\b', contenido.lower())
    
    # Palabras comunes a ignorar (artículos, preposiciones, etc.)
    palabras_comunes = {'de', 'la', 'que', 'el', 'en', 'y', 'a', 'los', 'del', 'se',
                        'las', 'por', 'un', 'para', 'con', 'no', 'una', 'su', 'al',
                        'lo', 'como', 'más', 'pero', 'sus', 'le', 'ya', 'o', 'este',
                        'sí', 'porque', 'esta', 'entre', 'cuando', 'muy', 'sin', 'sobre',
                        'también', 'me', 'hasta', 'hay', 'donde', 'quien', 'desde', 'todo',
                        'nos', 'durante', 'todos', 'uno', 'les', 'ni', 'contra', 'otros',
                        'ese', 'eso', 'ante', 'ellos', 'e', 'esto', 'mí', 'antes', 'algunos',
                        'qué', 'unos', 'yo', 'otro', 'otras', 'otra', 'él', 'tanto', 'esa',
                        'estos', 'mucho', 'quienes', 'nada', 'muchos', 'cual', 'poco', 'ella',
                        'estar', 'estas', 'algo', 'nosotros', 'mi', 'mis', 'tú', 'te', 'ti',
                        'tu', 'tus', 'ellas', 'nosotras', 'vosotros', 'vosotras', 'os', 'mío',
                        'mía', 'míos', 'mías', 'tuyo', 'tuya', 'tuyos', 'tuyas', 'suyo', 'suya',
                        'suyos', 'suyas', 'nuestro', 'nuestra', 'nuestros', 'nuestras', 'vuestro',
                        'vuestra', 'vuestros', 'vuestras', 'esos', 'esas', 'ha', 'he', 'sido',
                        'fue', 'ser', 'era'}
    
    # Filtrar palabras comunes
    palabras_filtradas = [p for p in palabras if p not in palabras_comunes and len(p) > 2]
    
    # Contar frecuencias
    contador = Counter(palabras_filtradas)
    mas_comunes = contador.most_common(top)
    
    print(f"\n{'Posición':<10} {'Palabra':<20} {'Frecuencia':<10}")
    print(f"{'-'*40}")
    for i, (palabra, freq) in enumerate(mas_comunes, 1):
        print(f"{i:<10} {palabra:<20} {freq:<10}")
    
    return mas_comunes

def indice_palabras_frecuentes(contenido, top=20):
    print(f"\n{'='*60}")
    print(f"6. ÍNDICE DE PALABRAS FRECUENTES (Primera aparición)")
    print(f"{'='*60}")
    
    # Dividir en líneas
    lineas = contenido.split('\n')
    
    # Extraer palabras más frecuentes (excluyendo comunes)
    palabras = re.findall(r'\b[a-záéíóúñü]+\b', contenido.lower())
    palabras_comunes = {'de', 'la', 'que', 'el', 'en', 'y', 'a', 'los', 'del', 'se',
                        'las', 'por', 'un', 'para', 'con', 'no', 'una', 'su', 'al',
                        'lo', 'como', 'más', 'pero', 'sus', 'le', 'ya', 'o', 'este'}
    palabras_filtradas = [p for p in palabras if p not in palabras_comunes and len(p) > 3]
    contador = Counter(palabras_filtradas)
    mas_comunes = contador.most_common(top)
    
    print(f"\n{'Palabra':<20} {'Frecuencia':<12} {'Primera línea':<10}")
    print(f"{'-'*60}")
    
    for palabra, freq in mas_comunes:
        # Buscar en qué línea aparece por primera vez
        for num_linea, linea in enumerate(lineas, 1):
            if palabra in linea.lower():
                print(f"{palabra:<20} {freq:<12} Línea {num_linea}")
                break

def longitud_media_palabras(contenido):
    print(f"\n{'='*60}")
    print(f"7. LONGITUD MEDIA DE LAS PALABRAS")
    print(f"{'='*60}")
    
    # Extraer solo palabras (sin números ni signos)
    palabras = re.findall(r'\b[a-záéíóúñü]+\b', contenido.lower())
    
    if not palabras:
        print("No se encontraron palabras.")
        return 0
    
    longitud_total = sum(len(palabra) for palabra in palabras)
    longitud_media = longitud_total / len(palabras)
    
    print(f"Total de palabras analizadas: {len(palabras)}")
    print(f"Longitud media: {longitud_media:.2f} caracteres")
    
    return longitud_media

def frases_mas_largas(contenido, top=5):
    print(f"\n{'='*60}")
    print(f"8. LAS {top} FRASES MÁS LARGAS")
    print(f"{'='*60}")
    
    # Dividir por puntos, signos de exclamación o interrogación
    frases = re.split(r'[.!?]+', contenido)
    
    # Limpiar espacios y filtrar frases vacías
    frases_limpias = [f.strip() for f in frases if f.strip()]
    
    # Ordenar por longitud (de mayor a menor)
    frases_ordenadas = sorted(frases_limpias, key=len, reverse=True)
    
    print()
    for i, frase in enumerate(frases_ordenadas[:top], 1):
        print(f"\n{i}. ({len(frase)} caracteres)")
        print(f"{'-'*60}")
        # Mostrar solo los primeros 200 caracteres si es muy larga
        if len(frase) > 200:
            print(f"{frase[:200]}...")
        else:
            print(frase)

def mostrar_menu():
    print(f"\n╔{'═'*58}╗")
    print(f"║{'ANÁLISIS DEL QUIJOTE - Menú de Ejercicios':^58}║")
    print(f"╚{'═'*58}╝")
    print(f"1.  Contar total de palabras")
    print(f"2.  Contar apariciones de 'Capítulo'")
    print(f"3.  Crear archivos por capítulo")
    print(f"4.  Contar palabras específicas (Dulcinea, Quijote, Sancho)")
    print(f"5.  Top 10 palabras más frecuentes")
    print(f"6.  Índice de palabras frecuentes")
    print(f"7.  Longitud media de palabras")
    print(f"8.  Las 5 frases más largas")
    print(f"9.  Ejecutar todos los ejercicios")
    print(f"0.  Salir")
    print(f"{'='*60}")

def main():
    # Cargar el archivo al inicio
    print("Cargando El Quijote...")
    contenido = cargar_archivo()
    
    if contenido is None:
        print("\nNo se pudo cargar el archivo. Asegúrate de que 'el_quijote.txt' está en la misma carpeta.")
        return
    
    print("Archivo cargado correctamente.\n")
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (0-9): ").strip()
        
        if opcion == '1':
            contar_palabras_totales(contenido)
        elif opcion == '2':
            contar_palabra_capitulo(contenido)
        elif opcion == '3':
            crear_archivos_por_capitulo(contenido)
        elif opcion == '4':
            contar_palabras_especificas(contenido)
        elif opcion == '5':
            palabras_mas_frecuentes(contenido)
        elif opcion == '6':
            indice_palabras_frecuentes(contenido)
        elif opcion == '7':
            longitud_media_palabras(contenido)
        elif opcion == '8':
            frases_mas_largas(contenido)
        elif opcion == '9':
            print("\nEJECUTANDO TODOS LOS EJERCICIOS...\n")
            contar_palabras_totales(contenido)
            contar_palabra_capitulo(contenido)
            crear_archivos_por_capitulo(contenido)
            contar_palabras_especificas(contenido)
            palabras_mas_frecuentes(contenido)
            indice_palabras_frecuentes(contenido)
            longitud_media_palabras(contenido)
            frases_mas_largas(contenido)
        elif opcion == '0':
            print("\n¡Hasta luego! Gracias por usar el analizador del Quijote.")
            break
        else:
            print("\nOpción no válida. Por favor, seleccione una opción del 0 al 9.")
        
        input("\nPresione Enter para continuar...")
        limpiar_consola()

# Ejecutar el programa
if __name__ == "__main__":
    main()