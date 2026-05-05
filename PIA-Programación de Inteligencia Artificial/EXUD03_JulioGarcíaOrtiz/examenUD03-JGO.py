import hashlib
import json
import csv
import os
import random
from datetime import datetime, timedelta

CARPETA        = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_CSV    = os.path.join(CARPETA, "nube_datos_iot.csv")
ARCHIVO_JSON   = os.path.join(CARPETA, "nube_datos_iot.json")
ARCHIVO_CADENA = os.path.join(CARPETA, "cadena_blockchain_iot.txt")

NUM_REGISTROS   = 24
PROB_CORRUPCION = 0.3


def generar_lecturas_iot():
    """Genera NUM_REGISTROS lecturas horarias de temperatura interior, exterior y humedad."""
    inicio = datetime(2026, 5, 5, 0, 0, 0)
    lecturas = []
    for h in range(NUM_REGISTROS):
        lecturas.append({
            "id":            h + 1,
            "timestamp":     (inicio + timedelta(hours=h)).strftime("%Y-%m-%d %H:%M"),
            "temp_interior": round(random.uniform(17.0, 28.0), 1),
            "temp_exterior": round(random.uniform(5.0,  25.0), 1),
            "humedad":       round(random.uniform(30.0, 75.0), 1),
        })
    return lecturas


def guardar_en_nube(lecturas):
    """Guarda las lecturas IoT en CSV y JSON simulando un servicio en la nube."""
    campos = ["id", "timestamp", "temp_interior", "temp_exterior", "humedad"]
    with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(lecturas)
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(lecturas, f, indent=4, ensure_ascii=False)
    print(f"  {len(lecturas)} lecturas guardadas -> {ARCHIVO_CSV}")


def calcular_hash(contenido):
    """Devuelve el hash SHA-256 de una cadena de texto."""
    return hashlib.sha256(contenido.encode()).hexdigest()


def crear_bloque(lectura, hash_anterior):
    """Crea un bloque blockchain a partir de una lectura IoT y el hash del bloque anterior."""
    bloque = {
        "id":            lectura["id"],
        "timestamp":     lectura["timestamp"],
        "temp_interior": lectura["temp_interior"],
        "temp_exterior": lectura["temp_exterior"],
        "humedad":       lectura["humedad"],
        "hash_anterior": hash_anterior,
        "estado":        "OK",
    }
    bloque["hash"] = calcular_hash(json.dumps(
        {k: v for k, v in bloque.items() if k != "estado"}, sort_keys=True
    ))
    return bloque


def corromper_bloque(bloque):
    """Altera el hash del bloque para simular una corrupcion de datos."""
    bloque["hash"] = "CORROMPIDO_" + bloque["hash"][11:]
    bloque["estado"] = "CORROMPIDO"


def verificar_cadena(cadena):
    """Recorre la cadena bloque a bloque y comprueba si el hash y el encadenamiento son validos."""
    resultados = []
    hash_anterior_esperado = "0" * 64

    for bloque in cadena:
        copia = {k: v for k, v in bloque.items() if k not in ("hash", "estado")}
        hash_recalculado = calcular_hash(json.dumps(copia, sort_keys=True))

        hash_ok   = bloque["hash"] == hash_recalculado
        enlace_ok = bloque["hash_anterior"] == hash_anterior_esperado

        if hash_ok and enlace_ok:
            estado = "OK"
        elif not hash_ok:
            estado = "HASH CORRUPTO"
        else:
            estado = "ENLACE ROTO"

        resultados.append({
            "id":        bloque["id"],
            "timestamp": bloque["timestamp"],
            "estado":    estado,
        })
        hash_anterior_esperado = bloque["hash"]

    return resultados


def guardar_cadena_txt(cadena, resultados):
    """Guarda en un fichero TXT los hashes almacenados y la verificacion de integridad."""
    cadena_valida = all(r["estado"] == "OK" for r in resultados)

    with open(ARCHIVO_CADENA, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("SIMULACION: IoT + CLOUD + BLOCKCHAIN\n")
        f.write(f"Generado: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
        f.write("=" * 60 + "\n\n")

        f.write("HASHES ALMACENADOS EN LA CADENA\n")
        f.write("-" * 60 + "\n\n")
        for b in cadena:
            f.write(f"#{b['id']:<3} {b['timestamp']}  [{b['estado']}]\n")
            f.write(f"     T.Int={b['temp_interior']}C  T.Ext={b['temp_exterior']}C  Hum={b['humedad']}%\n")
            f.write(f"     Hash ant.: {b['hash_anterior'][:45]}...\n")
            f.write(f"     Hash      : {b['hash'][:45]}...\n")
            f.write("\n")

        f.write("=" * 60 + "\n")
        f.write("VERIFICACION DE INTEGRIDAD\n")
        f.write("-" * 60 + "\n\n")
        for r in resultados:
            f.write(f"  #{r['id']:<3} {r['timestamp']}  {r['estado']}\n")
        f.write("\n")
        if cadena_valida:
            f.write("  -> Blockchain integra. Todos los bloques son validos.\n")
        else:
            corrompidos = [r["id"] for r in resultados if r["estado"] != "OK"]
            f.write(f"  -> Blockchain corrompida. Bloques con problemas: {corrompidos}\n")


# =============================================================================
# PROGRAMA PRINCIPAL
# =============================================================================

print("=" * 60)
print("  ECOSISTEMA IoT + CLOUD + BLOCKCHAIN")
print("  Autor: Julio Garcia Ortiz  |  EXUD03")
print("=" * 60)


# 1. Generar lecturas IoT
print("\nLECTURA DE SENSORES IoT\n")
lecturas = generar_lecturas_iot()

print(f"  {'#':<4} {'Timestamp':<18} {'T. Interior':>12} {'T. Exterior':>12} {'Humedad':>9}")
print("  " + "-" * 60)
for l in lecturas:
    print(f"  {l['id']:<4} {l['timestamp']:<18} "
          f"{l['temp_interior']:>10}C  "
          f"{l['temp_exterior']:>10}C  "
          f"{l['humedad']:>7}%")


# 2. Enviar a la nube
print(f"\n{'=' * 60}")
print("ENVIO A LA NUBE\n")
guardar_en_nube(lecturas)


# 3. Crear un bloque por cada lectura y corromper aleatoriamente
print(f"\n{'=' * 60}")
print(f"REGISTRO EN BLOCKCHAIN  (prob. corrupcion: {int(PROB_CORRUPCION * 100)}%)\n")

cadena = []
hash_anterior = "0" * 64

for lectura in lecturas:
    bloque = crear_bloque(lectura, hash_anterior)
    if random.random() < PROB_CORRUPCION:
        corromper_bloque(bloque)
    cadena.append(bloque)
    hash_anterior = bloque["hash"]
    print(f"  #{bloque['id']:<3} {bloque['timestamp']}  [{bloque['estado']}]")
    print(f"       Hash: {bloque['hash'][:50]}...")
    print()


# 4. Verificar integridad
print("=" * 60)
print("VERIFICACION DE INTEGRIDAD\n")

resultados = verificar_cadena(cadena)
cadena_valida = all(r["estado"] == "OK" for r in resultados)

for r in resultados:
    print(f"  #{r['id']:<3} {r['timestamp']}  {r['estado']}")

if cadena_valida:
    print("\n  -> Blockchain integra. Todos los bloques son validos.")
else:
    corrompidos = [r["id"] for r in resultados if r["estado"] != "OK"]
    print(f"\n  -> Blockchain corrompida. Bloques con problemas: {corrompidos}")


# 5. Guardar TXT
print(f"\n{'=' * 60}")
guardar_cadena_txt(cadena, resultados)
print(f"  Blockchain guardada en: {ARCHIVO_CADENA}")
print("=" * 60)
