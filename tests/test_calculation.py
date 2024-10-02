"""
Calculation Test Module
-----------------------
This module consists of the unit tests for the Calculation class and its operations performed.

It will use pytest and parametrize, testing and the decimal module to precide decimal arithmetic.
"""
from decimal import Decimal
import pytest
from calculator.Calculation import Calculation
from calculator.operations import add,divide

def test_operate(a, b, operation, expected):
    """
    Test for the operate method of calculation class for various operations. This test verifies that the calculation class will perform operations like add, subtract, multiply,
    divide properly

    Args : 
    a, b : (Decimal) : The Operands.
    operation(function) : the operation that needs to be performed.
    expected (Decimal) : The expected result for the operation performed.

    Raises:
    AssertionError : If the calculated result dont match with the expected result.
    """
    calc = Calculation(a, b, operation)
    assert calc.operate() == expected, f"Operation {operation.__name__} has been failed!!"

def test__repr():
    """
    Test for the _repr method of the Calculation class. This test will verify that the string representation created for Calculation object if it is correctly formatted.

    Raises:
        AssertionError: If the string representation dont match the expected format
    """
    obj = Calculation(Decimal('5'), Decimal('5'), add)
    assert obj.repr() == "Calculation(5, 5, add)", "String format is not matching with the expected output"


def test_dividebyzero():
    '''
    Tests for the divide method of the Calculation class if the method returns a ValueError when the second operand that is passed in equal to zero.
    asserts if it matches the error string as well.

    Raises:
        AssertionError: If a ValueError with the specific message is not raised
    '''
    obj = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        obj.operate()
