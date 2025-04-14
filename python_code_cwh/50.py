class parentclass:
    def parent_method(self):
        print("This is parent class.")

class childclass(parentclass):
    def child_method(self):
        print("Raju")
        super().parent_method()
        print("This is child class.")
        super().parent_method()

child_object = childclass()
child_object.child_method()
child_object.parent_method()

