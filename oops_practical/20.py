#  Create a class Person with a constructor that takes a name and an age. Instantiate several Person objects with different names and ages.

class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

person1 = Person("Raju",20)
person2 = Person("rani", 23)
person3 = Person("Shyam", 33)

print(f"Name of first person is {person1.name} and his age is {person1.age}")
print(f"Name of first person is {person2.name} and his age is {person2.age}")
print(f"Name of first person is {person3.name} and his age is {person3.age}")
        