#Programmet lar brukeren velge mellom et tilfeldig addisjons, subtraksjons,
#multiplikasjons eller -divisjonsproblem og gir på nytt valget
#etter at brukeren har gitt svaret på et problem

import random   #Brukes til å generere tilfeldige tall

go_to_main_menu = True

while go_to_main_menu:
    print(2 * "\n")
    print("Main menu")
    print()
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice_user = int(input("Enter a choice:"))

    addition        = 1
    subtraction     = 2
    multiplication  = 3
    division        = 4
    leave           = 5

    #Regneoperasjonene utføres på to tilfeldige ensifrede tall
    number_1 = random.randint(0,9)
    number_2 = random.randint(0,9)

    if choice_user == addition:
        print()
        user_answer_to_addition = (
        int(input(f"What is {number_1} + {number_2}? ")) )

        if user_answer_to_addition == (number_1 + number_2):
            print("Answer is correct!")
        else: 
            print("Answer is wrong")

    elif choice_user == subtraction:
        #Det første tallet skal være større enn det andre
        if number_2 > number_1:
            number_1, number_2 = number_2, number_1

        user_answer_to_subtraction = int(
            (input(f"What is {number_1} - {number_2}? ")) )


        if user_answer_to_subtraction == (number_1 - number_2):
            print("Answer is correct!")
        else: 
            print("Answer is wrong")

    elif choice_user == multiplication:
        user_answer_to_multiplication = (
        int(input(f"What is {number_1} * {number_2}? ")) )

        if user_answer_to_multiplication == (number_1 * number_2):
            print("Answer is correct!")
        else: 
            print("Answer is wrong")

    elif choice_user == division:
        #Kan ikke dele på null
        if number_2 == 0:
            number_2 = random.randint(1, 9)
        
        user_answer_to_division = (
        float(input(f"What is {number_1} / {number_2}? ")) )

        if user_answer_to_division == (number_1 / number_2):
            print("Answer is correct!")
        else: 
            print("Answer is wrong")

    elif choice_user == leave:
        print("Exiting program")
        go_to_main_menu = False

    else:
        print("Invalid input")