# Exercise : BMI Calculator

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

print(f"Your BMI is {bmi:.2f}.")