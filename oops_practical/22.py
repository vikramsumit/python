# Employee Constructor: Design an Employee class with a constructor that takes a name, employee ID, and salary. Create instances of employees with different information.

class Employee:
    def __init__(self, name, employee_ID, salary ):
        self.name = name
        self.id = employee_ID
        self.salary = salary

employee1 = Employee("Raju", 420, 45000)

print(f"Name:{employee1.name}\nID:{employee1.id}\nSALARY:{employee1.salary}")
