# Exercise 4: Create an Employee Class and Manager Subclass

class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department
        self.subordinates = []

    def add_subordinate(self, employee):
        self.subordinates.append(employee)

    def display(self):
        super().display()
        print(f"Department: {self.department}")
        print(f"Subordinates: {[emp.name for emp in self.subordinates]}")

manager = Manager("Alice", 1001, 80000, "Engineering")
employee1 = Employee("Bob", 1002, 50000)
employee2 = Employee("Charlie", 1003, 45000)

manager.add_subordinate(employee1)
manager.add_subordinate(employee2)
manager.display()
