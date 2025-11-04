#  Verificar si una lista está ordenada: Usa un bucle para verificar si una lista está ordenada 
# de manera ascendente

numeros = [int(x) for x in input("Ingresa números separados por espacio: ").split()]
ordenada = True

for i in range(len(numeros) - 1):
    if numeros[i] > numeros[i + 1]:
        ordenada = False
        break

if ordenada:
    print("La lista está ordenada de forma ascendente.")
else:
    print("La lista NO está ordenada.")
