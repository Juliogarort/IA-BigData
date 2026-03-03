import numpy as np
import matplotlib.pyplot as plt

# Longitudes de los eslabones
L1 = 2
L2 = 1.5

def transformacion(theta, L):
    return np.array([
        [np.cos(theta), -np.sin(theta), L*np.cos(theta)],
        [np.sin(theta),  np.cos(theta), L*np.sin(theta)],
        [0,              0,             1]
    ])

def cinematica_directa(theta1, theta2):
    T1 = transformacion(theta1, L1)
    T2 = transformacion(theta2, L2)
    
    T = np.dot(T1, T2)
    
    x = T[0, 2]
    y = T[1, 2]
    
    return x, y, T

def dibujar_brazo(theta1, theta2, numero):
    # Posición del primer eslabón
    x1 = L1 * np.cos(theta1)
    y1 = L1 * np.sin(theta1)
    
    # Posición final
    x2 = x1 + L2 * np.cos(theta1 + theta2)
    y2 = y1 + L2 * np.sin(theta1 + theta2)
    
    plt.figure()
    plt.plot([0, x1], [0, y1])
    plt.plot([x1, x2], [y1, y2])
    plt.scatter([0, x1, x2], [0, y1, y2])
    
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    plt.gca().set_aspect('equal')
    plt.title(f"Configuración {numero}")
    plt.grid()
    plt.show()


# 4 configuraciones distintas
configuraciones = [
    (0, 0),
    (np.pi/4, np.pi/4),
    (np.pi/2, -np.pi/4),
    (np.pi/3, np.pi/6)
]

for i, (t1, t2) in enumerate(configuraciones):
    x, y, T = cinematica_directa(t1, t2)
    
    print(f"\nResultado {i+1}")
    print(f"Theta1: {t1:.2f} rad, Theta2: {t2:.2f} rad")
    print(f"Posición final: x = {x:.3f}, y = {y:.3f}")
    print("Matriz T final:")
    print(T)
    
    dibujar_brazo(t1, t2, i+1)