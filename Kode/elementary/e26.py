#Programmet returnerer tallet brukeren skriver inn baklengs
#Funker for firesifrede tall

number_user = int(input("Enter an integer: "))


#Modulus regner ut hvilket tall som forsvinner ved en heltallsdivisjon
#Brukerens tall heltallsdivideres med 10, da forsvinner siste tall
new_first_digit = str(number_user % 10)   
number_user //= 10
new_second_digit = str(number_user % 10)
number_user //= 10
new_third_digit = str(number_user % 10)
number_user //= 10
new_last_digit = str(number_user % 10)

number_reversed = new_first_digit + new_second_digit + new_third_digit \
 + new_last_digit
print(number_reversed)