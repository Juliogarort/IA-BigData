#  Contar vocales y consonantes: Dada una cadena de texto, cuenta cuántas vocales y 
# cuántas consonantes contiene.

texto = input("Ingresa una cadena: ").lower()
vocales = consonantes = 0

for c in texto:
    if c.isalpha():
        if c in 'aeiou':
            vocales += 1
        else:
            consonantes += 1

print("Vocales:", vocales)
print("Consonantes:", consonantes)
