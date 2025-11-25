# Escribe un programa que imprima una pirámide de números utilizando bucles for

niveles = 5
for i in range(1, niveles + 1):
    
    for j in range(niveles - i):
        print(" ", end="")
    
    for k in range(1, i + 1):
        print(k, end=" ")
    print()  