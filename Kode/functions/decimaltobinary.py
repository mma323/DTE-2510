#Programmet lar brukeren taste inn et heltall på desimal form og gir det
#tilsvarende binærtallet

def decimal_to_binary(decimal_value):
    binary = ""
    while decimal_value > 0:
        binary = str(decimal_value % 2) + binary
        decimal_value //= 2
    return binary

def main():
    decimal_input_from_user = int(input("Enter an integer: "))
    print(f"The binary value is {decimal_to_binary(decimal_input_from_user)}")

main()
