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