# Escribe un programa que dibuje un cuadrado de asteriscos de tamaño N utilizando bucles for


N = int(input("Introduce el tamaño del cuadrado: "))

for i in range(N):
    for j in range(N):
        print('*', end=' ')
    print()  
