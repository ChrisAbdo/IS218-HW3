"""
This module contains tests for the operations module.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide


def test_op_add():
    """
    Test that the add operation returns the expected result
    """
    calculation = Calculation(Decimal('10'), Decimal('5'), add)
    assert calculation.execute_calculation() == Decimal('15'), "Add operation failed"

def test_op_subtract():
    """
    Test that the subtract operation returns the expected result
    """
    calculation = Calculation(Decimal('10'), Decimal('5'), subtract)
    assert calculation.execute_calculation() == Decimal('5'), "Subtract operation failed"

def test_op_multiply():
    """
    Test that the multiply operation returns the expected result
    """
    calculation = Calculation(Decimal('10'), Decimal('5'), multiply)
    assert calculation.execute_calculation() == Decimal('50'), "Multiply operation failed"

def test_op_divide():
    """
    Test that the divide operation returns the expected result
    """
    calculation = Calculation(Decimal('10'), Decimal('5'), divide)
    assert calculation.execute_calculation() == Decimal('2'), "Divide operation failed"

def test_divide_by_zero():
    """
    Test that dividing by zero raises a ZeroDivisionError
    """
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.execute_calculation()
