#Programmet lar brukeren taste inn et tall på desimal form og gir det
#tilsvarende binærtallet

def integral_part_to_binary(decimal_value):
    integral_part = int(decimal_value)
    binary = ""
    while integral_part > 0:
        binary = str(integral_part % 2) + binary
        integral_part //= 2
    return binary
    
def fractional_part_to_binary(decimal_value):
    decimal_value = float(decimal_value)
    binary = ""

    #Flytverdien er ikke nøyaktig
    fractional_part = round( ( decimal_value - int(decimal_value) ),
                            len( str(decimal_value) )  )

    count = 0
    while not( fractional_part == 1.0 or count > len( str(decimal_value) ) ):
        count += 1
        fractional_part = round(fractional_part * 2, 2)-int(fractional_part)*2
        binary += str( int(fractional_part) )
    return binary

def main():
    decimal_input = float(input("Enter a decimal number between 0 and 15: "))

    #Brukeren kan kun skrive inn tall mellom 0 og 15
    if 0 < decimal_input < 15: 
        print(integral_part_to_binary(decimal_input) + "," +
              fractional_part_to_binary(decimal_input) )
    else:
        print("Enter a number between 0-15")
    
main()