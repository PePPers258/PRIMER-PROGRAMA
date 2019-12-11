number_to_guess = 2

user_number = int(input("Adivina un numero: "))

if number_to_guess == user_number:
    print("has ganado")
else:
    print("intenta otra vez")
    user_number = int(input("Adivina un numero: "))
    if number_to_guess == user_number:
        print("has ganado")
    else:
        print("intenta otra vez")
        user_number = int(input("Adivina un numero: "))
        if number_to_guess == user_number:
            print("has ganado")
        else:
            print("intenta otra vez")
            user_number = int(input("Adivina un numero: "))
            if number_to_guess == user_number:
                print("has ganado")
            else:
                print("intenta otra vez")
                user_number = int(input("Adivina un numero: "))
                if number_to_guess == user_number:
                    print("has ganado")
                else:
                    print("has perdido")