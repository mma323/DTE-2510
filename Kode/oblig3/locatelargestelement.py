#Programmet lar brukeren skrive inn en todimensjonal liste og returnerer det
#største elementet i listen sin posisjon

def linear_search(list, key):

    for i in range( len(list) ):
        if list[i] == key:
            return i
        
    return -1

def locate_largest(list):

    max_values        = []
    max_value_columns = []
    for row in list:
        max_values.append( max(row) )
        max_value_columns.append( row.index( max(row) ) )

    max_value_row    = linear_search(max_values, max(max_values) )
    max_value_column = max_value_columns[max_value_row]

    position_of_largest = [max_value_row, max_value_column]

    return position_of_largest

def create_list():
    number_of_rows = int(input("Enter number of rows: "))

    list = []
    for i in range(number_of_rows):
        row = input("Enter a row: ")
        row = row.split()
        row = [float(number) for number in row] #Input returnerer string
        list.append(row)

    return list

def main():
    list_from_user = create_list()
    
    largest_element_position = locate_largest(list_from_user)

    print(f"The location of the largest element is at" +
           str(largest_element_position) )

if __name__ == "__main__":
    main()