import hashlib
import random
import os
from datetime import datetime

# Esta clase llamada Bloque representaría lo que en el juego real serían los jugadores, indice representa al numero de cada jugador
# mensaje el mensaje que se pasa de jugador a jugador (puede estar cambiao o haber cometido algun error), hash_anterior representa la huella
# digital del mensaje anterior y el hash sería la nueva huella que genera el mensaje actual. 
class Bloque:
    def __init__(self, indice, mensaje, hash_anterior=""):
        self.indice = indice
        self.mensaje = mensaje
        self.hash_anterior = hash_anterior
        self.hash = self.calcular_hash()

    def calcular_hash(self):
        contenido = str(self.indice) + self.mensaje + self.hash_anterior
        return hashlib.sha256(contenido.encode()).hexdigest()

    def __str__(self):
        return f"Bloque #{self.indice}\nMensaje: {self.mensaje}\nHash anterior: {self.hash_anterior[:20]}...\nHash propio: {self.hash[:20]}...\n"

# Esta función simularía el error cometido por algun jugador. Como funciona? Pues hay una probabilidad del 30% de que se cometa un error, 
# si se comete el error, mediante este bucle de forma aleatoria se selecciona una posición y se sustituye alguna letra por otra tambien aleatoriamente
def distorsionar_mensaje(mensaje, probabilidad=0.3):
    if random.random() < probabilidad:
        posicion = random.randint(0, len(mensaje) - 1)
        caracter_random = random.choice("abcdefghijklmnopqrstuvwxyz!?#@")
        return mensaje[:posicion] + caracter_random + mensaje[posicion + 1:], True
    return mensaje, False

def crear_cadena(mensaje_inicial, num_personas=6, probabilidad_error=0.3):
    cadena = []
    mensaje_actual = mensaje_inicial
    hash_anterior = "0" * 64


    for i in range(num_personas):
        mensaje_actual, fue_alterado = distorsionar_mensaje(mensaje_actual, probabilidad_error)
        bloque = Bloque(i, mensaje_actual, hash_anterior)
        cadena.append(bloque)
        hash_anterior = bloque.hash
        
        estado = "⚠️   ALTERADO" if fue_alterado else "✅ Sin cambios"
        print(f"\nPersona {i+1} [{estado}]")
        print(f"Mensaje: {mensaje_actual}")
        print(f"Hash: {bloque.hash[:30]}...")

    return cadena

# Esta función verifica la cadena, compara el hash del mensaje anterior y el del mensaje actual, si son iguales bien
# pero si son diferentes nos muestra un mensaje de bloque corrupto. 
def verificar_cadena(cadena):
    print("\n" + "=" * 60)
    print("VERIFICACIÓN DE INTEGRIDAD")
    print("=" * 60)

    cadena_valida = True
    for i, bloque in enumerate(cadena):
        if bloque.hash != bloque.calcular_hash():
            print(f"❌ Bloque #{i+1}: hash corrupto")
            cadena_valida = False
        else:
            print(f"✅ Bloque #{i+1}: OK — {bloque.mensaje}")

        if i > 0 and bloque.hash_anterior != cadena[i-1].hash:
            print(f"⚠️ Bloque #{i+1}: hash_anterior no coincide")
            cadena_valida = False

    estado = "✅ ÍNTEGRA" if cadena_valida else "❌ CORROMPIDA"
    print(f"\n{estado}")
    return cadena_valida

# Esta función simularía el modo trampa, donde se modifica un mensaje de un bloque
# y se muestra un mensaje de bloque corrupto. 
def modo_trampa(cadena, indice_bloque, nuevo_mensaje):
    print("\n" + "=" * 60)
    print("MODO TRAMPA ACTIVADO")
    print("=" * 60)

    if 0 <= indice_bloque < len(cadena):
        bloque = cadena[indice_bloque]
        mensaje_original = bloque.mensaje
        bloque.mensaje = nuevo_mensaje
        
        print(f"Bloque #{indice_bloque}:")
        print(f"Antes: {mensaje_original}")
        print(f"Después: {nuevo_mensaje}")
        print("→ Cadena ahora corrupta")

# Esta función se encarga de reparar el bloque en caso de que esté roto, actualiza el hash anterior y recalcula su hash y para que siga funcionando
# el siguiente bloque usa el hash anterior que se ha recalculado y se repite hasta el final. 
def reparar_cadena(cadena):
    print("\n" + "=" * 60)
    print("REPARANDO CADENA")
    print("=" * 60)

    for i, bloque in enumerate(cadena):
        hash_anterior = "0" * 64 if i == 0 else cadena[i-1].hash
        bloque.hash_anterior = hash_anterior
        bloque.hash = bloque.calcular_hash()
        print(f"Bloque #{i+1} → Hash recalculado")

    print("✅ Cadena reparada (hashes coherentes)")

# En esta guardamos un archivo, usamos timestamp para guardar la ultima fecha de ejecución y cada bloque con sus mensajes y hashes de cada mensaje. 
def guardar_en_txt(cadena, nombre_archivo="cadena_bloques.txt"):
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), nombre_archivo)
    
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("SIMULACIÓN: TELÉFONO ESCACHARRADO CON BLOCKCHAIN\n")
        f.write(f"Generado: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
        f.write("=" * 60 + "\n\n")
        
        for bloque in cadena:
            f.write(str(bloque))
            f.write("\n")

    print(f"\n💾 Guardado en: {ruta}")


if __name__ == "__main__":
    MENSAJE_INICIAL = "Fernando Alonso es la cabra, the GOAT, la bestia, el animal, el padre, el mejor de la historia"
    NUM_PERSONAS = 6
    PROBABILIDAD_ERROR = 0.3

    cadena = crear_cadena(MENSAJE_INICIAL, NUM_PERSONAS, PROBABILIDAD_ERROR)
    
    verificar_cadena(cadena)
    guardar_en_txt(cadena)
    modo_trampa(cadena, 2, "Mensaje modificado a propósito")
    verificar_cadena(cadena)

    reparar_cadena(cadena)
    verificar_cadena(cadena)

    guardar_en_txt(cadena, "cadena_reparada.txt")