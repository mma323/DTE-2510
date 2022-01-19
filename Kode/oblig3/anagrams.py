#Programmet lar brukeren skrive inn to ord og sjekker om de er anagrammer eller
#ikke

def selection_sort(list):
    
    #Ønsker ikke at den originale listen skal endres
    sorted_list = [item for item in list]

    for i in range( len(sorted_list) ):

        currently_not_sorted = sorted_list[i : ]
        current_minimum = min(currently_not_sorted)
        current_minimum_index = i + currently_not_sorted.index(current_minimum)

        if current_minimum_index != i:
            sorted_list[current_minimum_index], sorted_list[i] = (
            sorted_list[i], current_minimum )
        
    return sorted_list


def get_characters_in_word(word):
    word_characters = [character for character in word]
    return word_characters


def is_anagram(s1, s2):

    s1_characters = get_characters_in_word(s1)
    s2_characters = get_characters_in_word(s2)
    
    if selection_sort(s1_characters) == selection_sort(s2_characters):
        return True
    
    else:
        return False


def main():
    first_string  = input("Enter the first string: ")
    second_string = input("Enter the second string: ")

    if is_anagram(first_string, second_string):
        print(f"{first_string} and {second_string} are anagram")
    else:
        print(f"{first_string} and {second_string} are not anagrams")


if __name__ == "__main__":
    main()