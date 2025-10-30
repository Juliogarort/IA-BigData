# Imprimir tabla de multiplicar: Solicita un número al usuario y genera su tabla de
# multiplicar del 1 al 10.

while True:
    try:
        num = int(input("Ingrese un número del 1 al 10: "))
        
        if num < 1 or num > 10:
            print("Cabezaa ese numero no furula, introduce uno nuevamente.")
        else:
            print(f"\nTabla de multiplicar del {num}:")
            for i in range(1, 11):
                print(f"{num} x {i} = {num * i}")
            break
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")