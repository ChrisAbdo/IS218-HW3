"""Tests for the Calculator class."""
from calculator import Calculator

def test_addition():
    """Test that addition function works correctly."""
    assert Calculator.add(2, 2) == 4

def test_subtraction():
    """Test that subtraction function works correctly."""
    assert Calculator.subtract(2, 2) == 0

def test_multiply():
    """Test that multiplication function works correctly."""
    assert Calculator.multiply(2, 2) == 4

def test_divide():
    """Test that division function works correctly."""
    assert Calculator.divide(2, 2) == 1
