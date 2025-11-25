# 33. Crea una lista de listas y usa un for para recorrer los elementos de cada lista interna.

liston = [
    ["Sevilla Este", "Narnia", "La Rinconada"],  
    [1, 2, 3, ],
]

for lista in liston:
    for elemento in lista:
        print("--------------------") 
        print(elemento)