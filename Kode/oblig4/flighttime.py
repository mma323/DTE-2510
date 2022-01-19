#Programmet inneholder klassene Flight og Itinerary, disse benyttes 
#til å regne den totale fly- og reisetiden for en gitt reiserute

import datetime

SECONDS_IN_MINUTE = 60

class Flight:
    def __init__(self, flight_number, departure_time, arrival_time):
        self.flight_number = flight_number
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    #Hver flight i en itinerary skal sorteres etter departure time
    def __lt__(self, other):
        return self.departure_time < other.get_departure_time()

    def get_flight_number(self):
        return self.flight_number

    def set_departure_time(self, departure_time):
        self.departure_time = departure_time

    def get_departure_time(self):
        return self.departure_time
    
    def set_arrival_time(self, arrival_time):
        self.arrival_time = arrival_time

    def get_arrival_time(self):
        return self.arrival_time

    def get_flight_time(self):

        flight_time = self.arrival_time - self.departure_time
        flight_time = flight_time.total_seconds()
        flight_time /= SECONDS_IN_MINUTE

        return flight_time

class Itinerary:
    def __init__(self, flights):
        self.flights = flights
        self.flights = sorted(self.flights)

    def get_total_flight_time(self):
        total_flight_time = 0
        for flight in self.flights:
            total_flight_time += flight.get_flight_time()

        return total_flight_time

    def get_total_travel_time(self):
        self.first_departure_time = self.flights[0].get_departure_time()

        self.arrival_times = ( 
            [flight.get_arrival_time() for flight in self.flights]
        )
        self.last_arrival_time = max( self.arrival_times )

        self.total_travel_time = ( 
            self.last_arrival_time - self.first_departure_time
        )
        self.total_travel_time = self.total_travel_time.total_seconds()
        self.total_travel_time /= SECONDS_IN_MINUTE

        return self.total_travel_time


def main():

    flights = []

    flights.append(Flight("US230",

        datetime.datetime(2014, 4, 5, 5, 5, 0),

        datetime.datetime(2014, 4, 5, 6, 15, 0)))

    flights.append(Flight("US235",

        datetime.datetime(2014, 4, 5, 6, 55, 0),

        datetime.datetime(2014, 4, 5, 7, 45, 0)))

    flights.append(Flight("US237",

        datetime.datetime(2014, 4, 5, 9, 35, 0),

        datetime.datetime(2014, 4, 5, 12, 55, 0)))


    itinerary = Itinerary(flights)

    print( itinerary.get_total_travel_time() )

    print( itinerary.get_total_flight_time() )


if __name__ == "__main__":
    main()