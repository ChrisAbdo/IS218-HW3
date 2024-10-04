"""
This module contains tests for the calculator module.
"""

from decimal import Decimal
import pytest
from calculator import Calculator
from calculator.calculations import Calculations

def test_addition():
    """
    Test that the add method returns the expected result
    """
    result = Calculator.add(Decimal(2), Decimal(3))
    assert result == Decimal(5)

def test_subtraction():
    """
    Test that the subtract method returns the expected result
    """
    result = Calculator.subtract(Decimal(9), Decimal(3))
    assert result == Decimal(6)

def test_multiplication():
    """
    Test that the multiply method returns the expected result
    """
    result = Calculator.multiply(Decimal(2), Decimal(4))
    assert result == Decimal(8)

def test_division():
    """
    Test that the divide method returns the expected result
    """
    result = Calculator.divide(Decimal(6), Decimal(2))
    assert result == Decimal(3)

def test_divide_by_zero():
    """
    Test that dividing by zero raises a ZeroDivisionError
    """
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(Decimal(5), Decimal(0))

def test_history():
    """
    Test that the history contains the expected number of calculations
    """
    Calculations.clear_history()
    Calculator.add(Decimal(1), Decimal(1))
    Calculator.subtract(Decimal(5), Decimal(3))
    Calculator.multiply(Decimal(2), Decimal(4))
    Calculator.divide(Decimal(8), Decimal(2))
    assert len(Calculations.history()) == 4

def test_last_calculation():
    """
    Test that the last calculation is returned
    """
    Calculations.clear_history()
    Calculator.add(Decimal(1), Decimal(2))
    last_calc = Calculations.last_calculation()
    assert last_calc.execute_calculation() == Decimal(3)

def test_clear_history():
    """
    Test that the history is cleared
    """
    Calculations.clear_history()
    assert len(Calculations.history()) == 0
