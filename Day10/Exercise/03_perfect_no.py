# Exercise : To check no is a perfect no or not

def is_perfect_number(number):
    if number < 1:
        return False

    # Find the sum of proper divisors
    sum_of_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i

    return sum_of_divisors == number

number = int(input("Enter a number: "))
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
