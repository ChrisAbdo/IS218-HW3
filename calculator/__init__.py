from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        calculation = Calculation(a, b, add)
        return calculation.result

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        calculation = Calculation(a, b, subtract)
        return calculation.result

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        calculation = Calculation(a, b, multiply)
        return calculation.result

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        calculation = Calculation(a, b, divide)
        return calculation.result