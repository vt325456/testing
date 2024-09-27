""" Module String """
from decimal import Decimal
import pytest
from calculator.Calculation import Calculation
from calculator.operations import add,subtract,multiply,divide

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
    ''' method documentation '''
    calc = Calculation(value1, value2, operation)
    assert calc.operate() == expected, f"Operation {operation.__name__} has been failed!!"

def test__repr():
    ''' method documentation '''
    obj = Calculation(Decimal('5'), Decimal('5'), add)
    assert obj.repr() == "Calculation(5, 5, add)"


def test_dividebyzero():
    ''' method documentation '''
    obj = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="DivideByZero Exception Occured"):
        obj.operate()
