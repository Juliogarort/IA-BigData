municipio(algeciras).
municipio(almeria).
municipio(cadiz).
municipio(chiclana_de_la_frontera).
municipio(cordoba).
municipio(dos_hermanas).
municipio(el_ejido).
municipio(granada).
municipio(huelva).
municipio(jaen).
municipio(jerez_de_la_frontera).
municipio(la_linea_de_la_concepcion).
municipio(linares).
municipio(malaga).
municipio(marbella).
municipio(mijas).
municipio(motril).
municipio(roquetas_de_mar).
municipio(san_fernando).
municipio(sanlucar_de_barrameda).
municipio(sevilla).
municipio(utrera).
municipio(velez_malaga).
 

% --- Área de Sevilla ---
carretera(sevilla, dos_hermanas,            13).  % A-4
carretera(sevilla, utrera,                  36).  % A-376
carretera(sevilla, huelva,                  84).  % A-49
carretera(sevilla, cordoba,                122).  % A-4
carretera(sevilla, jerez_de_la_frontera,    78).  % A-4 / AP-4
carretera(sevilla, cadiz,                   99).  % AP-4

% --- Área de Cádiz ---
carretera(cadiz, jerez_de_la_frontera,      30).  % A-4
carretera(cadiz, san_fernando,              12).  % CA-33
carretera(cadiz, chiclana_de_la_frontera,   23).  % CA-33
carretera(cadiz, sanlucar_de_barrameda,     38).  % A-480
carretera(jerez_de_la_frontera, sanlucar_de_barrameda, 28). % A-480
carretera(jerez_de_la_frontera, algeciras,  80).  % A-381
carretera(algeciras, la_linea_de_la_concepcion, 14). % A-7 / N-351

% --- Área de Málaga ---
carretera(malaga, marbella,                 60).  % A-7
carretera(malaga, mijas,                    30).  % A-7 / MA-426
carretera(malaga, velez_malaga,             35).  % A-7
carretera(malaga, motril,                   96).  % A-7
carretera(malaga, granada,                 125).  % A-92
carretera(marbella, algeciras,              75).  % A-7
carretera(marbella, mijas,                  32).  % A-7
carretera(motril, granada,                  67).  % A-44

% --- Área de Granada / Almería ---
carretera(granada, jaen,                    93).  % A-44
carretera(granada, almeria,                166).  % A-92 / A-44
carretera(almeria, roquetas_de_mar,         16).  % AL-3106
carretera(almeria, el_ejido,                32).  % A-7 / N-340
carretera(el_ejido, roquetas_de_mar,        22).  % A-7

% --- Área de Córdoba / Jaén ---
carretera(cordoba, jaen,                   107).  % A-4
carretera(cordoba, malaga,                 158).  % A-45
carretera(jaen, linares,                    48).  % A-44 / N-323
carretera(linares, cordoba,                 87).  % A-4


conectado(A, B, D) :- carretera(A, B, D).
conectado(A, B, D) :- carretera(B, A, D).


ruta(Origen, Destino, Camino, Distancia) :-
    recorrer(Origen, Destino, [Origen], Camino, Distancia).

% Caso base: ya llegamos al destino
recorrer(Destino, Destino, Visitados, Camino, 0) :-
    reverse(Visitados, Camino).

% Caso recursivo: avanzar al siguiente nodo no visitado
recorrer(Actual, Destino, Visitados, Camino, Distancia) :-
    conectado(Actual, Siguiente, D),
    \+ member(Siguiente, Visitados),
    recorrer(Siguiente, Destino, [Siguiente|Visitados], Camino, DistanciaResto),
    Distancia is D + DistanciaResto.


% ============================================================
% CONSULTAS DE PRUEBA
%
% -- Cualquier ruta entre dos ciudades:
% ?- ruta(sevilla, malaga, Camino, Dist).
% ?- ruta(huelva, jaen, Camino, Dist).
% ?- ruta(cadiz, linares, Camino, Dist).
% ?- ruta(algeciras, almeria, Camino, Dist).
% ?- ruta(granada, huelva, Camino, Dist).
% ?- ruta(sevilla, granada, Camino, Dist).
% ?- ruta(sevilla, almeria, Camino, Dist).
% 
% -- Ver todos los municipios:
% ?- municipio(X).
% ============================================================