#Programmet lar brukeren taste inn et antall sekunder
#og returnerer dette skrevet som dager:timer:minutter:sekunder
#Det er uklart av oppgaveteksten om dager skal være med eller
#ikke, derfor er dette tatt med

def format(seconds):
    SECONDS_IN_MINUTE = 60
    SECONDS_IN_HOUR   =  SECONDS_IN_MINUTE * 60
    SECONDS_IN_DAY    =  SECONDS_IN_HOUR * 24
    
    days = seconds // SECONDS_IN_DAY
    days = add_zero_if_single_digit(days)
    seconds %= SECONDS_IN_DAY

    hours = seconds // SECONDS_IN_HOUR
    hours = add_zero_if_single_digit(hours)
    seconds %= SECONDS_IN_HOUR

    minutes = seconds // SECONDS_IN_MINUTE
    minutes = add_zero_if_single_digit(minutes)
    seconds %= SECONDS_IN_MINUTE

    seconds = add_zero_if_single_digit(seconds)

    days_hours_minutes_seconds = f"{days}:{hours}:{minutes}:{seconds}"

    return days_hours_minutes_seconds

def add_zero_if_single_digit(number):
    number = str(number) if number >= 10 else "0" + str(number)
    return number

def main():
    seconds_from_user = int(input("Enter total seconds: "))
    print("The days, hours, minutes, and seconds for total seconds " +
         f"{seconds_from_user} is {format(seconds_from_user)}")

if __name__ == "__main__":
    main()