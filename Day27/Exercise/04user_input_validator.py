# Exercise 4: Validate User Input Using Static Methods

import re

class UserInputValidator:
    @staticmethod
    def is_valid_email(email):
        pattern = r"[^@]+@[^@]+\.[^@]+"
        return re.match(pattern, email) is not None

    @staticmethod
    def is_valid_phone_number(phone):
        pattern = r"^\d{10}$"
        return re.match(pattern, phone) is not None

print(UserInputValidator.is_valid_email("test@example.com"))  # Output: True
print(UserInputValidator.is_valid_phone_number("1234567890"))  # Output: True
