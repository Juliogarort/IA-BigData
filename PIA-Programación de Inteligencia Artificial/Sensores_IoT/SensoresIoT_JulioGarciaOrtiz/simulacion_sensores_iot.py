import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import subprocess
import os

# Archivo de salida de resultados en formato TXT (similar al recomendador)
ARCHIVO_SALIDA = "informe_iot.txt"
ARCHIVO_CSV = "datos_sensores_iot.csv"

def explicar(rec):
    # Proporciona una explicación en lenguaje natural para la regla disparada.
    explicaciones = {
    "encender_aire_acondicionado": "temperatura interior superior a 26°C y exterior superior a 22°C",
    "encender_calefaccion": "temperatura interior inferior a 19°C y exterior inferior a 18°C",
    "activar_ventilacion": "niveles de CO2 superiores a 800 ppm",
    "activar_humidificador": "humedad relativa inferior al 35%",
    "activar_deshumidificador": "humedad relativa superior al 65%",
    "apagar_luces_ahorro": "casa vacía y luces encendidas",
    "cerrar_ventanas_seguridad": "casa vacía y ventanas abiertas o a medio cerrar",
    "abrir_persianas": "hay presencia y las persianas están cerradas",
    "abrir_ventanas_refrescar": "temperatura interior alta y exterior más fresca que la interior",
    "cerrar_persianas_aislamiento": "temperatura exterior inferior a 10°C y persianas abiertas"
}
    return explicaciones.get(rec, "sin explicación")

def generar_consulta_prolog(id_registro, fila):
    # Genera la consulta SWI-Prolog para evaluar las reglas con assertz.
    
    # Conversión de tipos y limpieza para Prolog
    temp_int = float(fila['temp_interior_c'])
    temp_ext = float(fila['temp_exterior_c'])
    humedad = float(fila['humedad_pct'])
    co2 = int(fila['co2_ppm'])
    luces = int(fila['luces_encendidas'])
    ventanas = str(fila['estado_ventanas']).strip().lower()
    persianas = str(fila['estado_persianas']).strip().lower()
    presencia = "si" if fila['presencia'] else "no"

    consulta = f"""
    consult('reglas_iot.pl'),
    assertz(temperatura_interior({id_registro}, {temp_int})),
    assertz(temperatura_exterior({id_registro}, {temp_ext})),
    assertz(humedad({id_registro}, {humedad})),
    assertz(co2({id_registro}, {co2})),
    assertz(luces_encendidas({id_registro}, {luces})),
    assertz(estado_ventanas({id_registro}, {ventanas})),
    assertz(estado_persianas({id_registro}, {persianas})),
    assertz(presencia({id_registro}, {presencia})),
    findall(R, recomendacion({id_registro}, R), Lista),
    write(Lista),
    halt.
    """
    return consulta

def generar_datos_simulados(num_registros=24):
    # Genera un DataFrame simple con datos aleatorios de sensores.
    np.random.seed(42)
    start = datetime(2026, 4, 29, 0, 0, 0)
    
    registros = []
    for h in range(num_registros):
        timestamp = start + timedelta(hours=h)
        # Datos simplificados
        temp_ext = round(np.random.uniform(5.0, 25.0), 1)
        temp_int = round(np.random.uniform(17.0, 28.0), 1)
        humedad = round(np.random.uniform(30.0, 75.0), 1)
        luces = np.random.randint(0, 5)
        
        estados_ventanas = ["abierta", "cerrada", "mitad"]
        estados_persianas = ["abierta", "cerrada", "mitad"]
        ventanas = np.random.choice(estados_ventanas)
        persianas = np.random.choice(estados_persianas)
        
        presencia = np.random.choice([True, False], p=[0.7, 0.3])
        co2 = np.random.randint(400, 1000)

        registros.append([
            h, timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            temp_ext, temp_int, humedad, luces,
            ventanas, persianas, presencia, co2
        ])

    df = pd.DataFrame(registros, columns=[
        'id_registro', 'timestamp', 'temp_exterior_c', 'temp_interior_c', 
        'humedad_pct', 'luces_encendidas', 'estado_ventanas', 
        'estado_persianas', 'presencia', 'co2_ppm'
    ])
    
    return df

def ejecutar():
    carpeta = os.path.dirname(os.path.abspath(__file__))
    os.chdir(carpeta)

    # 1. Generar los datos en formato Pandas y guardar en CSV
    print("Generando datos simulados...")
    df = generar_datos_simulados(24)
    df.to_csv(ARCHIVO_CSV, index=False)
    print(f"Datos guardados en {ARCHIVO_CSV}")

    # 2. Iterar sobre el DataFrame, consultar a Prolog y guardar en TXT
    print("Evaluando reglas con SWI-Prolog...")
    with open(ARCHIVO_SALIDA, "w", encoding="utf-8") as salida_txt:
        for _, fila in df.iterrows():
            id_registro = int(fila["id_registro"])
            consulta = generar_consulta_prolog(id_registro, fila)

            # Ejecutar SWI-Prolog como subproceso
            proceso = subprocess.run(
                ["swipl", "-g", consulta],
                capture_output=True,
                text=True
            )

            salida = proceso.stdout.strip()
            
            # Formatear la salida de texto
            texto = "\n====================================\n"
            texto += f"Registro: {id_registro} (Hora: {fila['timestamp']})\n"
            texto += "Datos:\n"
            texto += f" - Temp. Interior: {fila['temp_interior_c']}°C\n"
            texto += f" - Temp. Exterior: {fila['temp_exterior_c']}°C\n"
            texto += f" - Humedad: {fila['humedad_pct']}%\n"
            texto += f" - CO2: {fila['co2_ppm']} ppm\n"
            texto += f" - Luces encendidas: {fila['luces_encendidas']}\n"
            texto += f" - Ventanas: {fila['estado_ventanas']}\n"
            texto += f" - Persianas: {fila['estado_persianas']}\n"
            texto += f" - Presencia: {'Sí' if fila['presencia'] else 'No'}\n"
            texto += "\nDecisiones/Recomendaciones:\n"

            if salida == "[]" or not salida:
                texto += " - Sin acciones requeridas\n"
            else:
                # Procesar lista de salida de prolog "[acc1, acc2]" -> ["acc1", "acc2"]
                recomendaciones = [r.strip() for r in salida.replace("[", "").replace("]", "").split(",") if r.strip()]
                for r in recomendaciones:
                    texto += f" - {r}\n"
                
                texto += "\nExplicación:\n"
                for r in recomendaciones:
                    texto += f" - {r}: {explicar(r)}\n"

            # Imprimir por consola y escribir a archivo
            print(texto)
            salida_txt.write(texto)

    print("\n✅ Proceso completado. Archivo generado:", ARCHIVO_SALIDA)

if __name__ == "__main__":
    ejecutar()
