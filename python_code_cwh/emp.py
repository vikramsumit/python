class Employee:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i += 1
        return i

    def __str__(self):
        return f"The name of the employee is {self.name} str"

    def __repr__(self):
        return f"Employee('{self.name}')"

    def __call__(self):
        print("Hey I am good")


class StudentEvaluator:
    def __init__(self, passing_marks=40):
        self.passing_marks = passing_marks

    def __call__(self, name, marks):
        if marks >= self.passing_marks:
            print(f"{name} has PASSED with {marks} marks.")
        else:
            print(f"{name} has FAILED with {marks} marks.")
