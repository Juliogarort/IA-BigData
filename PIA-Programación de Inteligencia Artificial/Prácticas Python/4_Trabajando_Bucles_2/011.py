# Par o impar: Escribe un programa que determine si un número es par o impar.

while True:
    numero_str = input("Ingresa un número entero: ")
    
    if numero_str.lstrip('-').isdigit(): 
        numero = int(numero_str)
        break
    else:
        print("Error: Debes ingresar un número entero válido (sin decimales ni letras).")

if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
