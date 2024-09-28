"""
Operations module
-----------------
This module provides the methods for the arithmetic operations like add, subtract, multiply, divide where every method takes two Decimal objects and returns a Decimal object.
"""
from decimal import Decimal

def add(a: Decimal, b: Decimal) -> Decimal:
    '''
    Performs the addition operation
    Args : a(Decimal),b(Decimal) : Operands
    returns : Decimal : addition of two operands 
    '''
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    '''
    Performs the subtraction operation
    Args : a(Decimal),b(Decimal) : Operands
    returns : Decimal : subtraction of two operands 
    '''
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    '''
    Performs the multiplication operation
    Args : a(Decimal),b(Decimal) : Operands
    returns : Decimal : multiplication of two operands 
    '''
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    '''
    Raises ValueError when the value of second operand is equal to zero or it will perform a divsion operation on two operands.
    Args : a(Decimal),b(Decimal) : Operands
    returns : Decimal : Division of two operands
    Raises : raises a ValueError when second operand is equal to zero 
    '''
    if b == 0 :
        raise ValueError("DivideByZero Exception Occured")
    else:
        return a / b