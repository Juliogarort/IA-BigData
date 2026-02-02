# Nombre: Julio García Ortiz
# Actividad: Ejercicios NumPy

import numpy as np 

print("=" * 70)
print("ACTIVIDADES DE NUMPY")
print("=" * 70)

# 1. Crear un vector con valores dentro del rango 10-49
print("\n1. Vector con valores del rango 10-49:")
vector1 = np.arange(10, 50)
print(vector1)

# 2. Invertir vector
print("\n2. Vector invertido:")
vector_invertido = vector1[::-1]
print(vector_invertido)

# 3. Crear un array de 10 ceros
print("\n3. Array de 10 ceros:")
array_ceros = np.zeros(10)
print(array_ceros)

# 4. Crear un array de 10 unos
print("\n4. Array de 10 unos:")
array_unos = np.ones(10)
print(array_unos)

# 5. Crear matriz 3x3 con valores del 0 a 8
print("\n5. Matriz 3x3 con valores del 0 a 8:")
matriz_3x3 = np.arange(9).reshape(3, 3)
print(matriz_3x3)

# 6. Crear un array de 10 cincos
print("\n6. Array de 10 cincos:")
array_cincos = np.full(10, 5)
print(array_cincos)

# 7. Transformar el array anterior a dimensión [2,5] y [5,2]
print("\n7. Array transformado a [2,5]:")
array_2x5 = array_cincos.reshape(2, 5)
print(array_2x5)
print("\n   Array transformado a [5,2]:")
array_5x2 = array_cincos.reshape(5, 2)
print(array_5x2)

# 8. Encontrar los índices que no son cero
print("\n8. Índices de valores que no son cero:")
array_mix = np.array([1, 2, 4, 2, 4, 0, 1, 0, 0, 0, 12, 4, 5, 6, 7, 0])
indices_no_cero = np.nonzero(array_mix)[0]
print(f"Array: {array_mix}")
print(f"Índices no cero: {indices_no_cero}")

# 9. Crear una matriz identidad 6x6
print("\n9. Matriz identidad 6x6:")
matriz_identidad = np.eye(6)
print(matriz_identidad)

# 10. Crear vector con 100 valores aleatorios de formato entero
print("\n10. Vector con 100 valores aleatorios enteros:")
vector_aleatorio = np.random.randint(0, 100, size=100)
print(vector_aleatorio)

# 11. Crear un array con valores al azar de forma 3x3x3 (3 dimensiones)
print("\n11. Array 3x3x3 con valores aleatorios:")
array_3d = np.random.rand(3, 3, 3)
print(array_3d)

# 12. Encontrar los valores mínimos y máximos del anterior array
print("\n12. Valores mínimo y máximo del array 3D:")
valor_min = array_3d.min()
valor_max = array_3d.max()
print(f"Valor mínimo: {valor_min}")
print(f"Valor máximo: {valor_max}")

# 13. Indicar los índices de los valores mínimos y máximos
print("\n13. Índices de valores mínimo y máximo:")
indice_min = np.unravel_index(array_3d.argmin(), array_3d.shape)
indice_max = np.unravel_index(array_3d.argmax(), array_3d.shape)
print(f"Índice del mínimo: {indice_min}")
print(f"Índice del máximo: {indice_max}")

# 14. Matriz 10x10 con bordes de 1 y interior de ceros
print("\n14. Matriz 10x10 con bordes de 1 e interior de 0:")
matriz_bordes = np.zeros((10, 10))
matriz_bordes[0, :] = 1  # Primera fila
matriz_bordes[-1, :] = 1  # Última fila
matriz_bordes[:, 0] = 1  # Primera columna
matriz_bordes[:, -1] = 1  # Última columna
print(matriz_bordes)

# 15. Crear array de tamaño 5x5 con los valores [0,1,2,3,4]
print("\n15. Array 5x5 con valores [0,1,2,3,4]:")
array_5x5 = np.tile(np.arange(5), (5, 1))
print(array_5x5)

# 16. Crear dos arrays aleatorios y verificar si son iguales
print("\n16. Verificar si dos arrays aleatorios son iguales:")
array_a = np.random.randint(0, 10, size=(3, 3))
array_b = np.random.randint(0, 10, size=(3, 3))
print(f"Array A:\n{array_a}")
print(f"\nArray B:\n{array_b}")
son_iguales = np.array_equal(array_a, array_b)
print(f"\n¿Son iguales? {son_iguales}")
elementos_coinciden = (array_a == array_b)
print(f"\nMatriz booleana de coincidencias:\n{elementos_coinciden}")

# 17. Array 5x5 con valores enteros aleatorios entre 1 y 100
print("\n17. Array 5x5 con valores aleatorios entre 1 y 100:")
array_random_5x5 = np.random.randint(1, 101, size=(5, 5))
print(array_random_5x5)

# 18. Suma total de la matriz 5x5
print("\n18. Suma total de la matriz 5x5:")
suma_total = array_random_5x5.sum()
print(f"Suma total: {suma_total}")

# 19. Suma de cada una de las columnas
print("\n19. Suma de cada columna:")
suma_columnas = array_random_5x5.sum(axis=0)
print(f"Suma por columnas: {suma_columnas}")

# 20. Extraer fila inicial, fila intermedia y última fila
print("\n20. Extraer filas específicas:")
fila_inicial = array_random_5x5[0, :]
fila_intermedia = array_random_5x5[2, :]  # Fila 3 (índice 2)
fila_final = array_random_5x5[-1, :]
print(f"Fila inicial: {fila_inicial}")
print(f"Fila intermedia (fila 3): {fila_intermedia}")
print(f"Fila final: {fila_final}")