# 36. Crea una lista de cadenas y usa split() para dividir cada cadena en palabras.

cadenas = ["Los dioze", "Oc rinconero", "Cuando me jubile saldra GTA VI"]

palabras = [cadena.split() for cadena in cadenas]
print(palabras)