# Exercise : To check whether a number is palindrome or not

def is_palindrome(number):
    # Convert the number to a string
    str_num = str(number)
    # Reverse the string
    reversed_str_num = str_num[::-1]

    if str_num == reversed_str_num:
        return True
    else:
        return False

number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
