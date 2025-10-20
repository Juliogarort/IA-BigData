# 1. Crea una tupla llamada dias_semana que contenga los días de la semana,
# empezando por "Lunes".
# 2. Verifica si el día "Sábado" está en la tupla.
# 3. Usa un loop para imprimir cada día de la semana.
# 4. Intenta modificar el valor del primer día de la tupla y observa lo que ocurre.

# 1. Crear la tupla dias_semana
dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
print("")
print("Dias de la semana:", dias_semana)
print("--------------------")

# 2. Verificar si "Sábado" está en la tupla
tiene_sabado = "Sábado" in dias_semana
print("¿La tupla contiene 'Sábado'?", tiene_sabado)
print("--------------------")

# 3. Usar un loop para imprimir cada día de la semana
print("Días de la semana impresos con un loop:")
for dia in dias_semana:
    print(dia)
print("--------------------")

# 4. Intentar modificar el valor del primer día de la tupla
