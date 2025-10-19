# Ejercicio Sets (Conjuntos)
# 1. Crea un set llamado frutas con los valores: "manzana", "banana", "naranja", "uva".
# 2. Agrega una nueva fruta "pera" al set.
# 3. Intenta agregar la fruta "banana" nuevamente al set (nota lo que sucede).
# 4. Elimina la fruta "naranja" del set.
# 5. Imprime todos los elementos del set.

# 1. Crear el set frutas
frutas = {"manzana", "banana", "naranja", "uva"}

print("--------------------")
print("Set inicial 1:", frutas)
print("--------------------")

# 2. Agregar una nueva fruta "pera"
frutas.add("pera")
print("Set '2':", frutas)
print("--------------------")

# 3. Intentar agregar "banana" nuevamente
frutas.add("banana")  # No funciona, no se admiten duplicados 
print("Set '3':", frutas)
print("--------------------")

# 4. Eliminar la fruta "naranja"
frutas.remove("naranja")
print("Set final:", frutas)
print("--------------------")
