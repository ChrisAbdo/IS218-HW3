"""
This module contains unit tests for the Calculation class.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("num1, num2, op, exp", [
    (Decimal('10'), Decimal('5'), add, Decimal('15')),
    (Decimal('10'), Decimal('5'), subtract, Decimal('5')),
    (Decimal('10'), Decimal('5'), multiply, Decimal('50')),
    (Decimal('10'), Decimal('2'), divide, Decimal('5')),
    (Decimal('10.5'), Decimal('0.5'), add, Decimal('11.0')),
    (Decimal('10.5'), Decimal('0.5'), subtract, Decimal('10.0')),
    (Decimal('10.5'), Decimal('2'), multiply, Decimal('21.0')),
    (Decimal('10'), Decimal('0.5'), divide, Decimal('20')),
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
