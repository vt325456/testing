''' My Calculator Test using Calculator object'''
from calculator import Calculator

def test_add():
    '''Testing the add method from the Calculator class (Calling operations.py function)'''
    output = Calculator.add(2,3)
    assert  output == 5

def test_subtract():
    '''Testing the subtract method from the Calculator class (Calling operations.py function)'''
    output = Calculator.subtract(4,3)
    assert output == 1

def test_multiply():
    '''Testing the multiply method from the Calculator class (Calling operations.py function)'''
    output = Calculator.multiply(2,2)
    assert output == 4

def test_divide():
    '''Testing the divide method from the Calculator class (Calling operations.py function)'''
    output = Calculator.divide(8,2)
    assert output == 4
