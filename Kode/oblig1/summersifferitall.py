#Programmet tar i mot et heltall mellom 0 og 1000 fra bruker
#og skriver ut summen av sifrene i tallet


#To ulike variabler, slik at integer_from_user kan benyttes til å skrive ut
#brukerens originale tall til slutt
integer_from_user = int(input("Enter an integer between 0 and 1000: "))
integer_used_to_calculate_sum_of_digits = integer_from_user 


#Brukeren kan kun benytte verdier fra og med 0 til 1000
if (0 <= integer_from_user < 1000 ):
    
    #Resten ved heltallsdivisjon (av brukerens tall med 10) gir det siste 
    #sifferet
    #Heltallsdivisjon av tallet fjerner siste siffer
    
    digit_1 = integer_used_to_calculate_sum_of_digits % 10      
    integer_used_to_calculate_sum_of_digits //= 10              
    digit_2 = integer_used_to_calculate_sum_of_digits % 10
    integer_used_to_calculate_sum_of_digits //= 10
    digit_3 = integer_used_to_calculate_sum_of_digits % 10

    sum_of_digits = digit_1 + digit_2 + digit_3

    print(f"The sum of the digits in {integer_from_user} is {sum_of_digits}")
    
else:
    print("Invalid input, only numbers from 0 to 999 are allowed")
