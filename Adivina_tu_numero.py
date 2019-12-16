number_to_guess = 0
number_to_guess = int(input("Para continuar, introduce un numero para que alguien mas lo adivine, fijate que no lo vea (numeros entre el 1 y 100): "))

user_number = int(input("Adivina un numero: "))

while number_to_guess < 0 or number_to_guess > 0:
    print("Has fallado, intentalo de nuevo")
    user_number = int(input("Adivina un numero: "))

print("¡felicidades, adivinaste el nuemro, el numero era {}" .format(number_to_guess))