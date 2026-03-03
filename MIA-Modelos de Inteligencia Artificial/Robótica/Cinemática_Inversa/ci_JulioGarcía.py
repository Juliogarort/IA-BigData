# Implementar un Script en Python que calcule los ángulos de articulación de un 
# # brazo robótico para alcanzar una posición específica.


# Para comprobar su funcionalidad, generar 10 posiciones aleatorias e indicar en formato tabla (matriz) 
# los ángulos de cada articulación del # brazo robótico.

import numpy as np
import matplotlib.pyplot as plt

# ==============================
# LONGITUDES DEL BRAZO
# ==============================

L1 = 2
L2 = 1.5

# ==============================
# CINEMÁTICA INVERSA
# ==============================

def cinematica_inversa(x, y):
    """
    Calcula theta1 y theta2 para alcanzar (x,y)
    """
    cos_theta2 = (x**2 + y**2 - L1**2 - L2**2) / (2 * L1 * L2)

    if abs(cos_theta2) > 1:
        return None, None

    theta2 = np.arccos(cos_theta2)

    theta1 = np.arctan2(y, x) - np.arctan2(
        L2 * np.sin(theta2),
        L1 + L2 * np.cos(theta2)
    )

    return theta1, theta2

# ==============================
# FUNCIÓN PARA DIBUJAR EL BRAZO
# ==============================

def dibujar_brazo(theta1, theta2, x_obj, y_obj, numero):

    # Posición del primer eslabón
    x1 = L1 * np.cos(theta1)
    y1 = L1 * np.sin(theta1)

    # Posición final calculada
    x2 = x1 + L2 * np.cos(theta1 + theta2)
    y2 = y1 + L2 * np.sin(theta1 + theta2)

    plt.figure()

    # Dibujar eslabones
    plt.plot([0, x1], [0, y1])
    plt.plot([x1, x2], [y1, y2])

    # Dibujar puntos
    plt.scatter([0, x1, x2], [0, y1, y2])

    # Punto objetivo en rojo
    plt.scatter(x_obj, y_obj, marker='x')

    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    plt.gca().set_aspect('equal')
    plt.title(f"Posición {numero}")
    plt.grid()
    plt.show()

# ==============================
# GENERAR 10 POSICIONES
# ==============================

print("\nTabla de resultados:\n")
print("X\tY\tTheta1(rad)\tTheta2(rad)")

for i in range(10):

    # Generamos posición alcanzable
    r = np.random.uniform(0.5, L1 + L2 - 0.1)
    ang = np.random.uniform(0, 2*np.pi)

    x = r * np.cos(ang)
    y = r * np.sin(ang)

    theta1, theta2 = cinematica_inversa(x, y)

    if theta1 is not None:
        print(f"{x:.3f}\t{y:.3f}\t{theta1:.3f}\t\t{theta2:.3f}")
        dibujar_brazo(theta1, theta2, x, y, i+1)