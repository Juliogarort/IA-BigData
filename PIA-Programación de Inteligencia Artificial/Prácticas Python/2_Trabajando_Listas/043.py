# 43. Encuentra los números pares en una lista de 10 números enteros.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [num for num in numeros if num % 2 == 0]

print("--------------------") 
print("Numeros pares en la lista:", pares)
print("--------------------") 