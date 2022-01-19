#Programmet genererer et tilfeldig subtraksjonsproblem med positivt resultat
#og returnerer en tilfeldig av et utvalg tilbakemeldinger ut i fra om brukeren 
#sitt svar er riktig eller feil

import random

number_1 = random.randint(0, 9)
number_2 = random.randint(0, 9)

#Det første tallet må være størst for å få positivt resultat
if number_2 > number_1:
    number_2, number_1 = number_1, number_2

answer = int(input(f"What is {number_1}-{number_2}? "))

random_number_for_response_message = random.randint(0,2)

if answer == (number_1 - number_2):
    if random_number_for_response_message == 0:
        print("Excellent!")
    elif random_number_for_response_message == 1:
        print("Way to go!")
    else:
        print("Correct!")
else:
    if random_number_for_response_message == 0:
        print("Incorrect")
    elif random_number_for_response_message == 1:
        print("Wrong")
    else:
        print("Not right")