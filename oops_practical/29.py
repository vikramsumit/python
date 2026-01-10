# Define a base class "Employee" and create derived classes for different job roles (e.g., "Manager," "Technician," "HR"). Include attributes like "name," "employee_id," and role-specific methods for managing employee tasks.

class Employee:
    def __init__(self,name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.employee_id}")

class Manager(Employee):
    def __init__(self, name, employee_id, team_size):
        super().__init__(name, employee_id)
        self.team_size = team_size

    def manage_team(self):
        print(f"{self.name} is manageing a team of {self.team_size} members.")

class Technician(Employee):
    def __init__(self, name, employee_id, skill):
        super().__init__(name, employee_id)
        self.skill = skill

    def perform_task(self):
        print(f"{self.name} is performing {self.skill} tasks.")

class HR(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    def handle_recruitment(self):
        print(f"{self.name} is handling recruitment for {self.department}.")

manager = Manager("RAJU", "LKAJDFS", 250)
manager.display_info()
manager.manage_team()

print("---------------------------------------------")

technician = Technician("RAMU", "INS ARIHANT", "Repair")
technician.display_info()
technician.perform_task()

print("---------------------------------------------")

hr = HR("Shyam", "AHSDFK", "Marine")
hr.display_info()
hr.handle_recruitment()