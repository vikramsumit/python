# Classes and Objects

class person:
    name = "raju"
    occupation = "comedian and actor"
    networth = "20"
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person()
b = person()
# a.name = "shyam"
# a.networth = "250"
print(a.name,a.occupation)
print(a.networth)
a.info()

b.name = "kaju"
b.occupation = "Dry fruiit"
b.info()

class Details:
    name = "Rohan"
    age = 20

    def desc(self):
        print("My name is", self.name, "and I'm", self.age, "years old.")

obj1 = Details()
obj1.desc()