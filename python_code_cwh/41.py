class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def showdetails(self):
        print(f"The name of employee : {self.id} is {self.name}")
        
class Programmer(Employee):
    def showlanguage(self):
        print("currently we are studying python")
    

e = Employee("raju", 236)
e.showdetails()

e2 = Programmer("Raja raj", 2360)
e2.showdetails()
e2.showlanguage()