class PersonParam:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def display(self) -> None:
        print(f"Name: {self.name}, Age: {self.age}")

p = PersonParam("Raju", 524)
p.display()

# Output:
'''raju@kali:~/code only/python/oops_practical % python3 06.py
Name: Raju, Age: 524'''