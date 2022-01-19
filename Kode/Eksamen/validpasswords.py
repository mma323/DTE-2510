class Password():
    def __init__(self, password):
        self.password = password
    
    def valid_password(self):
        password = self.password

        if len(password) < 7:
            return False
        
        contains_upper_case_letter = False
        contains_lower_case_letter = False
        contains_numeric_digit     = False

        for character in password:
            if character.isupper():
                contains_upper_case_letter = True
            if character.islower():
                contains_lower_case_letter = True
            if character.isnumeric():
                contains_numeric_digit = True

        if not contains_upper_case_letter:
            return False
        
        if not contains_lower_case_letter:
            return False
        
        if not contains_numeric_digit:
            return False
        
        return True
        