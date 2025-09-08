class Calculator:
    def add(self, a: float, b: float) -> float:
        return a + b
    def subtract(self, a: float, b: float) -> float:
        return a - b
    def multiply(self, a: float, b: float) -> float:
        return a * b
    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    def modulus(self, a: int, b: int) -> int:
        if b == 0:
            raise ValueError("Cannot mod by zero.")
        return a % b
    def power(self, a: float, b: float) -> float:
        return a ** b

calc = Calculator()
print(calc.add(10, 5))        
print(calc.subtract(10, 5))   
print(calc.multiply(10, 5))   
print(calc.divide(10, 5))  
print(calc.modulus(10, 3))    
print(calc.power(2, 3))       


# Output:
''' raju@kali:~/code only/python/oops_practical % python3 04.py
15
5
50
2.0
1
8'''