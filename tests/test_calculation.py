"""
Calculation Test Module
-----------------------
This module consists of the unit tests for the Calculation class and its operations performed.

It will use pytest and parametrize, testing and the decimal module to precide decimal arithmetic.
"""
from decimal import Decimal
import pytest
from calculator.Calculation import Calculation
from calculator.operations import add,subtract,multiply,divide

# parametrized test for all the types of operations
@pytest.mark.parametrize("value1, value2, operation, expected",
[
    (Decimal('2'), Decimal('2'), add, Decimal('4')),
    (Decimal('2'), Decimal('2'), subtract, Decimal('0')),
    (Decimal('2'), Decimal('2'), multiply, Decimal('4')),
    (Decimal('10'), Decimal('2'), divide, Decimal('5')),
    (Decimal('4'), Decimal('3'), add, Decimal('7')),
    (Decimal('4'), Decimal('3'), subtract, Decimal('1')),
    (Decimal('10'), Decimal('3'), multiply, Decimal('30')),
    (Decimal('14'), Decimal('2'), divide, Decimal('7')),
])

def test_operate(value1, value2, operation, expected):
    """
    Test for the operate method of calculation class for various operations. This test verifies that the calculation class will perform operations like add, subtract, multiply,
    divide properly

    Args : 
    value1, value2 : (Decimal) : The Operands.
    operation(function) : the operation that needs to be performed.
    expected (Decimal) : The expected result for the operation performed.

    Raises:
    AssertionError : If the calculated result dont match with the expected result.
    """
    calc = Calculation(value1, value2, operation)
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
    with pytest.raises(ValueError, match="DivideByZero Exception Occured"):
        obj.operate()
