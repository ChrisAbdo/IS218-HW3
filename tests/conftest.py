"""Pytest configuration file for the calculator tests."""
from decimal import Decimal
import pytest

@pytest.fixture
def input_values():
    """Fixture to provide input values for calculator tests."""
    return {
        'a': Decimal(5),
        'b': Decimal(2)
    }
