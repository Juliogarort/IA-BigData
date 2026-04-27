import os
import csv

# Nombre del archivo CSV y del reporte de salida
ARCHIVO_CSV = "incidentes.csv"
ARCHIVO_SALIDA = "informe_incidentes.txt"

# Reglas del sistema experto
REGLAS = [
    {"id": "R1", "if": ["adjunto_sospechoso", "macro_activa"], "then": "phishing_probable", "op": "AND"},
    {"id": "R2", "if": ["antivirus_alerta", "ejecucion_binario"], "then": "malware_probable", "op": "AND"},
    {"id": "R3", "if": ["intentos_login_altos", "pais_inusual"], "then": "compromiso_cuenta_probable", "op": "AND"},
    {"id": "R4", "if": ["acceso_fuera_horario", "multiples_hosts"], "then": "movimiento_lateral_probable", "op": "AND"},
    {"id": "R5", "if": ["descarga_masiva", "acceso_fuera_horario"], "then": "exfiltracion_probable", "op": "AND"},
    {"id": "R6", "if": ["malware_probable", "movimiento_lateral_probable"], "then": "incidente_critico", "op": "AND"},
    {"id": "R7", "if": ["compromiso_cuenta_probable", "exfiltracion_probable"], "then": "incidente_critico", "op": "AND"},
    {"id": "R8", "if": ["phishing_probable", "compromiso_cuenta_probable"], "then": "acceso_inicial_exitoso", "op": "AND"},
    {"id": "R9", "if": ["acceso_inicial_exitoso", "malware_probable"], "then": "ataque_multietapa", "op": "AND"},
    {"id": "R10", "if": ["ataque_multietapa"], "then": "respuesta_prioritaria", "op": "OR"},
    {"id": "R11", "if": ["incidente_critico"], "then": "respuesta_prioritaria", "op": "OR"},
]

CAMPOS_OBLIGATORIOS = [
    "id_evento", "usuario", "ip_reputacion", "pais_inusual", "intentos_login",
    "adjunto_sospechoso", "macro_activa", "ejecucion_binario",
    "acceso_fuera_horario", "volumen_descarga_mb", "multiples_hosts",
    "antivirus_alerta"
]

def limpiar_valor(valor):
    return str(valor).strip().lower()

def es_si(valor):
    return limpiar_valor(valor) == "si"

def validar_fila(fila):
    errores = []
    for campo in CAMPOS_OBLIGATORIOS:
        if campo not in fila: errores.append(f"Falta {campo}")
    return len(errores) == 0, errores

def cargar_csv():
    # Obtener la ruta del directorio donde está el script
    base_path = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.join(base_path, ARCHIVO_CSV)
    
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"No se encuentra {ARCHIVO_CSV} en {base_path}")

    casos = []
    with open(ruta, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            hechos = set()
            if es_si(fila["pais_inusual"]): hechos.add("pais_inusual")
            if es_si(fila["adjunto_sospechoso"]): hechos.add("adjunto_sospechoso")
            if es_si(fila["macro_activa"]): hechos.add("macro_activa")
            if es_si(fila["ejecucion_binario"]): hechos.add("ejecucion_binario")
            if es_si(fila["acceso_fuera_horario"]): hechos.add("acceso_fuera_horario")
            if es_si(fila["multiples_hosts"]): hechos.add("multiples_hosts")
            if es_si(fila["antivirus_alerta"]): hechos.add("antivirus_alerta")
            if int(fila["intentos_login"]) > 5: hechos.add("intentos_login_altos")
            if float(fila["volumen_descarga_mb"]) > 1000: hechos.add("descarga_masiva")
            
            casos.append({"id": fila["id_evento"], "usuario": fila["usuario"], "hechos": hechos})
    return casos

def forward_chaining(hechos_iniciales):
    hechos = set(hechos_iniciales)
    inferidos, usadas = [], []
    cambio = True
    while cambio:
        cambio = False
        for regla in REGLAS:
            if regla["then"] not in hechos:
                cond = all(p in hechos for p in regla["if"]) if regla["op"] == "AND" else any(p in hechos for p in regla["if"])
                if cond:
                    hechos.add(regla["then"])
                    inferidos.append(regla["then"])
                    usadas.append(regla["id"])
                    cambio = True
    return hechos, inferidos, usadas

def backward_chaining(obj, hechos, visitados=None):
    if visitados is None: visitados = set()
    if obj in hechos: return True
    if obj in visitados: return False
    visitados.add(obj)
    for regla in REGLAS:
        if regla["then"] == obj:
            if all(backward_chaining(p, hechos, visitados) for p in regla["if"]) if regla["op"] == "AND" else any(backward_chaining(p, hechos, visitados) for p in regla["if"]):
                return True
    return False

def generar_texto_informe(caso):
    hechos_finales, inferidos, reglas_usadas = forward_chaining(caso["hechos"])
    objetivos = ["incidente_critico", "ataque_multietapa", "respuesta_prioritaria"]
    
    # Cabecera
    txt = f"\n==============================\nIncidente {caso['id']} - Usuario: {caso['usuario']}\n==============================\n"
    
    # Hechos iniciales
    txt += "\nHechos iniciales:\n" + ("\n".join([f"- {h}" for h in sorted(caso['hechos'])]) if caso['hechos'] else "- (ninguno)")
    
    # Inferencia Forward
    txt += "\n\nInferencia Forward:\n" + ("\n".join([f"- {h}" for h in inferidos]) if inferidos else "- (ninguna inferencia)")
    
    # Consultas Backward
    txt += "\n\nConsultas Backward:\n" + "\n".join([f"- {obj}: {'VERDADERO' if backward_chaining(obj, caso['hechos']) else 'FALSO'}" for obj in objetivos])
    
    # Explicación de reglas disparadas
    txt += "\n\nExplicación:\n"
    if reglas_usadas:
        for rid in reglas_usadas:
            regla = next(r for r in REGLAS if r["id"] == rid)
            op = regla["op"]
            txt += f"{rid}: {f' {op} '.join(regla['if'])} -> {regla['then']}\n"
    else:
        txt += "- No se ha disparado ninguna regla\n"
    
    # Recomendación
    txt += "\nRecomendación:\n"
    if "respuesta_prioritaria" in hechos_finales:
        txt += "- Activar respuesta prioritaria\n- Escalar al SOC\n- Aislar el equipo afectado\n- Forzar cambio de credenciales\n"
    elif "incidente_critico" in hechos_finales:
        txt += "- Escalar al SOC\n- Revisar contención y erradicación\n"
    elif inferidos:
        txt += "- Monitorización reforzada\n- Verificación manual por analista\n"
    else:
        txt += "- Sin acción urgente, revisar manualmente\n"
        
    return txt

def main():
    base_path = os.path.dirname(os.path.abspath(__file__))
    ruta_salida = os.path.join(base_path, ARCHIVO_SALIDA)
    casos = cargar_csv()
    
    with open(ruta_salida, "w", encoding="utf-8") as f:
        for caso in casos:
            informe = generar_texto_informe(caso)
            f.write(informe)
    print("")
    print("===================================================")
    print("")
    print(f"Se han procesado {len(casos)} incidentes.")
    print(f"Consulta el informe generado en el archivo llaamado: Informe_incidentes.txt")
    print("")
    print("===================================================")
    print("")
if __name__ == "__main__":
    main() 