import unittest
from validpasswords import *

class Test_Validpasswords(unittest.TestCase):
    def test_too_short_password(self):
        password = Password("Pass1")
        self.assertEqual(password.valid_password(), False)

    def test_only_digits(self):
        password = Password("2414234142")
        self.assertEqual(password.valid_password(), False)

    def test_only_lower_case_letters(self):
        password = Password("onlylowercaseletters1")
        self.assertEqual(password.valid_password(), False)

    def test_missing_lower_case_letter(self):
        password = Password("MISSINGLOWERCASE123")
        self.assertEqual(password.valid_password(), False)

    def test_only_upper_case_letters(self):
        password = Password("ONLYUPPERCASE2")
        self.assertEqual(password.valid_password(), False)

    def test_correct_password(self):
        password = Password("CorrectPassword123")
        self.assertEqual(password.valid_password(), True)
        
if __name__ == '__main__':
    unittest.main()