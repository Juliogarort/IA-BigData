# Verificar si un caractes es una coval: Escribe un programa que verifique si un caracter 
# ingresado es una vocal

letra = input("Ingresa una letra: ").lower()  

if letra in ['a', 'e', 'i', 'o', 'u']:
    print("La letra", letra, "es una vocal")
else:
    print("La letra", letra, "no es una vocal")