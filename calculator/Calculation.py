"""
Calculation Class
-----------------

The `Calculation` class will hold the methods to perform encapsulation of the calculation using the methods like create, operate and repr to create the calculation, perform 
the operation and format the operation with the desired string format for easy readability.
"""
from calculator.operations import add, subtract, multiply, divide
from decimal import Decimal
from typing import Callable

class Calculation:
    """
    Represents a calculation operation which takes two decimal objects and a callable function.
    """
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal,Decimal],Decimal]):
        '''
        Initializes a new object of calculation with Arguments a, b, operation function which takes two Decimal objects and returns
        a Decimal object.

        Args
        ----
        a (Decimal) : first operand
        b (Decimal) : second operand
        operation: Callable[[Decimal,Decimal],Decimal] : A callable function that takes two Decimal objects as arguments and returns a Decimal object.
        '''
        self.a = a
        self.b = b
        self.operation = operation

    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal,Decimal],Decimal]):
        """
        Creates a new Calculation object using the arguments passed and returns the created object.

        Args:
        a (Decimal): The first operand.
        b (Decimal): The second operand.
        operation (Callable[[Decimal,Decimal],Decimal]): A callable function that takes two Decimal objects as arguments and returns a Decimal object.

        Returns:
        Calculation: A new Calculation object created.
        """
        return Calculation(a, b, operation)

    def operate(self) -> Decimal:
        """
        This method will perform the operation by calling operation method pasing a and b as arguments.

        Returns:
        Decimal: The result of the operation performed.
        """
        return self.operation(self.a, self.b)
    
    def repr(self):
        """
        Returns a string representation of the Calculation object after formatting.

        Returns:
        str: Formatted string of the Calculation object like Calculation(a, b, operation_name).
        """
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"