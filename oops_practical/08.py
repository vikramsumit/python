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

c = Compute()

choice = int(input("Enter 1 for square area, 2 for rectangle area: "))

if choice == 1:
    arsq =float(input("Enter side length for square: "))
    print("Area of square :", c.area(arsq))

elif choice == 2:
    arrec_length = float(input("Enter length for rectangle: "))
    arrec_breadth = float(input("Enter breadth for rectangle: "))
    print("Area of rectangle :", c.area(arrec_length, arrec_breadth))
else:
    print("Invalid choice")
