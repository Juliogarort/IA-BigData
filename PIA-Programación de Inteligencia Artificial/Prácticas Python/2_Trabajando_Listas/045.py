# 45. Simula una cola utilizando listas, añadiendo elementos con append() y removiéndolos con pop(0).

cola = []

print("--------------------") 
print("Cola inicial:", cola)
print("--------------------") 
# Añadir elementos a la cola
cola.append('Elemento 1')
cola.append('Elemento 2')
cola.append('Elemento 3')
print("Cola despues de añadir elementos:", cola)
print("--------------------") 

# Remover elementos de la cola
elemento_removido = cola.pop(2)
print("Cola despues de remover un elemento:", cola)
print("--------------------") 