from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide


def test_op_add():
    calculation = Calculation(Decimal('10'), Decimal('5'), add)
    assert calculation.execute_calculation() == Decimal('15'), "Add operation failed"

def test_op_subtract():
    calculation = Calculation(Decimal('10'), Decimal('5'), subtract)
    assert calculation.execute_calculation() == Decimal('5'), "Subtract operation failed"

def test_op_multiply():
    calculation = Calculation(Decimal('10'), Decimal('5'), multiply)
    assert calculation.execute_calculation() == Decimal('50'), "Multiply operation failed"

def test_op_divide():
    calculation = Calculation(Decimal('10'), Decimal('5'), divide)
    assert calculation.execute_calculation() == Decimal('2'), "Divide operation failed"

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.execute_calculation()