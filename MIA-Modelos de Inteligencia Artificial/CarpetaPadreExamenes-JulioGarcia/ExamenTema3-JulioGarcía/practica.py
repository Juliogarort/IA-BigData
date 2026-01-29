import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ARCHIVO_TEXTO_ENTRADA = os.path.join(BASE_DIR, "HistoriaNaturalyMoral.txt")
ARCHIVO_IMAGEN = os.path.join(BASE_DIR, "nube_palabras.png")
ARCHIVO_PDF = os.path.join(BASE_DIR, "informe_resultados.pdf")


def leer_texto(archivo_entrada):
    """
    Lee un texto desde un archivo local.
    
    Args:
        archivo_entrada (str): Nombre del archivo a leer
    
    Returns:
        str: Contenido del texto leído
    """
    print(f"[*] Leyendo texto desde '{archivo_entrada}'...")
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as f:
            texto = f.read()
        
        print(f"[OK] Texto leído correctamente ({len(texto)} caracteres)")
        return texto
    except Exception as e:
        print(f"[ERROR] Error al leer el archivo: {e}")
        return None

def limpiar_texto(texto):
    """
    Limpia el texto eliminando signos de puntuación y palabras vacías.
    
    Args:
        texto (str): Texto original a limpiar
    
    Returns:
        list: Lista de palabras limpias
    """
    print("\n[*] Limpiando el texto...")
    
    # Convertir a minúsculas
    texto = texto.lower()
    
    # Eliminar signos de puntuación y caracteres especiales
    texto = re.sub(r'[^\w\s]', ' ', texto)
    texto = re.sub(r'\d+', '', texto)  # Eliminar números
    
    # Tokenizar (dividir en palabras)
    palabras = texto.split()
    
    # Obtener stopwords en español
    try:
        stop_words = set(stopwords.words('spanish'))
    except:
        print("⚠️ Descargando stopwords...")
        nltk.download('stopwords')
        stop_words = set(stopwords.words('spanish'))
    
    # Añadir stopwords adicionales específicas del texto
    stop_words.update(['don', 'doña', 'señor', 'señora', 'capítulo', 'parte'])
    
    # Filtrar palabras vacías y palabras muy cortas
    palabras_limpias = [palabra for palabra in palabras 
                        if palabra not in stop_words and len(palabra) > 3]
    
    print(f"[OK] Texto limpiado: {len(palabras_limpias)} palabras válidas")
    return palabras_limpias

def contar_frecuencias(palabras):
    """
    Cuenta la frecuencia de aparición de cada palabra.
    
    Args:
        palabras (list): Lista de palabras
    
    Returns:
        Counter: Objeto Counter con las frecuencias
    """
    print("\n[*] Contando frecuencias de palabras...")
    frecuencias = Counter(palabras)
    print(f"[OK] Se encontraron {len(frecuencias)} palabras únicas")
    return frecuencias

def mostrar_top_palabras(frecuencias, n=20):
    """
    Muestra las N palabras más frecuentes.
    
    Args:
        frecuencias (Counter): Contador de frecuencias
        n (int): Número de palabras a mostrar
    """
    print(f"\n[TOP {n}] Palabras más frecuentes:")
    print("-" * 50)
    for palabra, freq in frecuencias.most_common(n):
        print(f"{palabra:20} : {freq:5} veces")
    print("-" * 50)

def generar_nube_palabras(frecuencias, archivo_salida):
    """
    Genera una nube de palabras y la guarda como imagen.
    
    Args:
        frecuencias (Counter): Contador de frecuencias
        archivo_salida (str): Nombre del archivo de imagen
    """
    print(f"\n[*] Generando nube de palabras...")
    
    # Crear la nube de palabras
    wordcloud = WordCloud(
        width=1600,
        height=800,
        background_color='white',
        colormap='viridis',
        max_words=150,
        relative_scaling=0.5,
        min_font_size=10
    ).generate_from_frequencies(frecuencias)
    
    # Crear la figura
    plt.figure(figsize=(20, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Nube de Palabras - Análisis de Frecuencias', 
              fontsize=24, fontweight='bold', pad=20)
    
    # Guardar la imagen
    plt.savefig(archivo_salida, dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    print(f"[OK] Nube de palabras guardada en '{archivo_salida}'")
    
    # Mostrar la imagen
    plt.show()

def generar_informe_pdf(frecuencias, archivo_pdf):
    """
    Genera un informe en PDF con los resultados del análisis.
    
    Args:
        frecuencias (Counter): Contador de frecuencias
        archivo_pdf (str): Nombre del archivo PDF
    """
    print(f"\n[*] Generando informe PDF...")
    
    # Crear el documento PDF
    doc = SimpleDocTemplate(archivo_pdf, pagesize=letter,
                           rightMargin=72, leftMargin=72,
                           topMargin=72, bottomMargin=18)
    
    # Contenedor para los elementos del PDF
    elementos = []
    
    # Estilos
    estilos = getSampleStyleSheet()
    estilo_titulo = ParagraphStyle(
        'CustomTitle',
        parent=estilos['Heading1'],
        fontSize=24,
        textColor='#2C3E50',
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    estilo_subtitulo = ParagraphStyle(
        'CustomSubtitle',
        parent=estilos['Heading2'],
        fontSize=16,
        textColor='#34495E',
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    estilo_normal = ParagraphStyle(
        'CustomNormal',
        parent=estilos['BodyText'],
        fontSize=11,
        alignment=TA_JUSTIFY,
        spaceAfter=12
    )
    
    # Título
    elementos.append(Paragraph("Análisis de Texto y Nube de Palabras", estilo_titulo))
    elementos.append(Paragraph("Examen Tema 3 - MIA", estilos['Heading3']))
    elementos.append(Paragraph("Julio García", estilos['Normal']))
    elementos.append(Spacer(1, 0.3*inch))
    
    # Introducción
    elementos.append(Paragraph("1. Introducción", estilo_subtitulo))
    intro_text = """
    Este informe presenta los resultados del análisis de frecuencia de palabras realizado
    sobre un texto de dominio público descargado desde Project Gutenberg. El objetivo es
    identificar los términos más utilizados y representarlos visualmente mediante una nube
    de palabras.
    """
    elementos.append(Paragraph(intro_text, estilo_normal))
    elementos.append(Spacer(1, 0.2*inch))
    
    # Metodología
    elementos.append(Paragraph("2. Metodología", estilo_subtitulo))
    metodologia_text = f"""
    <b>Fuente de datos:</b> Se analizó el texto "{ARCHIVO_TEXTO_ENTRADA}", un documento
    de dominio público sobre historia natural y moral.<br/><br/>
    
    <b>Procesamiento del texto:</b><br/>
    • Conversión a minúsculas<br/>
    • Eliminación de signos de puntuación y números<br/>
    • Tokenización del texto<br/>
    • Filtrado de palabras vacías (stopwords) en español<br/>
    • Eliminación de palabras con menos de 4 caracteres<br/><br/>
    
    <b>Herramientas utilizadas:</b><br/>
    • Python 3.10<br/>
    • NLTK (Natural Language Toolkit)<br/>
    • WordCloud<br/>
    • Matplotlib<br/>
    • Collections (Counter)<br/>
    """
    elementos.append(Paragraph(metodologia_text, estilo_normal))
    elementos.append(Spacer(1, 0.2*inch))
    
    # Resultados
    elementos.append(Paragraph("3. Resultados", estilo_subtitulo))
    
    # Estadísticas
    total_palabras = sum(frecuencias.values())
    palabras_unicas = len(frecuencias)
    top_10 = frecuencias.most_common(10)
    
    stats_text = f"""
    <b>Estadísticas generales:</b><br/>
    • Total de palabras procesadas: {total_palabras:,}<br/>
    • Palabras únicas encontradas: {palabras_unicas:,}<br/>
    • Palabra más frecuente: "{top_10[0][0]}" ({top_10[0][1]} apariciones)<br/>
    """
    elementos.append(Paragraph(stats_text, estilo_normal))
    elementos.append(Spacer(1, 0.2*inch))
    
    # Top 10 palabras
    elementos.append(Paragraph("3.1. Palabras más frecuentes", estilo_subtitulo))
    top_text = "<br/>".join([f"{i+1}. <b>{palabra}</b>: {freq} veces" 
                             for i, (palabra, freq) in enumerate(top_10)])
    elementos.append(Paragraph(top_text, estilo_normal))
    elementos.append(Spacer(1, 0.3*inch))
    
    # Salto de página
    elementos.append(PageBreak())
    
    # Nube de palabras
    elementos.append(Paragraph("3.2. Visualización: Nube de Palabras", estilo_subtitulo))
    elementos.append(Spacer(1, 0.2*inch))
    
    # Insertar imagen
    try:
        img = Image(ARCHIVO_IMAGEN, width=6.5*inch, height=3.25*inch)
        elementos.append(img)
    except:
        elementos.append(Paragraph("Error: No se pudo cargar la imagen", estilos['Normal']))
    
    elementos.append(Spacer(1, 0.3*inch))
    
    # Conclusiones
    elementos.append(Paragraph("4. Conclusiones", estilo_subtitulo))
    conclusion_text = f"""
    El análisis de frecuencia de palabras ha permitido identificar los términos más
    relevantes en el texto analizado. La palabra más frecuente es "<b>{top_10[0][0]}</b>",
    con {top_10[0][1]} apariciones, lo cual refleja la temática central del documento.<br/><br/>
    
    La nube de palabras generada proporciona una representación visual intuitiva de la
    distribución de frecuencias, donde el tamaño de cada palabra es proporcional a su
    frecuencia de aparición. Esta técnica de visualización facilita la identificación
    rápida de los conceptos principales del texto.<br/><br/>
    
    Las herramientas de procesamiento de lenguaje natural (NLP) utilizadas, especialmente
    NLTK para la limpieza del texto y WordCloud para la visualización, han demostrado ser
    efectivas para este tipo de análisis textual.
    """
    elementos.append(Paragraph(conclusion_text, estilo_normal))
    
    # Construir el PDF
    doc.build(elementos)
    print(f"[OK] Informe PDF generado: '{archivo_pdf}'")

def main():
    """
    Función principal que ejecuta todo el proceso de análisis.
    """
    print("=" * 60)
    print("  ANALISIS DE TEXTO Y GENERACION DE NUBE DE PALABRAS")
    print("  Examen Tema 3 - MIA")
    print("  Autor: Julio Garcia")
    print("=" * 60)
    
    # 1. Leer el texto
    texto = leer_texto(ARCHIVO_TEXTO_ENTRADA)
    if not texto:
        print("\n[ERROR] No se pudo leer el archivo. Verifica que existe.")
        return
    
    # 2. Limpiar el texto
    palabras_limpias = limpiar_texto(texto)
    
    # 3. Contar frecuencias
    frecuencias = contar_frecuencias(palabras_limpias)
    
    # 4. Mostrar top palabras
    mostrar_top_palabras(frecuencias, 20)
    
    # 5. Generar nube de palabras
    generar_nube_palabras(frecuencias, ARCHIVO_IMAGEN)
    
    # 6. Generar informe PDF
    generar_informe_pdf(frecuencias, ARCHIVO_PDF)
    
    print("\n" + "=" * 60)
    print("[OK] Proceso completado exitosamente!")
    print("=" * 60)
    print(f"\nArchivos generados:")
    print(f"  - {ARCHIVO_IMAGEN}")
    print(f"  - {ARCHIVO_PDF}")
    print(f"\nArchivo analizado:")
    print(f"  - {ARCHIVO_TEXTO_ENTRADA}")
    print("\n")

if __name__ == "__main__":
    main()
