Posi_inicial = 0       # Posi inicial
Posi_final = 90    # Posi final
incremento = 10         # movimiento de 10 en 10 grados a cada paso

print("")
print(f"Ángulo inicial:  {Posi_inicial}°")
print(f"Ángulo objetivo: {Posi_final}°")
print(f"Incremento:      {incremento}°")
print("" )

paso = 0
print(f"Paso {paso}: Ángulo = {Posi_inicial}°")

while Posi_inicial != Posi_final:
    if Posi_inicial < Posi_final:
        Posi_inicial += incremento
    else:
        Posi_inicial -= incremento
    paso += 1
    print(f"Paso {paso}: Ángulo = {Posi_inicial}°")

print("")