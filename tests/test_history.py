''' Testing the Calculations methods of Calculator '''
from decimal import Decimal
import pytest

from calculator.Calculation import Calculation
from calculator.Calculations import Calculations
from calculator.operations import add, subtract, multiply, divide

@pytest.fixture
def samples():
    """Doc"""
    Calculations.history_clear()

    Calculations.history_add(Calculation(Decimal('5'), Decimal('3'), add))
    Calculations.history_add(Calculation(Decimal('9'), Decimal('3'), divide))
    Calculations.history_add(Calculation(Decimal('4'), Decimal('3'), subtract))
    Calculations.history_add(Calculation(Decimal('5'), Decimal('3'), multiply))

def test_addcalculation():
    """Doc"""
    cal = Calculation(Decimal('2'),Decimal('3'), add)
    Calculations.history_add(cal)
    assert Calculations.history_latest() == cal

def test_gethistory(samples):
    """Doc"""
    history = Calculations.history_print()
    assert len(history) == 4

def test_clearhistory():
    """Doc"""
    Calculations.history_clear()
    assert len(Calculations.history_print()) == 0

def test_getlatest(samples):
    """Doc"""
    latest = Calculations.history_latest()
    assert latest.a == Decimal('5') and latest.b == Decimal('3')

def test_getlatestafterclear():
    """Doc"""
    Calculations.history_clear()
    assert Calculations.history_latest() is None

def test_find_by_operation_name(samples):
    """Doc"""
    adds = Calculations.history_get_operation("add")
    assert len(adds) == 1
    divides = Calculations.history_get_operation("divide")
    assert len(divides) == 1
