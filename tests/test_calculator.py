from decimal import Decimal
import pytest
from calculator import Calculator
from calculator.calculation import Calculation

def test_addition():
    result = Calculator.add(Decimal(2), Decimal(3))
    assert result == Decimal(5)

def test_subtraction():
    result = Calculator.subtract(Decimal(5), Decimal(3))
    assert result == Decimal(2)

def test_multiplication():
    result = Calculator.multiply(Decimal(2), Decimal(3))
    assert result == Decimal(6)

def test_division():
    result = Calculator.divide(Decimal(6), Decimal(2))
    assert result == Decimal(3)

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(Decimal(5), Decimal(0))

def test_history():
    Calculation.clear_history()
    Calculator.add(Decimal(1), Decimal(1))
    Calculator.subtract(Decimal(5), Decimal(3))
    Calculator.multiply(Decimal(2), Decimal(4))
    Calculator.divide(Decimal(8), Decimal(2))
    assert len(Calculation.history()) == 4

def test_last_calculation():
    Calculation.clear_history()
    Calculator.add(Decimal(1), Decimal(2))
    last_calc = Calculation.last_calculation()
    assert last_calc.result == Decimal(3)

def test_clear_history():
    Calculation.clear_history()
    assert len(Calculation.get_history()) == 0
