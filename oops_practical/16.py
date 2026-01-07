# Create a Student Class: Define a Student class with attributes for name, age, and grade. Create an instance of the class and print out the student's information.

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

student = Student("raju",20, "A")

print(f"Name of student is: {student.name}")
print(f"Age of student is: {student.age}")
print(f"Grade of student is: {student.grade}")