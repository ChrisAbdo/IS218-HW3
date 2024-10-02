from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract

@pytest.fixture
def calculations():
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))

def test_add_calculation():
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    Calculations.add_calculation(calc)
    assert Calculations.last_calculation() == calc, "Failed to add the calculation to the history"

def test_history():
    history = Calculations.history()
    assert len(history) == 2, "History does not contain the expected number of calculations"

def test_clear_history():
    Calculations.clear_history()
    assert len(Calculations.history()) == 0, "History was not cleared"

def test_last_calculation():
    latest = Calculations.last_calculation()
    assert latest.a == Decimal('20') and latest.b == Decimal('3'), "Did not get the correct latest calculation"