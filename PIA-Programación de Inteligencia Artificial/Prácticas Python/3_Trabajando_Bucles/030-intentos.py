# Escribe un programa que intente adivinar un número ingresado por el usuario y use un bucle
# while. Si no logra adivinar después de 5 intentos, muestra un mensaje en el bloque else

numero_usuario = int(input("Introduce un número entre 1 y 100: "))
intentos = 0

while intentos < 5:
    intento_adivinanza = int(input("Adivina el número: "))
    intentos += 1
    if intento_adivinanza == numero_usuario:
        print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
        break
    elif intento_adivinanza < numero_usuario:
        print("El número es mayor.")
    else:
        print("El número es menor.")
else:
    print(f"No has logrado adivinar el número en 5 intentos. El número era {numero_usuario}.")

