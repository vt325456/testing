from calculator.operations import add, subtract, divide, multiply
from calculator.Calculation import Calculation
from decimal import Decimal

class Calculator:
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        calculation = Calculation(a ,b, add)
        return calculation.get_Output()
    
    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        calculation = Calculation(a ,b, subtract)
        return calculation.get_Output()

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        calculation = Calculation(a ,b, multiply)
        return calculation.get_Output()
    
    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        calculation = Calculation(a, b, divide)
        return calculation.get_Output()