% =====================================================
%  ÁRBOL GENEALÓGICO EN PROLOG
%  5 niveles, mínimo 3 personas por nivel
% =====================================================

:- discontiguous hombre/1, mujer/1, casados/2, padre/2, madre/2, progenitor/2, abuelo/2, abuela/2, nieto/2, nieta/2, hermano/2, hermana/2, primo/2, prima/2.

% -----------------------------------------------------
% NIVEL 1 – Bisabuelos
% -----------------------------------------------------
hombre(eduardo).
mujer(concha).
hombre(ramon).

casados(eduardo, concha).

% -----------------------------------------------------
% NIVEL 2 – Abuelos
% -----------------------------------------------------
hombre(juan).
mujer(rosa).
hombre(luis).        % hermano de juan

casados(juan, rosa).

% -----------------------------------------------------
% NIVEL 3 – Padres
% -----------------------------------------------------
hombre(carlos).
mujer(ana).
mujer(marta).        

casados(carlos, ana).
casados(tomas, marta).

% -----------------------------------------------------
% NIVEL 4 – Hijos
% -----------------------------------------------------
hombre(hugo).
mujer(emma).
hombre(pedro).
mujer(laura).        % NUEVO (pareja de hugo)

casados(hugo, laura).

% -----------------------------------------------------
% NIVEL 5 – Nietos
% -----------------------------------------------------
hombre(leo).
mujer(noa).
mujer(sara).

% =====================================================
%  HECHOS DE PATERNIDAD
% =====================================================

% Nivel 1 → Nivel 2
padre(eduardo, juan).
madre(concha, juan).
padre(eduardo, luis).
madre(concha, luis).

% Nivel 2 → Nivel 3
padre(juan, carlos).
madre(rosa, carlos).
padre(juan, marta).
madre(rosa, marta).

% Nivel 3 → Nivel 4
padre(carlos, hugo).
madre(ana, hugo).
padre(carlos, emma).
madre(ana, emma).
padre(tomas, pedro).
madre(marta, pedro).

% Nivel 4 → Nivel 5 (CORREGIDO)
padre(hugo, leo).
madre(laura, leo).

padre(hugo, noa).
madre(laura, noa).

padre(hugo, sara).
madre(laura, sara).

% =====================================================
%  REGLAS
% =====================================================

% Progenitor: padre o madre
progenitor(X, Y) :- padre(X, Y).
progenitor(X, Y) :- madre(X, Y).

% Abuelo
abuelo(A, N) :-
    hombre(A),
    progenitor(A, P),
    progenitor(P, N).

% Abuela
abuela(A, N) :-
    mujer(A),
    progenitor(A, P),
    progenitor(P, N).

% Nieto
nieto(N, A) :-
    hombre(N),
    progenitor(A, P),
    progenitor(P, N).

% Nieta
nieta(N, A) :-
    mujer(N),
    progenitor(A, P),
    progenitor(P, N).

% Hermano
hermano(X, Y) :-
    hombre(X),
    progenitor(P, X),
    progenitor(P, Y),
    X \= Y.

% Hermana
hermana(X, Y) :-
    mujer(X),
    progenitor(P, X),
    progenitor(P, Y),
    X \= Y.

% Primo
primo(X, Y) :-
    hombre(X),
    progenitor(PX, X),
    progenitor(PY, Y),
    X \= Y,
    (hermano(PX, PY) ; hermana(PX, PY) ; hermano(PY, PX) ; hermana(PY, PX)).

% Prima
prima(X, Y) :-
    mujer(X),
    progenitor(PX, X),
    progenitor(PY, Y),
    X \= Y,
    (hermano(PX, PY) ; hermana(PX, PY) ; hermano(PY, PX) ; hermana(PY, PX)).


% =====================================================
%  CONSULTAS DE PRUEBA POR NIVELES
% =====================================================
% -------------------------------
% BISABUELOS
% -------------------------------
% ?- padre(eduardo, X), padre(X, Y), padre(Y, hugo).

% -------------------------------
% ABUELOS
% -------------------------------
% ?- abuelo(juan, hugo).
% ?- abuela(rosa, emma).

% -------------------------------
% PADRES
% -------------------------------
% ?- padre(carlos, hugo).
% ?- padre(hugo, leo).

% -------------------------------
% HIJOS
% -------------------------------
% ?- progenitor(carlos, hugo).
% ?- progenitor(ana, emma).

% -------------------------------
% NIETOS
% -------------------------------
% ?- nieto(hugo, juan).
% ?- nieto(leo, juan).

% -------------------------------
% RELACIONES EXTRA (RECOMENDADO)
% -------------------------------
% ?- hermana(emma, hugo).
% ?- primo(hugo, pedro).
% ?- primo(leo, pedro).
