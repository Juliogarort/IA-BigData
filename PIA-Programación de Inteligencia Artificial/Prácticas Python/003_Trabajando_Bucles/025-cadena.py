# Escribe un programa que cifre una cadena desplazando cada letra una posición en el alfabeto utilizando un bucle for

def cifrar_cadena(cadena):
    cadena_cifrada = ""
    for char in cadena:
        if char.isalpha():  
            if char == 'z':
                cadena_cifrada += 'a'
            elif char == 'Z':
                cadena_cifrada += 'A'
            else:
                cadena_cifrada += chr(ord(char) + 1)
        else:
            cadena_cifrada += char  
    return cadena_cifrada

texto = "Losh diozeee, eto esta como rarooo"
texto_cifrado = cifrar_cadena(texto)
print("Texto original:", texto)
print("Texto cifrado:", texto_cifrado)
