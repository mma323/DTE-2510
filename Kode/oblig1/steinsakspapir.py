#Stein, saks, papir der brukeren skriver inn et tall som representerer valget
#Det genereres et tilfeldig tall som representerer datamaskinen sitt valg
#Brukeren spiller mot datamaskinen

import random as rdm #Brukt til å generere tilfeldig tall

print("Rock, paper, scissor: Type 0 for scissor, 1 for rock or 2 for paper")
scissor = 0
rock    = 1
paper   = 2

user_choice = int(input("Pick number: ")) 

computer_choice = (
    rdm.randint(scissor, paper))

if user_choice == scissor:
    if computer_choice == scissor:
        print("You picked scissor and the computer picked scissor," 
        " it is a draw")
    elif computer_choice == rock:
        print("You picked scissor and the computer picked rock, computer wins")
    else:
        print("You picked scissor and the computer picked paper, you win")
elif user_choice == rock:
    if computer_choice == scissor:
        print("You picked rock and the computer picked scissor, you win")
    elif computer_choice == rock:
        print("You picked rock and the computer picked rock,"
        " it is a draw")
    else:
        print("You picked rock and the computer picked paper, computer wins")
elif user_choice == paper:
    if computer_choice == scissor:
        print("You picked paper and the computer picked scissor, computer wins")
    elif computer_choice == rock:
        print("You picked paper and the computer picked rock, you win")
    else:
        print("You picked paper and the computer picked paper," 
        " it is a draw")
else:
    print("Invalid input, you can only type in 0, 1 or 2")