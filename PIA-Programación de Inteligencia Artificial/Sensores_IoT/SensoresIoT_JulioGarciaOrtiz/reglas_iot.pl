:- dynamic temperatura_interior/2.
:- dynamic temperatura_exterior/2.
:- dynamic humedad/2.
:- dynamic co2/2.
:- dynamic luces_encendidas/2.
:- dynamic estado_ventanas/2.
:- dynamic estado_persianas/2.
:- dynamic presencia/2.



recomendacion(Id, encender_aire_acondicionado) :-
    temperatura_interior(Id, Ti),
    temperatura_exterior(Id, Te),
    Ti > 26,
    Te > 22.

recomendacion(Id, abrir_ventanas_refrescar) :-
    temperatura_interior(Id, Ti),
    temperatura_exterior(Id, Te),
    Ti > 25,
    Te < Ti.

recomendacion(Id, encender_calefaccion) :-
    temperatura_interior(Id, Ti),
    temperatura_exterior(Id, Te),
    Ti < 19,
    Te < 18.

recomendacion(Id, activar_ventilacion) :-
    co2(Id, C),
    C > 800.

recomendacion(Id, activar_humidificador) :-
    humedad(Id, H),
    H < 35.

recomendacion(Id, activar_deshumidificador) :-
    humedad(Id, H),
    H > 65.


recomendacion(Id, apagar_luces_ahorro) :-
    presencia(Id, no),
    luces_encendidas(Id, L),
    L > 0.


recomendacion(Id, cerrar_ventanas_seguridad) :-
    presencia(Id, no),
    estado_ventanas(Id, abierta).

recomendacion(Id, cerrar_ventanas_seguridad) :-
    presencia(Id, no),
    estado_ventanas(Id, mitad).



recomendacion(Id, cerrar_persianas_aislamiento) :-
    temperatura_exterior(Id, Te),
    Te < 10,
    estado_persianas(Id, abierta).