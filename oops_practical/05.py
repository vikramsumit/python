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
'''raju@kali:~/code only/python/oops_practical % python3 05.py
Name: Bhanu, Age: 55 
Name: Raju , Age: 22'''
