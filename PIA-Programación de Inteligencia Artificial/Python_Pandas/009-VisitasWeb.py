import pandas as pd

num_dias = 10
visitas = []

print("Ingrese el número de visitas diarias durante 10 días")

# 1. Ingreso de visitas
for i in range(num_dias):
    while True:
        entrada = input(f"Día {i+1}: ")

        if entrada == "":
            print("Error: el campo no puede estar vacío. Intente nuevamente.")
        else:
            try:
                num_visitas = int(entrada)
                if num_visitas < 0:
                    print("Error: el número de visitas no puede ser negativo.")
                else:
                    visitas.append(num_visitas)
                    break
            except ValueError:
                print("Error: debe ingresar un número válido.")

# 2. Crear la Serie
serie_visitas = pd.Series(visitas, index=[f"Día {i+1}" for i in range(num_dias)])

# 3. Total y promedio de visitas
total = serie_visitas.sum()
promedio = serie_visitas.mean()

print(f"\nTotal de visitas: {total}")
print(f"Promedio de visitas diarias: {promedio:.2f}")

# 4. Días con más visitas que el promedio
print("\nDías con más visitas que el promedio:")
dias_alto_trafico = serie_visitas[serie_visitas > promedio]
if dias_alto_trafico.empty:
    print("Ningún día superó el promedio.")
else:
    for dia, num_visitas in dias_alto_trafico.items():
        print(f"{dia}: {num_visitas} visitas")

# 5. Clasificar visitas
serie_clasificacion = serie_visitas.apply(lambda x: "Baja visita" if x < 50 else str(x))

print("\nClasificación de visitas:")
for dia, clasificacion in serie_clasificacion.items():
    print(f"{dia}: {clasificacion}")

# 6. Gráfico de barras horizontal en consola
print("Día             │ Número de Visitas")
print("-" * 75)

# Encontrar el máximo para escalar
visitas_max = serie_visitas.max()

# Crear el gráfico
for dia, num_visitas in serie_visitas.items():
    # Calcular la longitud de la barra
    if visitas_max > 0:
        barra_longitud = int((num_visitas / visitas_max) * 40)
    else:
        barra_longitud = 0
    
    barra = "█" * barra_longitud if barra_longitud > 0 else ""
    
    print(f"{dia:<10}      │ {barra} {num_visitas:,}")

print("-" * 75)
print(f"Línea de promedio: {promedio:,.2f} visitas")
print("=" * 75)

print("")