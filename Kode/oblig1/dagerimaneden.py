#Programmet lar brukeren taste inn nummeret for en måned i et år
#og returnerer antall dager i måneden 

number_representing_month = int(input("Enter a month (Number 1-12): "))
year = int(input("Enter a year: "))

if number_representing_month == 1:
    print("There are 31 days in january")
elif number_representing_month==2:
    #Skuddår dersom året er delelig på 4 og ikke 100, eller på 400
    is_leap_year = (year % 4 == 0)
    is_leap_year = is_leap_year and not (year % 100 == 0)
    is_leap_year = is_leap_year or (year % 400 == 0)
    if is_leap_year:
        print(f"February of {year} has 29 days")
    else:
        print(f"February of {year} has 28 days")
elif number_representing_month==3:
    print("There are 31 days in march")
elif number_representing_month==4:
    print("There are 30 days in april")
elif number_representing_month==5:
    print("There are 31 days in may")
elif number_representing_month==6:
    print("There are 30 days in june")
elif number_representing_month==7:
    print("There are 31 days in july")
elif number_representing_month==8:
    print("There are 31 days in august")
elif number_representing_month==9:
    print("There are 30 days in september")
elif number_representing_month==10:
    print("There are 31 days in october")
elif number_representing_month==11:
    print("There are 30 days in november")
elif number_representing_month==12:
    print("There are 31 days in december")
else:
    print("Invalid input")
