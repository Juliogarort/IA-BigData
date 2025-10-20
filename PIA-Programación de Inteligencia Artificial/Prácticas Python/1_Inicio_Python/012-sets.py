# 1: Crear el set animales
animales = {"gato", "perro", "loro", "pez"}

# 2: Crear el set animales_domesticos
animales_domesticos = {"gato", "perro", "conejo"}

#aso 3: Encontrar la intersección entre ambos sets
interseccion = animales.intersection(animales_domesticos)

# so 4: Encontrar la diferencia entre animales y animales_domesticos
diferencia = animales.difference(animales_domesticos)

# 5: Hacer la unión de los dos sets
union = animales.union(animales_domesticos)

print("--------------------")
print("Animales:", animales)

print("--------------------")
print("Animales domesticos:", animales_domesticos)

print("--------------------")
print("Interseccion:", interseccion)

print("--------------------")
print("Diferencia (animales - animales_domesticos):", diferencia)