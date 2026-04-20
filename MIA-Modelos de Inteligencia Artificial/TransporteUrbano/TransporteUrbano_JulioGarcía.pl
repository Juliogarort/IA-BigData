% ============================================================
%  TransporteUrbano_JulioGarcía.pl
%  Base de conocimiento - Sistema Experto Transporte Urbano
%  MIA · ILERNA Sevilla · Julio García
% ============================================================

:- dynamic distancia/1, tiempo/1, trafico/1, clima/1, presupuesto/1, preferencia/1.

% ── BICICLETA ───────────────────────────────────────────────
% Distancia corta + buen clima + cualquier preferencia razonable
recomienda(bicicleta, ecologico) :-
    distancia(corta),
    clima(bueno),
    (preferencia(ecologico) ; preferencia(economia) ;
     preferencia(rapidez)   ; tiempo(suficiente)).

% ── METRO ───────────────────────────────────────────────────
% Tráfico alto o distancia larga → rápido
recomienda(metro, rapido) :-
    (trafico(alto) ; distancia(larga)),
    \+ clima(extremo).

% Distancia larga + presupuesto bajo → económico
recomienda(metro, economico) :-
    distancia(larga),
    presupuesto(bajo).

% Lluvia + distancia larga → metro protegido
recomienda(metro, ecologico) :-
    clima(lluvia),
    distancia(larga).

% ── AUTOBÚS ─────────────────────────────────────────────────
% Distancia media con variedad de condiciones
recomienda(autobus, economico) :-
    distancia(media),
    (presupuesto(bajo) ; preferencia(economia) ; clima(lluvia) ;
     trafico(bajo)     ; trafico(medio)).

% Lluvia + distancia corta (evitar bicicleta)
recomienda(autobus, economico) :-
    clima(lluvia),
    distancia(corta).

% Clima extremo sin presupuesto alto (taxi no accesible)
recomienda(autobus, economico) :-
    clima(extremo),
    \+ presupuesto(alto).

% ── COCHE COMPARTIDO ────────────────────────────────────────
% Distancia larga + tráfico bajo + rapidez
recomienda(coche_compartido, rapido) :-
    distancia(larga),
    trafico(bajo),
    preferencia(rapidez).

% Distancia larga + presupuesto medio o alto
recomienda(coche_compartido, economico) :-
    distancia(larga),
    (presupuesto(medio) ; presupuesto(alto)).

% ── TAXI ────────────────────────────────────────────────────
% Tiempo escaso con presupuesto o tráfico favorable
recomienda(taxi, rapido) :-
    tiempo(poco),
    (presupuesto(alto) ; trafico(bajo)).

% Clima extremo con presupuesto alto
recomienda(taxi, rapido) :-
    clima(extremo),
    presupuesto(alto).

% ── ALTERNATIVAS ────────────────────────────────────────────
alternativa(bicicleta,       patinete_electrico) :- clima(bueno), distancia(corta).
alternativa(metro,           autobus)            :- distancia(media).
alternativa(metro,           coche_compartido)   :- distancia(larga), \+ presupuesto(bajo).
alternativa(autobus,         metro)              :- distancia(larga).
alternativa(autobus,         bicicleta)          :- distancia(corta), clima(bueno).
alternativa(coche_compartido, taxi)              :- presupuesto(alto).
alternativa(coche_compartido, metro)             :- distancia(larga).
alternativa(taxi,            coche_compartido)   :- presupuesto(medio).

% ── JUSTIFICACIONES ─────────────────────────────────────────
justificacion(bicicleta,       'Distancia corta con buen clima. Ideal para preferencias ecologicas o economicas.').
justificacion(metro,           'Trafico alto o distancia larga. El metro es rapido y evita el trafico en ciudad.').
justificacion(autobus,         'Opcion economica para distancias medias. Adecuado con trafico moderado o lluvia.').
justificacion(coche_compartido,'Distancia larga con buen presupuesto. Equilibrio entre comodidad y coste compartido.').
justificacion(taxi,            'Tiempo muy limitado o clima extremo. Garantiza rapidez y comodidad de puerta a puerta.').