import pandas as pd 

ventas = []
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

# 1. Ingreso de ventas
for i in range(7):
    while True:
        entrada = input(f"Ingrese las ventas del {dias[i]}: ")
        
        if entrada == "":
            print("Error: el campo no puede estar vacío. Intente nuevamente.")
        else:
            try:
                ventas.append(float(entrada))
                break
            except ValueError:
                print("Error: debe ingresar un número válido.")
 

# 2. Serie con datos proporcionados 
serie_ventas = pd.Series(ventas, index=dias)



# 3. Análisis
print("\nTotal de ventas de la semana:")
print(serie_ventas.sum())

print("\nPromedio de ventas de la semana:")
print(round(serie_ventas.mean(), 2))

print("\nDía con mayores ventas:")
print(serie_ventas.idxmax())

# 4. Días por encima del promedio
print("\nDías de la semana con ventas por encima del promedio:")
ventas_altas = serie_ventas[serie_ventas > serie_ventas.mean()]

if ventas_altas.empty:
    print("Ningún día superó el promedio.")
else:
    for dia, venta in ventas_altas.items():
        print(f"{dia}: {venta}")
