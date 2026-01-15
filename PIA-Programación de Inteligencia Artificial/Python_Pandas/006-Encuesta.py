# Ejercicio 6: Evaluación de Encuesta de Satisfacción
# Solicita al usuario que ingrese las calificaciones de satisfacción (de 1 a 5) de 12 clientes.
# Crea una Serie con las calificaciones.
# Calcula la frecuencia de cada calificación y el porcentaje de clientes satisfechos (calificación ≥ 4).
# Reemplaza cualquier calificación de 1 con "Insatisfecho".
# Muestra un resumen de las calificaciones en forma de gráfico de barras.

import pandas as pd

num_clientes = 12
calificaciones = []

print("Ingrese las calificaciones de satisfacción (1-5) de los clientes")

# 1. Ingreso de calificaciones
for i in range(num_clientes):
    while True:
        entrada = input(f"Cliente {i+1}: ")
        try:
            calificacion = int(entrada)
            if 1 <= calificacion <= 5:
                calificaciones.append(calificacion)
                break
            else:
                print("Error: la calificación debe estar entre 1 y 5.")
        except ValueError:
            print("Error: ingrese un número válido.")

# 2. Crear la Serie
serie_calificaciones = pd.Series(calificaciones)

# 3. Frecuencia de cada calificación
print("\nFrecuencia de calificaciones:")
print("-" * 30)
frecuencias = serie_calificaciones.value_counts().sort_index()
for calificacion, cantidad in frecuencias.items():
    print(f"Calificación {calificacion}: {cantidad} clientes")

# 4. Porcentaje de clientes satisfechos (≥ 4)
clientes_satisfechos = (serie_calificaciones >= 4).sum()
porcentaje_satisfechos = (clientes_satisfechos / len(serie_calificaciones)) * 100
print(f"\nClientes satisfechos (calificación ≥ 4): {porcentaje_satisfechos:.1f}%")

# 5. Reemplazar calificaciones de 1 con "Insatisfecho"
serie_resultados = serie_calificaciones.apply(
    lambda x: "Insatisfecho" if x == 1 else str(x)
)

print("\nResultados de la encuesta:")
for i, resultado in enumerate(serie_resultados):
    print(f"Cliente {i+1}: {resultado}")

# 6. Gráfico de barras en consola
print("\n" + "=" * 60)
print("GRÁFICO DE BARRAS - DISTRIBUCIÓN DE CALIFICACIONES")
print("=" * 60)
print("Calificación (1-5)          │ Número de Clientes")
print("-" * 60)

# Encontrar el máximo para escalar las barras
max_frecuencia = frecuencias.max()

# Crear el gráfico
for calificacion in range(1, 6):
    cantidad = frecuencias.get(calificacion, 0)
    # Calcular la longitud de la barra (proporcional al espacio disponible)
    barra_longitud = int((cantidad / max_frecuencia) * 30) if max_frecuencia > 0 else 0
    barra = "█" * barra_longitud
    
    # Formato mejorado con espacios alineados
    print(f"{calificacion} ⭐   │ {barra} ({cantidad})")

print("=" * 60)
print(f"Total de clientes encuestados: {num_clientes}")
print("=" * 60)

print("")