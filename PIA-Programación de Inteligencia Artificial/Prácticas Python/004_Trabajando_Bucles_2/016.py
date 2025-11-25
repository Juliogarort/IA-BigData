#  Calcular la calificación: Dado un puntaje entre 0 y 100, imprime la calificación 
# correspondiente (A, B, C, D, F) usando condicionales.

puntaje = int(input("Ingresa tu puntaje (0-100): "))

if puntaje >= 90:
    print("Calificación: A")
elif puntaje >= 80:
    print("Calificación: B")
elif puntaje >= 70:
    print("Calificación: C")
elif puntaje >= 60:
    print("Calificación: D")
else:
    print("Calificación: F")