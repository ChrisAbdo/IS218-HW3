from typing import List
from calculator.calculation import Calculation

class Calculations:
    # empty list to store calculation objects
    calculation_history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        cls.calculation_history.append(calculation)

    @classmethod
    def history(cls) -> List[Calculation]:
        return cls.calculation_history

    @classmethod
    def clear_history(cls):
        cls.calculation_history.clear()

    @classmethod
    def last_calculation(cls) -> Calculation:
        return cls.calculation_history[-1] if cls.calculation_history else None