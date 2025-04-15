# class parentclass:
#     def parent_method(self):
#         print("This is parent class.")

# class childclass(parentclass):
#     def child_method(self):
#         print("Raju")
#         super().parent_method()
#         print("This is child class.")
#         super().parent_method()

# child_object = childclass()
# child_object.child_method()
# child_object.parent_method()

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, expertise):
        # self.name = name
        # self.id = id
        super().__init__(name,id)
        self.expertise = expertise
        
ram = Employee("Ram", "94387")
shyam = Programmer("Shyam", "3947", "PYTHON")
print(shyam.expertise)
print(shyam.id)