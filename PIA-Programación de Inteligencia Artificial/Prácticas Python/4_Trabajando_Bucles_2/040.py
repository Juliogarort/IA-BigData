#  Convertir números decimales a binarios: Escribe un programa que convierta un número 
# decimal a binario usando un bucle.


numero_str = input("Ingresa un número decimal: ").replace(",", ".")  
numero = float(numero_str)

parte_entera = int(numero)
parte_decimal = numero - parte_entera

binario_entero = ""
if parte_entera == 0:
    binario_entero = "0"
else:
    while parte_entera > 0:
        binario_entero = str(parte_entera % 2) + binario_entero
        parte_entera //= 2

binario_decimal = ""
contador = 0
while parte_decimal > 0 and contador < 10:
    parte_decimal *= 2
    bit = int(parte_decimal)
    binario_decimal += str(bit)
    parte_decimal -= bit
    contador += 1

if binario_decimal:
    print("En binario es:", binario_entero + "." + binario_decimal)
else:
    print("En binario es:", binario_entero)
