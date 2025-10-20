# 1. Crea una lista llamada números con los valores [12, 45, 78, 23, 56, 89, 23, 56].
# 2. Cuenta cuántas veces aparece el número 23 en la lista.
# 3. Encuentra el índice de la primera aparición del número 56.
# 4. Elimina el último número de la lista.
# 5. Usa el método extend() para agregar los valores [100, 200, 300] al final de la lista.
# 6. Haz una copia de la lista en una nueva variable llamada numeros_copia.
# 7. Limpia (vacía) la lista original.

# 1. Crear la lista números
numeros = [12, 45, 78, 23, 56, 89, 23, 56]
print("Lista inicial:", numeros)
print("--------------------")

# 2. Contar cuántas veces aparece el número 23
contador_23 = numeros.count(23)
print("El número 23 aparece", contador_23, "veces en la lista.")
print("--------------------")

# 3. Encontrar el índice de la primera aparición del número 56
indice_56 = numeros.index(56)   
print("El número 56 aparece por primera vez en el índice:", indice_56)
print("--------------------")

# 4. Eliminar el último número de la lista
numeros.pop()
print("Lista después de eliminar el último número:", numeros)
print("--------------------")

# 5. Usar el método extend() para agregar [100, 200, 300] al final de la lista
numeros.extend([100, 200, 300])
print("Lista después de extender con [100, 200, 300]:", numeros)
print("--------------------")

# 6. Hacer una copia de la lista en una nueva variable llamada numeros_copia
numeros_copia = numeros.copy()
print("Copia de la lista:", numeros_copia)
print("--------------------")

# 7. Limpiar (vaciar) la lista original
numeros.clear()
print("Lista original después de limpiarla:", numeros)
print("--------------------")
