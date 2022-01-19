#Programmet lar brukeren taste inn en streng og vurderer
#deretter det største antallet ganger et tegn i strengen
#forekommer rett etter hverandre

string_from_user = input("Enter a string: ")

#Så lenge brukeren taster inn noe, vil det være minimum et tegn 
consecutive_repeating_characters = 1
highest_number_of_consecutive_repeating_characters = 1

#Vil kun være et tegn dersom strengen er kortere enn eller lik et tegn
if len(string_from_user) > 1:

    max_index_of_string = len(string_from_user)-1 

    #Det siste tegnet i stringen har ikke et tegn etter seg
    for index_of_string in range(max_index_of_string):

        while string_from_user[index_of_string] == (
              string_from_user[index_of_string+1] ):

                consecutive_repeating_characters += 1

                #Det siste tegnet i stringen har ikke et tegn etter seg
                if index_of_string != (max_index_of_string-1):
                    index_of_string += 1
                else:
                    break

        #Skal finne det høyeste antallet ganger et tegn repeteres konsekutivt
        if consecutive_repeating_characters >= (
            highest_number_of_consecutive_repeating_characters):

                highest_number_of_consecutive_repeating_characters = (
                                     consecutive_repeating_characters)

        #Tilbakestilles før neste iterasjon
        consecutive_repeating_characters = 1   

print(string_from_user)
print(highest_number_of_consecutive_repeating_characters)
