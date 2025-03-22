class Mukund:
    def eat(self):
        print("Mukund is vegetarian. eats sb pussy")

class Study(Mukund):
    def read(self):
        print("Studying too much all the time.")

class Work(Study):
    def work(self):
        print("Working too much all the time.")

class Marriage(Mukund):
    def enjoy(self):
        print("Lover of SB.")

class BoyType(Mukund):
    def boytype(self):
        print("Mukund is a fuck boy.")


my_mukund = Mukund()
my_mukund.eat()

my_study = Study()
# my_study.eat()  
my_study.read()

my_work = Work()
# my_work.eat()  
# my_work.read() 
my_work.work()

my_marriage = Marriage()
# my_marriage.eat()  
my_marriage.enjoy()

my_boytype = BoyType()
# my_boytype.eat()  
my_boytype.boytype()
