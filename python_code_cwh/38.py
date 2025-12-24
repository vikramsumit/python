# Constructor

class Details:
  def __init__(self):
    print("animal Crab belongs to Crustaceans group")

Details()

class person:
    def __init__(self, n, o):
        print("Hey i am a person")
        self.name = n
        self.occ = o
        
    def info(self):
        print(f"{self.name} is a {self.occ}")
    
a = person("raju", "Developer")
b = person("rani", "hr")
# c = person(21,34,2)
c = person(21,34)
a.info()
b.info()
c.info()
