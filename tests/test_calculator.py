"""
Calculator Test Module
----------------------
This module contains unit tests for the Calculator class, demonstrating the principle of encapsulation.
Each test method checks a different arithmetic operation (add, subtract, multiply, divide)
by calling the corresponding method from the Calculator class.
"""

from calculator import Calculator

def test_add():
    '''
    Testing the add method from the Calculator class (Calling operations.py function)
    Expected behavior : 2 + 3 = 5
    '''
    output = Calculator.add(2,3)
    assert  output == 5, "Addition test failed"

def test_subtract():
    '''
    Testing the subtract method from the Calculator class (Calling operations.py function)
    Expected behavior : 4 - 3 = 1
    '''
    output = Calculator.subtract(4,3)
    assert output == 1, "Subtraction test failed"

def test_multiply():
    '''
    Testing the multiply method from the Calculator class (Calling operations.py function)
    Expected behavior : 2 * 2 = 4
    '''
    output = Calculator.multiply(2,2)
    assert output == 4, "Multiplication test failed"

def test_divide():
    '''
    Testing the divide method from the Calculator class (Calling operations.py function)
    Expected behavior : 8 / 2 = 4
    '''
    output = Calculator.divide(8,2)
    assert output == 4, "Division test failed"
