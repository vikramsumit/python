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
'''raju@kali:~/code only/python/oops_practical % python3 07.py
Name: Raju, Age: 20, Roll No: 422
Has 'age'? -> True
Get 'name' -> Raju
Get 'grade' -> A
Has 'grade'? -> False
Get 'grade' -> N/A
Get 'roll_no' -> 422
Has 'roll_no'? -> True
Get 'roll_no' -> 45
Name: Raju, Age: 20, Roll No: 45'''