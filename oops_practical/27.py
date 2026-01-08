# Implement a class called Person with attributes for name and age. Overload the < operator to compare the ages of two people and determine who is younger.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        if self.age < other.age:
            return True
        return False

p1 =Person("raju", 22)
p2 = Person("rani", 33)

if p2 < p1:
    print(f"{p2.name} is younger than {p1.name}")
else:
    print(f"{p1.name} is younger than {p2.name}")

# Operator Overloading Methods:
# __lt__(self, other)  -> Less than (<)
# __le__(self, other)  -> Less than or equal to (<=)
# __gt__(self, other)  -> Greater than (>)
# __ge__(self, other)  -> Greater than or equal to (>=)
# __eq__(self, other)  -> Equal to (==)
# __ne__(self, other)  -> Not equal to (!=)
#
# These methods define how objects of this class are compared
# using standard comparison operators based on custom logic.

    