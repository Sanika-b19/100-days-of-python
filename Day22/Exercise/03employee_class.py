# Exercise 3: Create an Employee Class with Methods

class Employee:
    def __init__(self, name, position, salary, years_of_service):
        self.name = name
        self.position = position
        self.salary = salary
        self.years_of_service = years_of_service

    def give_raise(self, amount):
        self.salary += amount

    def annual_salary(self):
        return self.salary * 12

    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Monthly Salary: ${self.salary:.2f}")
        print(f"Years of Service: {self.years_of_service}")
        print(f"Annual Salary: ${self.annual_salary():.2f}")

employee = Employee("Jane Doe", "Manager", 5000, 5)
employee.give_raise(500)
employee.display()
