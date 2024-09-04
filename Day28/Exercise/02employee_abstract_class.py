# Exercise 2: Abstract Employee Class

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def get_details(self):
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return self.base_salary

    def get_details(self):
        return f"Full-Time Employee: {self.name}, Salary: {self.calculate_salary()}"

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, hourly_rate)
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.base_salary * self.hours_worked

    def get_details(self):
        return f"Part-Time Employee: {self.name}, Salary: {self.calculate_salary()}"
 
employees = [
    FullTimeEmployee("Alice", 50000),
    PartTimeEmployee("Bob", 20, 120)
]

for employee in employees:
    print(employee.get_details())
