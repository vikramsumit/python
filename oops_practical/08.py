class Compute:
    def area(self, *args):
        # Square: 1 argument
        if len(args) == 1:
            side = args[0]
            return side * side
        
        # Rectangle: 2 arguments
        elif len(args) == 2:
            length, breadth = args
            return length * breadth
        
        else:
            return "Invalid number of arguments"

# Testing
c = Compute()
print("Area of square (side=5):", c.area(5))
print("Area of rectangle (6 x 4):", c.area(6, 4))
