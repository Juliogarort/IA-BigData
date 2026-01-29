"""
Chatbot de Fórmula 1 con Reglas y Respuestas Basadas en Similaridad
Autor: Julio García
Fecha: 29/01/2026

Este chatbot responde preguntas sobre Fórmula 1, Fernando Alonso y Carlos Sainz Jr.
utilizando análisis de similitud de texto con TF-IDF y similitud del coseno.
"""

import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Descargar recursos necesarios de NLTK (ejecutar solo la primera vez)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# ============================================================================
# BASE DE CONOCIMIENTO: Preguntas y Respuestas Predefinidas sobre F1
# ============================================================================

# Lista de preguntas predefinidas (mínimo 10 pares)
preguntas_base = [
    "¿Quién es Fernando Alonso?",
    "¿Cuántos campeonatos mundiales ha ganado Fernando Alonso?",
    "¿En qué equipo corre Fernando Alonso actualmente?",
    "¿Cuál es la nacionalidad de Fernando Alonso?",
    "¿Quién es Carlos Sainz Jr?",
    "¿En qué equipo corre Carlos Sainz Jr actualmente?",
    "¿Cuántas victorias tiene Carlos Sainz Jr en F1?",
    "¿Qué es la Fórmula 1?",
    "¿Cuántos equipos hay en la Fórmula 1?",
    "¿Cuál es el circuito más rápido de F1?",
    "¿Quién tiene más campeonatos mundiales en F1?",
    "¿Cuál es el equipo más exitoso de la historia de F1?",
    "¿Qué significa DRS en Fórmula 1?",
    "¿Cuántos puntos se dan por ganar una carrera?",
    "¿Qué relación tienen Fernando Alonso y Carlos Sainz?"
]

# Respuestas correspondientes a cada pregunta
respuestas_base = [
    "Fernando Alonso es un piloto español de Fórmula 1, considerado uno de los mejores de la historia. Nació en Oviedo en 1981 y es bicampeón mundial de F1.",
    "Fernando Alonso ha ganado 2 campeonatos mundiales de Fórmula 1, en 2005 y 2006 con el equipo Renault.",
    "Fernando Alonso corre actualmente para el equipo Aston Martin desde la temporada 2023.",
    "Fernando Alonso es español, nacido en Oviedo, Asturias.",
    "Carlos Sainz Jr es un piloto español de Fórmula 1, hijo del legendario piloto de rallies Carlos Sainz. Nació en Madrid en 1994.",
    "Carlos Sainz Jr corre actualmente para el equipo Ferrari desde la temporada 2021.",
    "Carlos Sainz Jr ha conseguido 3 victorias en Fórmula 1: Gran Bretaña 2022, Singapur 2023 y Australia 2024.",
    "La Fórmula 1 es la máxima categoría del automovilismo mundial, donde compiten los mejores pilotos en monoplazas de alta tecnología.",
    "En la Fórmula 1 hay 10 equipos, cada uno con 2 pilotos, sumando un total de 20 pilotos en la parrilla.",
    "El circuito más rápido de F1 es Monza en Italia, conocido como el 'Templo de la Velocidad', donde se alcanzan velocidades superiores a 350 km/h.",
    "Lewis Hamilton y Michael Schumacher comparten el récord con 7 campeonatos mundiales cada uno.",
    "Ferrari es el equipo más exitoso de la historia de F1, con 16 campeonatos de constructores y múltiples títulos de pilotos.",
    "DRS significa 'Drag Reduction System' (Sistema de Reducción de Resistencia). Es un alerón trasero móvil que reduce la resistencia aerodinámica para facilitar los adelantamientos.",
    "Por ganar una carrera se otorgan 25 puntos al piloto ganador. El segundo lugar recibe 18 puntos y el tercero 15 puntos.",
    "Fernando Alonso y Carlos Sainz Jr son ambos pilotos españoles de F1. Alonso es una inspiración para Sainz, quien lo considera un referente. Ambos han representado con orgullo a España en la máxima categoría."
]

# ============================================================================
# FUNCIONES DEL CHATBOT
# ============================================================================

def calcular_similitud(pregunta_usuario, preguntas_base):
    """
    Calcula la similitud entre la pregunta del usuario y las preguntas predefinidas
    utilizando TF-IDF y similitud del coseno.
    
    Args:
        pregunta_usuario (str): Pregunta introducida por el usuario
        preguntas_base (list): Lista de preguntas predefinidas
    
    Returns:
        tuple: (índice de la pregunta más similar, valor de similitud)
    """
    # Crear el vectorizador TF-IDF con mejores parametros
    # TF-IDF convierte el texto en vectores numéricos basados en la frecuencia de términos
    # ngram_range=(1,2) permite capturar palabras individuales y pares de palabras
    # token_pattern permite palabras con acentos y caracteres especiales
    vectorizador = TfidfVectorizer(
        lowercase=True, 
        ngram_range=(1, 2),
        token_pattern=r'\b\w+\b'
    )
    
    # Combinar la pregunta del usuario con todas las preguntas base
    todas_preguntas = [pregunta_usuario] + preguntas_base
    
    # Transformar todas las preguntas en vectores TF-IDF
    vectores_tfidf = vectorizador.fit_transform(todas_preguntas)
    
    # Calcular la similitud del coseno entre la pregunta del usuario (índice 0)
    # y todas las preguntas predefinidas (índices 1 en adelante)
    similitudes = cosine_similarity(vectores_tfidf[0:1], vectores_tfidf[1:])
    
    # Encontrar el índice de la pregunta con mayor similitud
    indice_max_similitud = np.argmax(similitudes)
    
    # Obtener el valor de similitud máximo
    valor_similitud = similitudes[0][indice_max_similitud]
    
    return indice_max_similitud, valor_similitud


def obtener_respuesta(pregunta_usuario, umbral_similitud=0.3):
    """
    Obtiene la respuesta más adecuada basándose en la similitud de la pregunta.
    
    Args:
        pregunta_usuario (str): Pregunta del usuario
        umbral_similitud (float): Umbral mínimo de similitud (por defecto 0.3 = 30%)
    
    Returns:
        str: Respuesta del chatbot
    """
    # Calcular la similitud con las preguntas predefinidas
    indice, similitud = calcular_similitud(pregunta_usuario, preguntas_base)
    
    # Si la similitud es alta (mayor al umbral), devolver la respuesta correspondiente
    if similitud >= umbral_similitud:
        return respuestas_base[indice]
    else:
        # Si la similitud es baja, indicar que no se entiende la pregunta
        return "No entiendo tu pregunta, intenta reformularla. Puedo responder sobre Fórmula 1, Fernando Alonso y Carlos Sainz Jr."


def mostrar_bienvenida():
    """
    Muestra el mensaje de bienvenida del chatbot.
    """
    print("=" * 70)
    print("  CHATBOT DE FORMULA 1 - Fernando Alonso & Carlos Sainz Jr")
    print("=" * 70)
    print("\nHola! Soy un chatbot especializado en Formula 1.")
    print("Puedo responder preguntas sobre:")
    print("  - Formula 1 en general")
    print("  - Fernando Alonso")
    print("  - Carlos Sainz Jr")
    print("\nEscribe 'salir' para terminar la conversacion.")
    print("=" * 70 + "\n")


def ejecutar_chatbot():
    """
    Función principal que ejecuta el bucle del chatbot.
    Permite al usuario hacer múltiples preguntas hasta que escriba 'salir'.
    """
    mostrar_bienvenida()
    
    # Contador de interacciones para el informe
    interacciones = []
    
    # Bucle principal del chatbot
    while True:
        # Solicitar pregunta al usuario
        pregunta = input("Tu pregunta: ").strip()
        
        # Verificar si el usuario quiere salir
        if pregunta.lower() == 'salir':
            print("\n" + "=" * 70)
            print("Gracias por usar el chatbot de F1! Hasta pronto!")
            print("=" * 70)
            break
        
        # Validar que la pregunta no esté vacía
        if not pregunta:
            print("Por favor, escribe una pregunta valida.\n")
            continue
        
        # Obtener y mostrar la respuesta
        respuesta = obtener_respuesta(pregunta)
        print(f"\nRespuesta: {respuesta}\n")
        print("-" * 70 + "\n")
        
        # Guardar la interacción para el informe
        interacciones.append({
            'pregunta': pregunta,
            'respuesta': respuesta
        })
    
    # Generar informe de interacciones
    generar_informe(interacciones)


def generar_informe(interacciones):
    """
    Genera un informe con ejemplos de interacción del chatbot.
    
    Args:
        interacciones (list): Lista de diccionarios con preguntas y respuestas
    """
    if not interacciones:
        return
    
    print("\n" + "=" * 70)
    print("INFORME DE INTERACCIONES")
    print("=" * 70)
    print(f"\nTotal de preguntas realizadas: {len(interacciones)}\n")
    
    for i, interaccion in enumerate(interacciones, 1):
        print(f"Interacción {i}:")
        print(f"  Pregunta: {interaccion['pregunta']}")
        print(f"  Respuesta: {interaccion['respuesta'][:100]}...")
        print()
    
    print("=" * 70)


# ============================================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================================

if __name__ == "__main__":
    """
    Punto de entrada principal del programa.
    Ejecuta el chatbot cuando se ejecuta el script directamente.
    """
    ejecutar_chatbot()
