#  Juego del "FizzBuzz": Imprime los números del 1 al 100. Para múltiplos de 3 imprime 
# "Fizz", para múltiplos de 5 imprime "Buzz", y para múltiplos de ambos imprime 
# "FizzBuzz".

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
