# Exercise 3: Polymorphism with Employees

class Employee:
    def work(self):
        pass

class Manager(Employee):
    def work(self):
        return "Managing the team"

class Developer(Employee):
    def work(self):
        return "Writing code"

class Designer(Employee):
    def work(self):
        return "Designing user interfaces"
 
employees = [Manager(), Developer(), Designer()]

for employee in employees:
    print(employee.work())
