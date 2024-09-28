"""
Calculator class
----------------
Addition, subtraction, multiplication, and division are some of the fundamental arithmetic operations provided in the static `Calculator` class.
It creates and stores calculation history by using the `Calculation and `Calculations` classes.
"""
from calculator.operations import add, subtract, divide, multiply
from calculator.Calculation import Calculation
from calculator.Calculations import Calculations
from decimal import Decimal
from typing import Callable

class Calculator:
    """
    This is a Calculator class that provides basic arithmetic operations with the methods initialised to do arithmetic operations such as add, subtract, multiply, divide.
    """
    @staticmethod
    def _do_operate(a: Decimal, b: Decimal, operation: Callable[[Decimal,Decimal], Decimal]):
        """
        Calls the history_add and operate methods to add the calculation to the history and complete the operation.

        Args Passed:
        a (Decimal): The first operand.
        b (Decimal): The second operand.
        operation (Callable[[Decimal,Decimal], Decimal]): A callable function that takes two Decimals as parameters and returns a Decimal object.

        Returns a Decimal: The result of the operation performed.
        """
        calculation = Calculation.create(a, b, operation)
        Calculations.history_add(calculation)
        return calculation.operate()
    
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """
        This method takes two decimals as arguments to perform addition operation.

        Args Passed:
        a (Decimal): The first operand.
        b (Decimal): The second operand.

        Returns a Decimal: it is a addition of a and b.
        """
        return Calculator._do_operate(a,b,add)
    
    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """
        This method takes two decimals as arguments to perform subtraction operation.

        Args Passed:
        a (Decimal): The first operand.
        b (Decimal): The second operand.

        Returns a Decimal: it is a difference between a and b.
        """
        return Calculator._do_operate(a,b,subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """
        This method takes two decimals as arguments to perform multiplication operation.

        Args Passed:
        a (Decimal): The first operand.
        b (Decimal): The second operand.

        Returns a Decimal: product of the numbers a and b.
        """
        return Calculator._do_operate(a,b,multiply)
    
    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """
        This method takes two decimals as arguments to perform division operation.

        Args Passed:
        a (Decimal): The first operand.
        b (Decimal): The second operand.

        Returns a Decimal: division result of the numbers a by b.
        """
        return Calculator._do_operate(a,b,divide)