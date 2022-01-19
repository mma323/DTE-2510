#Programmet lar brukeren skrive inn en teller og en nevner for en brøk.
#Programmet avgjør om brøken er ekte eller uekte, dersom den er ekte blir
#det returnert en streng som sier at brøken er ekte, dersom brøken er uekte
#blir det returnert et heltall eller et blandet tall

numerator = int(input("Enter a numerator: "))
denominator = int(input("Enter a denominator: "))

if (numerator < denominator):
    print(f"{numerator} / {denominator} is a proper fraction")

#Uekte brøk der brøken blir et heltall (ikke blandet tall)
elif (numerator % denominator == 0): 
    fraction_to_integer = int(numerator / denominator)
    print(f"{numerator} / {denominator} is an improper fraction and it can "
    f"be reduced to {int(fraction_to_integer)}")

else:
    print(f"{numerator} / {denominator} is an improper fraction and its mixed"
        f"number is {numerator // denominator} + {numerator % denominator} / " 
        f"{denominator}")

