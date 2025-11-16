class Person:
    def __init__(self, person_id: int, name: str, age: int):
        self.id = person_id
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"Person(id={self.id}, name='{self.name}', age={self.age})"

p = Person(11, "Raju", 22)
p1 = Person(222, "Kaju", 333)
print(p,p1)  

# Output:
'''raju@kali:~/code only/python/oops_practical % python3 02.py                 
Person(id=11, name='Raju', age=22) Person(id=222, name='Kaju', age=333)'''

'''# create a class, take a method calculate_volume of the room.
class Room:
    def __init__(self, length: float, width: float, height: float):
        if length < 0 or width < 0 or height < 0:
            raise ValueError("Dimensions must be non-negative.")
        self.length = length
        self.width = width
        self.height = height

    def calculate_volume(self) -> float:
        return self.length * self.width * self.height

r = Room(25.5, 14.7, 9.8)
print("Room volume:", r.calculate_volume())  

# Output:
raju@kali:~/code only/python/oops_practical % python3 03.py
Room volume: 3673.5299999999997

# create a class Calculator. Include methods for basic arithmetic operations.
class Calculator:
    def add(self, a: float, b: float) -> float:
        return a + b
    def subtract(self, a: float, b: float) -> float:
        return a - b
    def multiply(self, a: float, b: float) -> float:
        return a * b
    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    def modulus(self, a: int, b: int) -> int:
        if b == 0:
            raise ValueError("Cannot mod by zero.")
        return a % b
    def power(self, a: float, b: float) -> float:
        return a ** b

calc = Calculator()
print(calc.add(10, 5))        
print(calc.subtract(10, 5))   
print(calc.multiply(10, 5))   
print(calc.divide(10, 5))  
print(calc.modulus(10, 3))    
print(calc.power(2, 3))       


# Output:
 raju@kali:~/code only/python/oops_practical % python3 04.py
15
5
50
2.0
1
8

# create a class Person. Take a default constructor where parameters are name and age. Display all details of that person.
class PersonDefault:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self) -> None:
        print(f"Name: {self.name}, Age: {self.age}")

p1 = PersonDefault("Bhanu", 55)                 
p2 = PersonDefault("Raju ", 22)       
p1.display()
p2.display()

# Output:
raju@kali:~/code only/python/oops_practical % python3 05.py
Name: Bhanu, Age: 55 
Name: Raju , Age: 22

# create a class Person. Take a parameterized constructor where arguments are name and age. Display all details of that person.
class PersonParam:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def display(self) -> None:
        print(f"Name: {self.name}, Age: {self.age}")

p = PersonParam("Raju", 524)
p.display()

# Output:
raju@kali:~/code only/python/oops_practical % python3 06.py
Name: Raju, Age: 524


# create a Python class Student. Take arguments name, age, roll no. Display()  (b) Use functions like get, set, del.
class Student:
    def __init__(self, name: str, age: int, roll_no: int):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def display(self) -> None:
        print(f"Name: {self.name}, Age: {self.age}, Roll No: {self.roll_no}")

s = Student("Raju", 20, 422)
s.display()

print("Has 'age'? ->", hasattr(s, "age"))                
print("Get 'name' ->", getattr(s, "name", "N/A"))        
setattr(s, "grade", "A")                                 
print("Get 'grade' ->", getattr(s, "grade", "N/A"))    
delattr(s, "grade")                                       
print("Has 'grade'? ->", hasattr(s, "grade"))            
print("Get 'grade' ->", getattr(s, "grade", "N/A"))    
print("Get 'roll_no' ->", getattr(s, "roll_no", "N/A"))  
print("Has 'roll_no'? ->", hasattr(s, "roll_no"))        
setattr(s, "roll_no", 45)                                  
print("Get 'roll_no' ->", getattr(s, "roll_no", "N/A"))  
s.display()

# Output:
raju@kali:~/code only/python/oops_practical % python3 07.py
Name: Raju, Age: 20, Roll No: 422
Has 'age'? -> True
Get 'name' -> Raju
Get 'grade' -> A
Has 'grade'? -> False
Get 'grade' -> N/A
Get 'roll_no' -> 422
Has 'roll_no'? -> True
Get 'roll_no' -> 45
Name: Raju, Age: 20, Roll No: 45
'''