# ============================================================
# Alumno: Julio García Ortiz
# ============================================================

resolver(Rojo, Naranja, Amarillo, Verde, Azul, Violeta) :-

    # valores posibles
    member(Rojo, [0,1]),
    member(Naranja, [0,1]),
    member(Amarillo, [0,1]),
    member(Verde, [0,1]),
    member(Azul, [0,1]),
    member(Violeta, [0,1]),

    # dato fijo
    Rojo = 0,

    # 1 = venenoso y 0 = no venenoso
    (Violeta = 1, Azul = 0 ; Violeta = 0, Azul = 1),
    (Rojo = 1, Amarillo = 0 ; Rojo = 0, Amarillo = 1),
    (Azul = 1, Naranja = 0 ; Azul = 0, Naranja = 1),

    # no pueden ser los dos venenosos
    \+ (Violeta = 1, Amarillo = 1),
    \+ (Rojo = 1, Naranja = 1),
    \+ (Verde = 1, Azul = 1).