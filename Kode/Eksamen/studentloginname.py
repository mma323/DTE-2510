def get_login_name(first_name, last_name, id_number):
    first_name_part = first_name
    last_name_part = last_name
    id_number_part = id_number

    if len(first_name) >= 3:
        first_name_part = ""
        for i in range(3):
            first_name_part += first_name[i]
    
    if len(last_name) >= 3:
        last_name_part = ""
        for i in range(3):
            last_name_part += last_name[i]
    
    if len(id_number) >= 3:
        id_number_part = ""
        for i in range(-3, 0, 1):
            id_number_part += id_number[i]

    login_name = first_name_part + last_name_part + id_number_part

    return login_name

def main():
    first_name = "Amanda"
    last_name = "Spencer"
    id_number = "ENG6721"
    login_name = get_login_name(first_name, last_name, id_number)
    print(login_name)

if __name__ == "__main__":
    main()

    

