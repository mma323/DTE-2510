#Programmet lar brukeren taste inn et tresifret tall og avgjør 
#om det er et palindromtall eller ikke

number_from_user = int(input("Enter an integer: "))

#Brukeren kan kun taste inn tall med tre sifre
if 100 <= number_from_user <=999: 

    #Resten ved heltallsdivisjon (av brukerens tall med 10) gir det siste 
    #sifferet
    #Heltallsdivisjon av tallet fjerner siste siffer
    #Konverteres fra int til str slik at tallene ikke adderes
    
    number_to_be_reversed = number_from_user
    first_digit_of_reversed_number = str(number_to_be_reversed % 10)   
    number_to_be_reversed //= 10                                         
    second_digit_of_reversed_number = str(number_to_be_reversed % 10)    
    number_to_be_reversed //= 10                                         
    third_digit_of_reversed_number = str(number_to_be_reversed % 10)     

    number_reversed = (first_digit_of_reversed_number +
                       second_digit_of_reversed_number +
                       third_digit_of_reversed_number)

    #Variabelen skal sammenlignes med number_from_user, som er et heltall
    number_reversed = int(number_reversed) 

    if number_from_user == number_reversed:
        print(f"{number_from_user} is a palindrome number")
    else:
        print(f"{number_from_user} is not a palindrome number")

else:
    print("Invalid input, only three-digit numbers are allowed")