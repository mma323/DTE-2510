#Tester for clock.py

import unittest  
from clock import Clock 

class Test_Clock(unittest.TestCase):
    def setUp(self):
        self.__clock = Clock()


    def test_increment_second_from_default_values(self):
        self.__clock.increment_second()
        self.assertEqual(self.__clock.clock_as_string(), "00:00:0000:00:00:01")


    def test_increment_second_from_end_of_january(self):
        self.__clock = Clock(31, 1, 2021, 23, 59, 59)
        self.__clock.increment_second()
        self.assertEqual(self.__clock.clock_as_string(), "01:02:2021:00:00:00")


    def test_increment_second_from_end_of_hour(self):
        self.__clock = Clock(1, 2, 2021, 22, 58, 59)
        self.__clock.increment_second()
        self.assertEqual(self.__clock.clock_as_string(), "01:02:2021:22:59:00")


    def test_increment_minute_from_default_values(self):
        self.__clock.increment_minute()
        self.assertEqual(self.__clock.clock_as_string(), "00:00:0000:00:01:00")


    def test_increment_minute_from_end_of_minute(self):
        self.__clock = Clock(1, 2, 2021, 22, 58, 59)
        self.__clock.increment_minute()
        self.assertEqual(self.__clock.clock_as_string(), "01:02:2021:22:59:59")


    def test_increment_minute_from_end_of_year(self):
        self.__clock = Clock(31, 12, 2021, 23, 59, 59)
        self.__clock.increment_minute()
        self.assertEqual(self.__clock.clock_as_string(), "01:01:2022:00:00:59")


    def test_increment_hour_from_default_value(self):
        self.__clock.increment_hour()
        self.assertEqual(self.__clock.clock_as_string(), "00:00:0000:01:00:00")


    def test_increment_hour_from_end_of_hour(self):
        self.__clock = Clock(3, 5, 2021, 19, 59, 59)
        self.__clock.increment_hour()
        self.assertEqual(self.__clock.clock_as_string(), "03:05:2021:20:59:59")


    def test_increment_hour_from_end_of_day(self):
        self.__clock = Clock(3, 5, 2021, 23, 59, 59)
        self.__clock.increment_hour()
        self.assertEqual(self.__clock.clock_as_string(), "04:05:2021:00:59:59")


    def test_increment_day_from_default_value(self):
        self.__clock.increment_day()
        self.assertEqual(self.__clock.clock_as_string(), "01:00:0000:00:00:00")


    def test_increment_day_from_end_of_february_in_leap_year(self):
        self.__clock = Clock(29, 2, 2024, 0, 0, 0)
        self.__clock.increment_day()
        self.assertEqual(self.__clock.clock_as_string(), "01:03:2024:00:00:00")


    def test_increment_day_from_end_of_february_in_common_year(self):
        self.__clock = Clock(28, 2, 2021, 0, 0, 0)
        self.__clock.increment_day()
        self.assertEqual(self.__clock.clock_as_string(), "01:03:2021:00:00:00")


    def test_increment_month_from_default_value(self):
        self.__clock.increment_month()
        self.assertEqual(self.__clock.clock_as_string(), "00:01:0000:00:00:00")


    def test_increment_month_from_end_of_may_to_june(self):
        self.__clock = Clock(31, 5, 2021, 0, 0, 0)
        self.__clock.increment_month()
        self.assertEqual(self.__clock.clock_as_string(), "01:07:2021:00:00:00")


    def test_increment_month_from_end_of_june_to_july(self):
        self.__clock = Clock(31, 8, 2021, 0, 0, 0)
        self.__clock.increment_month()
        self.assertEqual(self.__clock.clock_as_string(), "01:10:2021:00:00:00")


    def test_increment_year_from_default_value(self):
        self.__clock.increment_year()
        self.assertEqual(self.__clock.clock_as_string(), "00:00:0001:00:00:00")


    def test_increment_year_from_end_of_february_in_leap_year(self):
        self.__clock = Clock(29, 2, 2024, 3, 2, 1)
        self.__clock.increment_year()
        self.assertEqual(self.__clock.clock_as_string(), "01:03:2025:03:02:01")


    def test_increment_year_from_end_of_february_in_common_year(self):
        self.__clock = Clock(28, 2, 2021, 3, 2, 1)
        self.__clock.increment_year()
        self.assertEqual(self.__clock.clock_as_string(), "28:02:2022:03:02:01")

if __name__ == '__main__':
    unittest.main()