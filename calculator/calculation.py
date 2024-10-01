from decimal import Decimal
from typing import Callable, List

class Calculation:
    history: List['Calculation'] = []

    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        self.operation = operation  # Store the operation function
        self.result = self.get_result()
        self.add_calculation(self)

    def get_result(self) -> Decimal:
        return self.operation(self.a, self.b)

    @classmethod
    def add_calculation(cls, calculation: 'Calculation'):
        cls.history.append(calculation)

    @classmethod
    def get_last_calculation(cls) -> 'Calculation':
        return cls.history[-1] if cls.history else None

    @classmethod
    def clear_history(cls):
        cls.history.clear()

    @classmethod
    def get_history(cls) -> List['Calculation']:
        return cls.history