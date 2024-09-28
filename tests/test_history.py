"""
Calculations History Test Module
--------------------------------

This module contains unit tests for the Calculations class, which manages a history of calculator operations.
The tests cover various methods related to adding, retrieving, manipulating and deleting calculation history.
"""
from decimal import Decimal
import pytest

from calculator.Calculation import Calculation
from calculator.Calculations import Calculations
from calculator.operations import add, subtract, multiply, divide

@pytest.fixture
def samples():
    """
    Pytest fixture is used to setup a sample Calculation history. This will first clear the history and add the sample
    calculations using different arithmetic operations like (add, subtract, multiply, divide)
    """
    Calculations.history_clear() # Clears the history list.

    Calculations.history_add(Calculation(Decimal('5'), Decimal('3'), add))
    Calculations.history_add(Calculation(Decimal('9'), Decimal('3'), divide))
    Calculations.history_add(Calculation(Decimal('4'), Decimal('3'), subtract))
    Calculations.history_add(Calculation(Decimal('5'), Decimal('3'), multiply))

def test_addcalculation():
    """
    Testing the addition of history operation. This will verify whether the calculation is correctly added into the history,
    it will become the latest entry to the history.
    """
    cal = Calculation(Decimal('2'),Decimal('3'), add)
    Calculations.history_add(cal)
    assert Calculations.history_latest() == cal, "Calculation is not correctly added into History"

def test_gethistory(samples):
    """
    Testing the history retrieval of the calculations made. This test checks if the history contains the correct number of entries in it
    after the sample calculations have been added.
    """
    history = Calculations.history_print()
    assert len(history) == 4, "History is not updated with correct count of calculations."

def test_clearhistory():
    """
    Testing whether the clear function of the history is working correctly. Verifies whether the history is delted after performing clear operation
    """
    Calculations.history_clear()
    assert len(Calculations.history_print()) == 0, "History is not empty."

def test_getlatest(samples):
    """
    Test to retrieve the latest calculation of the history. This verifies if the latest calculation in the history matches to last one of the samples added.
    """
    latest = Calculations.history_latest()
    assert latest.a == Decimal('5') and latest.b == Decimal('3'), "Latest calculation doesnt match the last added value"

def test_getlatestafterclear():
    """
    Test to get the latest after clearing the history. This will verify the history list should be empty after doing a clear operation.
    """
    Calculations.history_clear()
    assert Calculations.history_latest() is None, "History should be empty after clear"

def test_find_by_operation_name(samples):
    """
    Test to find the list of calculations using the filter of operation_name from the samples entered. This will verify the correct number of calculations
    are present in the history with the operation_name that is specified.
    """
    adds = Calculations.history_get_operation("add")
    assert len(adds) == 1
    divides = Calculations.history_get_operation("divide")
    assert len(divides) == 1
