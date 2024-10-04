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
    (Decimal('-3'), Decimal('7'), add, Decimal('4')),
    (Decimal('100'), Decimal('99'), subtract, Decimal('1')),
    (Decimal('0.1'), Decimal('0.1'), multiply, Decimal('0.01')),
    (Decimal('1'), Decimal('3'), divide, Decimal('0.3333333333333333333333333333')),
    (Decimal('2.5'), Decimal('2.5'), add, Decimal('5.0')),
    (Decimal('10000'), Decimal('0.0001'), multiply, Decimal('1')),
    (Decimal('-5'), Decimal('-5'), subtract, Decimal('0')),
    (Decimal('2'), Decimal('2'), multiply, Decimal('4')),
    (Decimal('1'), Decimal('1'), divide, Decimal('1')),
    (Decimal('0'), Decimal('5'), add, Decimal('5')),
    (Decimal('0'), Decimal('0'), add, Decimal('0')),
    (Decimal('-10'), Decimal('5'), multiply, Decimal('-50')),
    (Decimal('123.456'), Decimal('654.321'), add, Decimal('777.777')),
    (Decimal('987.654'), Decimal('123.456'), subtract, Decimal('864.198')),
    (Decimal('3.14159'), Decimal('2.71828'), multiply, Decimal('8.5397212652')),
    (Decimal('1000'), Decimal('250'), divide, Decimal('4')),
    (Decimal('-50'), Decimal('25'), add, Decimal('-25')),
    (Decimal('0.333'), Decimal('0.667'), add, Decimal('1.0')),
    (Decimal('100'), Decimal('0.1'), multiply, Decimal('10')),
    (Decimal('1.234'), Decimal('0.4321'), subtract, Decimal('0.8019')),
    (Decimal('9'), Decimal('3'), divide, Decimal('3')),
    (Decimal('0.5'), Decimal('0.5'), multiply, Decimal('0.25')),
    (Decimal('-100'), Decimal('-200'), add, Decimal('-300')),
    (Decimal('50'), Decimal('50'), subtract, Decimal('0')),
    (Decimal('0.01'), Decimal('0.01'), multiply, Decimal('0.0001')),
    (Decimal('10'), Decimal('0.1'), divide, Decimal('100')),
    (Decimal('12345'), Decimal('54321'), add, Decimal('66666')),
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
