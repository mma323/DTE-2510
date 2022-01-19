#En klasse Clock med metoder for å manipulere denne

MONTHS_31 = [1, 3, 5, 7, 8, 10, 12]
MONTHS_30 = [4, 6, 9, 11]

class Clock:
    def __init__(self, day=0, month=0, year=0, hour=0, minute=0, second=0):
        self.__day = day
        self.__month = month
        self.__year = year
        self.__hour = hour
        self.__minute = minute
        self.__second = second
        
    def increment_second(self):
        self.__second += 1
        if self.__second == 60:
            self.__second = 0
            self.increment_minute()

    def increment_minute(self):
        self.__minute += 1
        if self.__minute == 60:
            self.__minute = 0
            self.increment_hour()

    def increment_hour(self):
        self.__hour += 1
        if self.__hour == 24:
            self.__hour = 0
            self.increment_day()

    def increment_day(self):
        if self.__should_change_month(self.__year):
            self.__day = 1
            self.increment_month()
        else:
            self.__day += 1

    def increment_month(self):
        if ( self.__month in MONTHS_31 and 
             self.__day == 31  and 
             (self.__month + 1) in MONTHS_30
            ):

            self.__month += 2
            self.__day = 1

        elif ( self.__month == 1 and 
               self.__day == 31 and 
               self.__is_leapyear(self.__year) 
            ):

            self.__month += 2
            self.__day = 2

        elif self.__month == 1 and self.__day == 31:
            self.__month += 2
            self.__day = 3
        
        else:
            self.__month += 1


        if self.__month > 12:
            self.__month = 1
            self.increment_year()

    def increment_year(self):
        if (self.__is_leapyear(self.__year) and 
            self.__month == 2 and 
            self.__day == 29
        ):
            self.set_clock(1, 
                           3, 
                           self.__year + 1, 
                           self.__hour, 
                           self.__minute, 
                           self.__second)
        else:
            self.__year += 1

    def __should_change_month(self, year):
        if self.__month in MONTHS_31 and self.__day == 31:
            return True
        elif self.__month in MONTHS_31 and self.__day == 30:
            return True
        elif self.__month == 2 and self.__day == 28:
            return True
        elif self.__is_leapyear(year) and self.__day == 28:
            return False
        elif self.__is_leapyear(year) and self.__day == 29:
            return True
        return False

    def __is_leapyear(self, year):
        is_leap_year = (year % 4 == 0)
        is_leap_year = is_leap_year and not (year % 100 == 0)
        is_leap_year = is_leap_year or (year % 400 == 0)
        return is_leap_year

    def clock_as_string(self):
        return ( f"{self.__day:02d}:{self.__month:02d}:{self.__year:04d}:" +
                 f"{self.__hour:02d}:{self.__minute:02}:{self.__second:02}"        
        )

    def set_clock(self, day, month, year, hour, minute, second):
        self.__day = day
        self.__month = month
        self.__year = year
        self.__hour = hour
        self.__minute = minute
        self.__second = second

def main():
    clock = Clock(29, 2, 2024, 0, 0, 0)
    clock.increment_year()
    s = clock.clock_as_string()
    print(s)

if __name__ == "__main__":
    main()