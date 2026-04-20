import csv, os
from pyswip import Prolog

BASE = os.path.dirname(os.path.abspath(__file__))
prolog = Prolog()
prolog.consult(os.path.join(BASE, "TransporteUrbano_JulioGarcía.pl"))

def clasif_distancia(km):
    if km < 2:   return "corta"
    if km <= 10: return "media"
    return "larga"

def clasif_tiempo(min):
    if min < 15:  return "poco"
    if min <= 45: return "normal"
    return "suficiente"

VALIDOS = {
    "trafico":     ["bajo","medio","alto"],
    "clima":       ["bueno","lluvia","extremo"],
    "presupuesto": ["bajo","medio","alto"],
    "preferencia": ["rapidez","economia","ecologico"],
}

def validar(fila):
    errores = []
    try:
        if float(fila["distancia_km"]) <= 0: raise ValueError
    except: errores.append("distancia_km inválida")
    try:
        if int(fila["tiempo_disponible_min"]) <= 0: raise ValueError
    except: errores.append("tiempo inválido")
    for campo, ops in VALIDOS.items():
        if fila.get(campo,"").strip().lower() not in ops:
            errores.append(f"{campo} inválido")
    return errores

def consultar(dist, tiempo, trafico, clima, presupuesto, preferencia):
    for h in ["distancia","tiempo","trafico","clima","presupuesto","preferencia"]:
        prolog.retractall(f"{h}(_)")
    prolog.assertz(f"distancia({dist})")
    prolog.assertz(f"tiempo({tiempo})")
    prolog.assertz(f"trafico({trafico})")
    prolog.assertz(f"clima({clima})")
    prolog.assertz(f"presupuesto({presupuesto})")
    prolog.assertz(f"preferencia({preferencia})")
    return list(prolog.query("recomienda(Transporte, Prioridad)"))

def mostrar(num, fila, dist_s, tiempo_s, recs):
    print(f"\n{'─'*50}")
    print(f" CASO {num:02d} | {fila['distancia_km']}km [{dist_s}] | "
          f"{fila['tiempo_disponible_min']}min [{tiempo_s}] | "
          f"{fila['trafico']} | {fila['clima']} | {fila['presupuesto']} | {fila['preferencia']}")
    if not recs:
        print(" Sin recomendación")
        return
    r = recs[0]
    print(f" {r['Transporte']} ({r['Prioridad']})")
    for j in prolog.query(f"justificacion({r['Transporte']}, J)"):
        print(f"    {j['J']}")
    alts = list(prolog.query(f"alternativa({r['Transporte']}, A)"))
    if alts:
        print(f"    Alternativas: {', '.join(str(a['A']) for a in alts)}")

def main():
    print("\n🚌 SISTEMA EXPERTO – TRANSPORTE URBANO\n")
    with open(os.path.join(BASE, "transporte_urbano.csv"), encoding="utf-8") as f:
        filas = [{k.strip().lower(): v.strip().lower() for k,v in row.items()}
                 for row in csv.DictReader(f)]

    ok = err = 0
    for i, fila in enumerate(filas, 1):
        e = validar(fila)
        if e:
            print(f" Caso {i}: ignorado ({', '.join(e)})")
            err += 1; continue
        d = clasif_distancia(float(fila["distancia_km"]))
        t = clasif_tiempo(int(fila["tiempo_disponible_min"]))
        recs = consultar(d, t, fila["trafico"], fila["clima"],
                         fila["presupuesto"], fila["preferencia"])
        mostrar(i, fila, d, t, recs)
        ok += 1

    print(f"\nFin: {ok} procesados, {err} ignorados.\n")

if __name__ == "__main__":
    main()