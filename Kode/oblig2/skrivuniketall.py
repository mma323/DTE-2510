#Programmet lar brukeren skrive inn tall og returnerer 
#en liste med de samme tallene, der duplikater er fjernet

def print_distinct_numbers(integers):
    integers = integers.split()
    printed_integers = []

    for i in range( len(integers) ):
        if integers[i] not in printed_integers:
            printed_integers.append(integers[i])

    return printed_integers

def main():
    integers_from_user = input("Type in integers seperated by space: ")
    print(print_distinct_numbers(integers_from_user))

if __name__ == "__main__":
    main()