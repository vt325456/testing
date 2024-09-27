from calculator.operations import add, subtract, multiply, divide
from decimal import Decimal

class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    @staticmethod
    def create(a, b, operation):
        return Calculation(a, b, operation)

    def operate(self) -> Decimal:
        return self.operation(self.a, self.b)
    
    def repr(self):
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"