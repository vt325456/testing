from calculator.operations import add, subtract, divide, multiply
from calculator.Calculation import Calculation
from calculator.History import History
from decimal import Decimal
from typing import Callable

class Calculator:

    @staticmethod
    def _do_operate(a: Decimal, b: Decimal, operation: Callable[[Decimal,Decimal], Decimal]):
        calculation = Calculation.create(a, b, operation)
        History.history_add(calculation)
        return calculation.operate()
    
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._do_operate(a,b,add)
    
    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._do_operate(a,b,subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._do_operate(a,b,multiply)
    
    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._do_operate(a,b,divide)
