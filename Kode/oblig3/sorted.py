#Programmet lar brukeren skrive inn et sett med tall og returnerer
#True dersom tallene er sortert i stigende rekkefølge og False hvis ikke

def selection_sort(list):
    
    #Ønsker ikke at den originale listen skal endres
    sorted_list = [item for item in list]

    for i in range(len(sorted_list)):

        currently_not_sorted = sorted_list[i : ]
        current_minimum = min(currently_not_sorted)
        current_minimum_index = i + currently_not_sorted.index(current_minimum)

        if current_minimum_index != i:
            sorted_list[current_minimum_index], sorted_list[i] = (
            sorted_list[i], current_minimum )
        
    return sorted_list


def is_sorted(list):
    return list==selection_sort(list)


def main():
    numbers_from_user = input("Enter numbers separated by space: ")

    list_of_numbers = numbers_from_user.split()
    #Det er tall som sorteres
    list_of_numbers = [int(number) for number in list_of_numbers]

    print(is_sorted(list_of_numbers))


if __name__ == "__main__":
    main()