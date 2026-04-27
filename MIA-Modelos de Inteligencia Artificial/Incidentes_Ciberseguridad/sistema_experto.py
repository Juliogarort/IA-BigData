import os
import csv

# Nombre del archivo CSV que debe estar en la misma carpeta que este script
ARCHIVO_CSV = "incidentes.csv"

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

# Campos obligatorios del CSV
CAMPOS_OBLIGATORIOS = [
    "id_evento", "usuario", "ip_reputacion", "pais_inusual", "intentos_login",
    "adjunto_sospechoso", "macro_activa", "ejecucion_binario",
    "acceso_fuera_horario", "volumen_descarga_mb", "multiples_hosts",
    "antivirus_alerta"
]

def limpiar_valor(valor):
    # Normaliza textos para comparar sin problemas de mayúsculas o espacios.
    return str(valor).strip().lower()

def es_si(valor):
    # Devuelve True si el valor del CSV es 'si'.
    return limpiar_valor(valor) == "si"

def validar_fila(fila):
    # Comprueba que la fila tenga campos válidos y tipos correctos.
    errores = []

    for campo in CAMPOS_OBLIGATORIOS:
        if campo not in fila:
            errores.append(f"Falta el campo {campo}")

    if errores:
        return False, errores

    if not str(fila["id_evento"]).strip().isdigit():
        errores.append("id_evento debe ser entero")

    if not str(fila["usuario"]).strip():
        errores.append("usuario vacío")

    if limpiar_valor(fila["ip_reputacion"]) not in ["normal", "desconocida", "maliciosa"]:
        errores.append("ip_reputacion inválida")

    for campo in [
        "pais_inusual", "adjunto_sospechoso", "macro_activa",
        "ejecucion_binario", "acceso_fuera_horario",
        "multiples_hosts", "antivirus_alerta"
    ]:
        if limpiar_valor(fila[campo]) not in ["si", "no"]:
            errores.append(f"{campo} debe ser si o no")

    try:
        int(fila["intentos_login"])
    except:
        errores.append("intentos_login debe ser numérico")

    try:
        float(fila["volumen_descarga_mb"])
    except:
        errores.append("volumen_descarga_mb debe ser numérico")

    return len(errores) == 0, errores

def cargar_csv():
    # Lee el CSV, valida cada fila y la transforma en hechos iniciales.
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), ARCHIVO_CSV)

    if not os.path.exists(ruta):
        raise FileNotFoundError(f"No se encuentra {ARCHIVO_CSV} en la misma carpeta que el script.")

    casos = []

    with open(ruta, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)

        for fila in lector:
            ok, errores = validar_fila(fila)
            if not ok:
                raise ValueError(f"Error en la fila {fila.get('id_evento', '?')}: {errores}")

            hechos = set()

            # Hechos simples
            if es_si(fila["pais_inusual"]):
                hechos.add("pais_inusual")
            if es_si(fila["adjunto_sospechoso"]):
                hechos.add("adjunto_sospechoso")
            if es_si(fila["macro_activa"]):
                hechos.add("macro_activa")
            if es_si(fila["ejecucion_binario"]):
                hechos.add("ejecucion_binario")
            if es_si(fila["acceso_fuera_horario"]):
                hechos.add("acceso_fuera_horario")
            if es_si(fila["multiples_hosts"]):
                hechos.add("multiples_hosts")
            if es_si(fila["antivirus_alerta"]):
                hechos.add("antivirus_alerta")

            # Hechos derivados obligatorios
            if int(fila["intentos_login"]) > 5:
                hechos.add("intentos_login_altos")
            if float(fila["volumen_descarga_mb"]) > 1000:
                hechos.add("descarga_masiva")

            casos.append({
                "id_evento": int(fila["id_evento"]),
                "usuario": fila["usuario"].strip(),
                "hechos": hechos
            })

    return casos

def regla_cumplida(hechos, regla):
    # Comprueba si una regla puede activarse con los hechos actuales.
    if regla["op"] == "AND":
        return all(premisa in hechos for premisa in regla["if"])
    return any(premisa in hechos for premisa in regla["if"])

def forward_chaining(hechos_iniciales):
    # Aplica reglas desde los hechos iniciales hasta no poder inferir más.
    hechos = set(hechos_iniciales)
    inferidos = []
    reglas_usadas = []
    cambio = True

    while cambio:
        cambio = False
        for regla in REGLAS:
            conclusion = regla["then"]
            if conclusion not in hechos and regla_cumplida(hechos, regla):
                hechos.add(conclusion)
                inferidos.append(conclusion)
                reglas_usadas.append(regla["id"])
                cambio = True

    return hechos, inferidos, reglas_usadas

def backward_chaining(objetivo, hechos, visitados=None):
    # Comprueba si una hipótesis puede demostrarse a partir de los hechos y reglas.
    if visitados is None:
        visitados = set()

    if objetivo in hechos:
        return True

    if objetivo in visitados:
        return False

    visitados.add(objetivo)

    for regla in REGLAS:
        if regla["then"] == objetivo:
            if regla["op"] == "AND":
                if all(backward_chaining(premisa, hechos, visitados) for premisa in regla["if"]):
                    return True
            else:
                if any(backward_chaining(premisa, hechos, visitados) for premisa in regla["if"]):
                    return True

    return False

def mostrar_informe(caso):
    # Muestra un informe simple y claro por cada incidente.
    hechos_finales, inferidos, reglas_usadas = forward_chaining(caso["hechos"])

    objetivos = ["incidente_critico", "ataque_multietapa", "respuesta_prioritaria"]
    resultados_backward = {obj: backward_chaining(obj, caso["hechos"]) for obj in objetivos}

    print("\n" + "=" * 30)
    print(f"Incidente {caso['id_evento']} - Usuario: {caso['usuario']}")
    print("=" * 30)

    print("\nHechos detectados:")
    for hecho in sorted(caso["hechos"]):
        print(f"- {hecho}")

    print("\nRiesgos inferidos:")
    if inferidos:
        for hecho in inferidos:
            print(f"- {hecho}")
    else:
        print("- No se han inferido nuevos riesgos")

    print("\nEstado final:")
    for obj in objetivos:
        estado = "SI" if resultados_backward[obj] else "NO"
        print(f"- {obj}: {estado}")

    print("\nExplicación breve:")
    if reglas_usadas:
        for rid in reglas_usadas:
            regla = next(r for r in REGLAS if r["id"] == rid)
            op = " Y " if regla["op"] == "AND" else " O "
            print(f"{rid}: {op.join(regla['if'])} -> {regla['then']}")
    else:
        print("- No se ha activado ninguna regla")

    print("\nAcción recomendada:")
    if "respuesta_prioritaria" in hechos_finales:
        print("- Activar respuesta prioritaria")
        print("- Escalar al SOC")
        print("- Aislar el equipo afectado")
        print("- Forzar cambio de credenciales")
    elif "incidente_critico" in hechos_finales:
        print("- Escalar al SOC")
        print("- Revisar contención y erradicación")
    elif inferidos:
        print("- Monitorización reforzada")
        print("- Verificación manual por analista")
    else:
        print("- Sin acción urgente, revisar manualmente")

def main():
    """Función principal del programa."""
    casos = cargar_csv()
    for caso in casos:
        mostrar_informe(caso)

if __name__ == "__main__":
    main()