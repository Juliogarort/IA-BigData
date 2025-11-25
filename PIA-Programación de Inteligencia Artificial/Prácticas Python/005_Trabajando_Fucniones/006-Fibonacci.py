# FIBONACCI: Crear una función que genere la serie de Fibonacci hasta un número dado
# de término.


n = int(input("¿Cuántos términos de Fibonacci quieres ver?: "))

def fibonacci(n):
    serie = [0, 1]
    while len(serie) < n:
        serie.append(serie[-1] + serie[-2])
    return serie[:n]

print("Se estan mostrando:", n, "numeros de la serie de Fibonacci", fibonacci(n))
