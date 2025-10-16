# 1. Crea una lista
colores = [ "rojo", "verde", "azul", "amarillo" ]

print("Lista inicial:", colores)
print("--------------------")

# Aladir morado al final de la lista
colores.append("morado")
print("Lista con 'morado' al final:", colores)
print("--------------------")

# Añadir naranja en la segunda posicion (indice 1)
colores.insert(1, "naranja")
print("Lista con 'naranja' en la segunda posicion:", colores)
print("--------------------")

# Eliminar verde de la lista
colores.remove("verde")
print("Lista con 'verde' eliminado:", colores)
print("--------------------")

#  Lista ordenada 
colores.sort()
print("Lista ordenada alfabeticamente:", colores)
print("--------------------")

# Lista invertida
colores.reverse()
print("Lista con orden invertido:", colores)
print("--------------------")

# Lista final
print("Lista final:", colores)
print("--------------------")