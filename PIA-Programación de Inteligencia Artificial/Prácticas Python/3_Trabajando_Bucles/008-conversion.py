# Escribe un programa que convierta un rango de temperaturas de Celsius a Fahrenheit 
# utilizando un bucle for.

temperatura_celsius = (-5, 0, 32, 37)  

print("Celsius\tFahrenheit")
for celsius in temperatura_celsius:
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}\t{fahrenheit:.2f}")
