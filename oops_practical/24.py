# Create a simple calculator class with method overloading for addition and multiplication. The class should have a method called calculate() that takes variable arguments. Depending on the number of arguments, it should perform either addition or multiplication.  

class Calculator:
    def calculate(self, *args):
        if len(args) < 2:
            raise ValueError("At least two numbers are requires")
        
        if len(args) == 2:
            return args[0] + args[1]
        
        if len(args) > 2:
            result = 1
        for num in args:
            result *= num
        return result
    
calc = Calculator()

# print(calc.calculate(2))
# print(calc.calculate(r))
print(calc.calculate(2,6))
print(calc.calculate(2,4,3,23,45))
