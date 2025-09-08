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
