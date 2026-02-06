import numpy as np


def separador():
    print("\n" + "=" * 40 + "\n")


separador()
print("EJERCICIO 1: Producto Escalar")
print("Calcula el producto escalar utilizando NumPy.")
# 1. Producto Escalar
# Dado los vectores:
# a = [2, 3, 4]
# b = [5, 6, 7]
# Calcula el producto escalar utilizando NumPy.
a = np.array([2, 3, 4])
b = np.array([5, 6, 7])
print(a @ b)
print(a.dot(b))


separador()
print("EJERCICIO 2: Módulo de un Vector")
print("Calcula su módulo (norma) utilizando NumPy.")
# 2. Módulo de un Vector
# Dado el vector:
# v = [3, 4]
# Calcula su módulo (norma) utilizando NumPy.
v = np.array([3, 4])
print(np.linalg.norm(v))


separador()
print("EJERCICIO 3: Producto de Dos Matrices")
print("Calcula su producto utilizando NumPy.")
# 3. Producto de Dos Matrices
# Dadas las matrices:
# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]
# Calcula su producto utilizando NumPy.
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A @ B)


separador()
print("EJERCICIO 4: Matriz Traspuesta")
print("Obtén su traspuesta utilizando NumPy")
# 4. Matriz Traspuesta
# Dada la matriz:
# a = [[1, 2, 3], [4, 5, 6]]
# Obtén su traspuesta utilizando NumPy
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.T)


separador()
print("EJERCICIO 5: Traza de una Matriz")
print("Calcula su traza utilizando NumPy.")
# 5. Traza de una Matriz
# Dada la matriz cuadrada:
# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Calcula su traza utilizando NumPy.
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.trace(a))


separador()
print("EJERCICIO 6: Determinante de una Matriz")
print("Calcula su determinante utilizando NumPy.")
# 6. Determinante de una Matriz
# Dada la matriz cuadrada:
# A = [[1, 2], [3, 4]]
# Calcula su determinante utilizando NumPy.
A = np.array([[1, 2], [3, 4]])
print(np.linalg.det(A))


separador()
print("EJERCICIO 7: Matriz Inversa")
print("Calcula su inversa utilizando NumPy.")
# 7. Matriz Inversa
# Dada la matriz cuadrada:
# A = [[4, 7], [2, 6]]
# Calcula su inversa utilizando NumPy.
A = np.array([[4, 7], [2, 6]])
print(np.linalg.inv(A))


separador()
print("EJERCICIO 8: Autovalores y Autovectores")
print("Calcula sus autovalores y autovectores utilizando NumPy.")
# 8. Autovalores y Autovectores
# Dada la matriz cuadrada:
# A = [[2, 1], [1, 3]]
# Calcula sus autovalores y autovectores utilizando NumPy.
A = np.array([[2, 1], [1, 3]])
autovalores, autovectores = np.linalg.eig(A)
print(autovalores)
print(autovectores)


separador()
print("EJERCICIO 9: Solución de un Sistema de Ecuaciones")
print("Resuelve el siguiente sistema de ecuaciones lineales utilizando NumPy:")
# 9. Solución de un Sistema de Ecuaciones
# Resuelve el siguiente sistema de ecuaciones lineales utilizando NumPy:
# 2x + y = 8
# x + 3y = 18
A = np.array([[2, 1], [1, 3]])
b = np.array([8, 18])
print(np.linalg.solve(A, b))

separador()
