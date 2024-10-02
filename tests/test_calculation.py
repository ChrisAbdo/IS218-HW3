"""
This module contains unit tests for the Calculation class.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("num1, num2, op, exp", [
    (Decimal('7'), Decimal('2'), add, Decimal('9')),
    (Decimal('9'), Decimal('4'), subtract, Decimal('5')),
    (Decimal('12'), Decimal('3'), multiply, Decimal('36')),
    (Decimal('18'), Decimal('6'), divide, Decimal('3')),
    (Decimal('6.5'), Decimal('0.5'), add, Decimal('7.0')),
    (Decimal('8.5'), Decimal('7.5'), subtract, Decimal('1.0')),
    (Decimal('1.5'), Decimal('2'), multiply, Decimal('3.0')),
    (Decimal('5'), Decimal('0.5'), divide, Decimal('10')),
])
def test_ops(num1, num2, op, exp):
    """
    Test the Calculation class with the add, subtract, multiply, and divide operations.
    """
    calc = Calculation(num1, num2, op)
    assert calc.execute_calculation() == exp, f"Failed {op.__name__}"

def test_divide_by_zero():
    """
    Test that dividing by zero raises a ZeroDivisionError.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        calc.execute_calculation()
