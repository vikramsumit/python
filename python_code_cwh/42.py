# Access Modifiers in python

class Employee:
    def __init__(self):
        self.__name = "Raju bhai"
        self.address = "New york"

a = Employee()
# print(a.__name) #cannot access directly
print(a._Employee__name) #can be accessed indirectly
print(a.address)
print(a.__dir__())

#protected methods
class Student:
    def __init__(self):
        self._name = "Raju"

    def _funName(self):      # protected method
        return "CodeWithRaju"

class Subject(Student):       #inherited class
    def __init__(self):
        self._subject = "social study"

obj = Student()
obj1 = Subject()
# print(dir(obj))

print(obj._name)      
print(obj._funName()) 
print(obj1._subject)    
# calling by object of Subject class
# print(obj1._name)    
print(obj1._funName())
print(dir(obj))
print(dir(obj1))