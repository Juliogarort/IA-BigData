# Escribe un programa que genere los primeros N números de la serie de Fibonacci utilizando
# un bucle for.

mostrar = 12

a, b = 0, 1
fibonacci = []
for _ in range(mostrar):
    fibonacci.append(a)
    a, b = b, a + b
print(fibonacci)
