#  Serie de Fibonacci: Escribe un programa que imprima los primeros N términos de la serie 
# de Fibonacci.

def fibonacci_series(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

N = int(input("Illo cuantos numeritos quieres mostrar de fibonacci?? : "))
fibonacci_terms = fibonacci_series(N)

print("Los primeros", N, "términos de la serie de Fibonacci son:")
for term in fibonacci_terms:
    print(term)
