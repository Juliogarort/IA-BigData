# Serie de Fibonacci: Escribe un programa que imprima los primeros N términos de la serie
# de Fibonacci.

N = int(input("Introduce el número de términos de la serie de Fibonacci que deseas ver: "))
a, b = 0, 1
fibonacci = []
for _ in range(N):
    fibonacci.append(a)
    a, b = b, a + b
print(fibonacci)

