#Programmet simulerer en bean machine/quincunx/Galton box

import random

def generate_path(number_of_slots):
    LEFT = 0
    RIGHT = 1
    path = ""

    #En rekke mindre med pegs enn antall slots 
    for i in range(number_of_slots-1):                   

        direction = random.randint(LEFT, RIGHT)
        if direction == LEFT:
            path += 'L'
        #Kun venstre og høyre er alternativer
        else:             
            path += 'R'

    return path

def get_ball_position(path):

    amount_of_R = 0
    for i in range( len(path) ):
        if path[i] == 'R':
            amount_of_R += 1
        
    ball_position = amount_of_R
    
    return ball_position

    
def bean_machine(number_of_balls, number_of_slots):
    slots = [0] * number_of_slots

    for i in range(number_of_balls):

        path = generate_path(number_of_slots)
        print(path)
        ball_position = get_ball_position(path)
        slots[ball_position] += 1
    
    return slots

def generate_histogram(slots):
    for i in range(max(slots), 0, -1 ):

        row = [" "] * len(slots)
        for j in range( len(slots) ):
            if slots[j] >= i:
                row[j] = 'O'
        
        print("".join(row))

def main():

    number_of_balls = int( input("Enter the number of balls to drop: ") )
    number_of_slots = int( input("Enter the number of slots: ") )

    result = bean_machine(number_of_balls, number_of_slots)
    generate_histogram(result)
    

if __name__ == "__main__":
    main()
