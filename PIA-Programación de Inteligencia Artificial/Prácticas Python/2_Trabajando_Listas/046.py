# 46. Crea una lista de nombres y usa filter() para obtener solo los nombres que comienzan con una vocal.

nombres = ["Oc", "José", "Joseca", "Antonio", "Paco", "Pepe", "Elena", "Ana"]

print("--------------------") 
print("Nombres originales:", nombres)
print("--------------------") 

vocales = ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u")
nombres_con_vocal = list(filter(lambda nombre: nombre.startswith(vocales), nombres))
print("Nombres que comienzan con vocal:", nombres_con_vocal)