import math

# longitud eslabon
L1 = 2
L2 = 2

# punto final a alcanzar
x = 2
y = 3

#  distancia al punto
distancia = math.sqrt(x**2 + y**2)


if distancia <= L1 + L2 and distancia >= abs(L1 - L2):
    print(f"El punto ({x}, {y}) esta DENTRO del espacio de trabajo")
else:
    print(f"El punto ({x}, {y}) esta FUERA del espacio de trabajo")
