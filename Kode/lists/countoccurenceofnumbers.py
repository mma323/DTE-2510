#Programmet tar i mot heltall mellom 1 og 100 og teller antall ganger hvert
#tall forekommer

def main():
    #Tallene skal skrives i stigende rekkefølge
    integers = sorted( get_integers() )
    
    #Kun heltall mellom 1 og 100 tillatt
    if min(integers) >= 1 and max(integers) <= 100:

        if all_elements_are_equal(integers):
            print_occurences_of_integer( integers[0], len(integers) )

        else:
            for i in range( len(integers) ):

                if integers[i] != integers[i - 1]:
                    integer_count = integers.count(integers[i])
                    print_occurences_of_integer(integers[i], integer_count )
    
    else:
        print("Only integers between 1 and 100 inclusive allowed")

def get_integers():
    integers = input("Enter integers between 1 and 100 inclusive: ") 
    integers = integers.split(" ")
    integers = [int(integer) for integer in integers]
    return integers
    
def all_elements_are_equal(list):
    first_element = list[0]
    for element in list:
        if element != first_element:
            return False
    
    return True

def print_occurences_of_integer(integer, integer_count):
    print(f"{integer} occurs {integer_count}", 
    "times" if integer_count> 1 else "time" 
    )

 
main()