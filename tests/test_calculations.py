"""
Tests for the Calculations class
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract

@pytest.fixture
def calculations():
    """
    Create a history of calculations
    """
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))

def test_add_calculation():
    """
    Test that a calculation is added to the history
    """
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    Calculations.add_calculation(calc)
    assert Calculations.last_calculation() == calc, "Failed to add the calculation to the history"

def test_history():
    """
    Test that the history contains the expected number of calculations
    """
    Calculations.clear_history()
    calc1 = Calculation(Decimal('10'), Decimal('5'), add)
    calc2 = Calculation(Decimal('20'), Decimal('3'), subtract)
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)
    history = Calculations.history()
    assert len(history) == 2, "History does not contain the expected number of calculations"

def test_clear_history():
    """
    Test that the history is cleared
    """
    Calculations.clear_history()
    assert len(Calculations.history()) == 0, "History was not cleared"

def test_last_calculation():
    """
    Test that the last calculation is returned
    """
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))
    latest = Calculations.last_calculation()
    assert latest is not None, "No calculation found in history"
    assert latest.num1 == Decimal('20') and latest.num2 == Decimal('3'), "Not correct"
