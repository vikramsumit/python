class Employee:
    companyname = "Luminent nexus"
    noofEmployees = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.5
        Employee.noofEmployees += 1
    def showdetails(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.companyname} is {self.raise_amount}.\n Total no of employee in company is{self.noofEmployees}")

emp1 = Employee("Rajubhai")
emp1.raise_amount = 0.7
Employee.companyname = "Google"
emp1.companyname = "AppleIndia"
emp1.showdetails()
# Employee.showdetails(emp1)

emp2 = Employee("Babubahi")
emp2.showdetails()