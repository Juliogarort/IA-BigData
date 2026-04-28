:- dynamic nota_media/2.
:- dynamic nota_matematicas/2.
:- dynamic nota_programacion/2.
:- dynamic interes_tecnologia/2.
:- dynamic trabaja/2.
:- dynamic tiempo_disponible/2.

% -------------------------
% REGLAS
% -------------------------

recomendacion(Id, refuerzo_academico) :-
    nota_media(Id, N),
    N < 5.

recomendacion(Id, refuerzo_matematicas) :-
    nota_matematicas(Id, N),
    N < 5.

recomendacion(Id, itinerario_tecnico) :-
    interes_tecnologia(Id, si),
    nota_programacion(Id, N),
    N >= 7.

recomendacion(Id, carga_reducida) :-
    trabaja(Id, si),
    tiempo_disponible(Id, bajo).

recomendacion(Id, carga_intensiva) :-
    nota_media(Id, N),
    N >= 8,
    tiempo_disponible(Id, alto).

recomendacion(Id, itinerario_general) :-
    nota_media(Id, N),
    N >= 5,
    N < 8.