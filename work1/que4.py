# Que 4)    Write a Python program to create a calculator class. Include methods for
#           basic arithmetic operations.



class Calcu:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error"
        return a / b

calc = Calcu()

# 
print("Addition:", calc.add(10, 5))         # Output: 15
print("Subtraction:", calc.subtract(10, 5)) # Output: 5
print("Multiplication:", calc.multiply(10, 5)) # Output: 50
print("Division:", calc.divide(10, 5))      # Output: 2.0
print("Division by zero:", calc.divide(10, 0)) # Output: Error: Division by zero
