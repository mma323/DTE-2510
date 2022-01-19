#Programmet lar brukeren skrive inn et heltall og sjekker om
#det er et palindromtall

def reverse(number):
    number = str(number)                     #Kan ikke indeksere inn i tall
    reversed_number = ""

    for i in range( len(number) ):
        reversed_number += number[-(i+1)]

    reversed_number = int(reversed_number)   #Funksjonen skal returnere et tall
    return reversed_number


def is_palindrome(number):
    if number == reverse(number):
        return True
    else:
        return False

def main():
    #is_palindrome() tar i mot et heltall
    number_from_user = int(input("Enter an integer: "))

    if is_palindrome(number_from_user):
        print(f"{number_from_user} is palindrome")
    else:
        print(f"{number_from_user} is not palindrome")


if __name__ == "__main__":
    main()