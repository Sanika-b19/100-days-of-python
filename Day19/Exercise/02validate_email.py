# Exercise 2: Validate Email Address Format

def validate_email(email):
    if "@" not in email or "." not in email:
        raise ValueError("Invalid email address format.")
    return True

try:
    validate_email("invalid-email")
except ValueError as e:
    print(e)   
