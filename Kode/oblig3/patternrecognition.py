#Programmet lar brukeren skrive en rekke med tall og sjekker hvorvidt rekken
#inneholder fire like tall etter hverandre

def is_consecutive_four(values):
    AMOUNT_OF_CONSECUTIVES = 4

    #-1 gjør at en får med siste verdien
    for i in range( len(values) - (AMOUNT_OF_CONSECUTIVES - 1) ):

        values_to_check = values[ i : (i + AMOUNT_OF_CONSECUTIVES) ]

        #Finnes minst en verdi av samme type
        value_count = 1  
        #Siste verdi har ingen neste verdi å sammenligne med
        for j in range( len(values_to_check) - 1 ):         

            if values_to_check[j] == values_to_check[j+1]:
                value_count = value_count + 1
            
            if value_count == AMOUNT_OF_CONSECUTIVES:
                return True
    
    return False

def main():
    integers_from_user = ( 
        input("Enter integers separated by spaces from one line:") )

    integers_from_user = integers_from_user.split()
    
    #Brukeren skal skrive inn heltall
    integers_from_user = [int(integer) for integer in  integers_from_user]

    if is_consecutive_four(integers_from_user):
        print("The series has consecutive fours")
    else:
        print("The series does not have consecutive fours")


if __name__ == "__main__":
    main()