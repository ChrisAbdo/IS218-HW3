"""
Calculation class
"""

from typing import Callable
from decimal import Decimal

class Calculation:
    """
    A class to represent a calculation.
    """
    def __init__(self, num1: Decimal, num2: Decimal, op: Callable[[Decimal, Decimal], Decimal]):
        self.num1 = num1
        self.num2 = num2
        self.op = op
        self.result = None
    
    """
    Create a Calculation object.
    """
    @staticmethod
    def create_calculation(num1: Decimal, num2: Decimal, op: Callable[[Decimal, Decimal], Decimal]):
        return Calculation(num1, num2, op)
    
    """
    Execute the calculation and return the result.
    """
    def execute_calculation(self) -> Decimal:
        if self.result is None:
            self.result = self.op(self.num1, self.num2)
        return self.result