# 44. Crea una lista de palabras y usa map() para convertirlas a mayúsculas.

palabras = ["Oc", "es", "de", "la", "rinconada"]

print("--------------------") 
print(palabras)

mayus = list(map(str.upper, palabras))

print("--------------------") 
print(mayus)
print("--------------------") 