# 42. Crea una lista de temperaturas y convierte todas las temperaturas de Celsius a Fahrenheit.

temperatura = [-15, 16, 100, 38, 0]
print("--------------------") 
print(f"Temperaturas en Celsius:", temperatura)
print("--------------------") 

# farenheit = (temperatura * 9/5) + 32
farenheit = [(temp * 9/5) + 32 for temp in temperatura]
print(f"Temperaturas en Farenheit:", farenheit)
print("--------------------") 