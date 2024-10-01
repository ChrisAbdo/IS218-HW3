"""Unit tests for the Calculator class."""
from decimal import Decimal
import pytest
from calculator import Calculator
from calculator.calculation import Calculation

def test_addition():
    """Test the addition method of the Calculator class."""
    result = Calculator.add(Decimal(2), Decimal(3))
    assert result == Decimal(5)

def test_subtraction():
    """Test the subtraction method of the Calculator class."""
    result = Calculator.subtract(Decimal(5), Decimal(3))
    assert result == Decimal(2)

def test_multiplication():
    """Test the multiplication method of the Calculator class."""
    result = Calculator.multiply(Decimal(2), Decimal(3))
    assert result == Decimal(6)

def test_division():
    """Test the division method of the Calculator class."""
    result = Calculator.divide(Decimal(6), Decimal(2))
    assert result == Decimal(3)

def test_divide_by_zero():
    """Test division by zero raises a ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(Decimal(5), Decimal(0))

def test_calculation_history():
    """Test the calculation history functionality."""
    Calculation.clear_history()
    Calculator.add(Decimal(1), Decimal(1))
    Calculator.subtract(Decimal(5), Decimal(3))
    Calculator.multiply(Decimal(2), Decimal(4))
    Calculator.divide(Decimal(8), Decimal(2))
    assert len(Calculation.get_history()) == 4

def test_get_last_calculation():
    """Test retrieving the last calculation from history."""
    Calculation.clear_history()
    Calculator.add(Decimal(1), Decimal(2))
    last_calc = Calculation.get_last_calculation()
    assert last_calc.result == Decimal(3)

def test_clear_history():
    """Test clearing the calculation history."""
    Calculation.clear_history()
    assert len(Calculation.get_history()) == 0
