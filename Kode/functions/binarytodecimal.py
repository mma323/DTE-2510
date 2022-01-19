#Programmet lar brukeren taste inn et tall på binær form
#og returnerer det tilsvarende tallet på desimal form

def binary_to_decimal(binary_string):
    decimal_number = 0
    for i in range(0, len(binary_string)):
        decimal_place = len(binary_string) - 1 - i
        decimal_number += ( int(binary_string[i]) ) * 2**(decimal_place)
    return decimal_number

def main():
    decimal_number_from_user = input("Enter binary number:")
    print(binary_to_decimal(decimal_number_from_user))

main()
