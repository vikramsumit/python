# Multiple Inheritance

# class Employee:
#   def __init__(self, name):
#     self.name = name
#   def show(self):
#     print(f"The name is {self.name}")

class Dancer:
  def __init__(self, dance):
    self.dance = dance

  def show(self):
    print(f"The dance is {self.dance}")

class DancerEmployee(Dancer, Employee):
  def __init__(self, dance, name):
    self.dance = dance
    self.name = name
    
class DancerEmployee1(Employee, Dancer):
  def __init__(self, dance, name):
    self.dance = dance
    self.name = name

o  = DancerEmployee("Kathak", "Raju")
o1  = DancerEmployee1("Kathak", "Raju")
print(o.name)
print(o.dance)
o1.show() 
o.show() 
print(DancerEmployee.mro())