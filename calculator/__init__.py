from decimal import Decimal
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        calculation = Calculation(a, b, add)
        Calculations.add_calculation(calculation)
        return calculation.execute_calculation()

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        calculation = Calculation(a, b, subtract)
        Calculations.add_calculation(calculation)
        return calculation.execute_calculation()

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        calculation = Calculation(a, b, multiply)
        Calculations.add_calculation(calculation)
        return calculation.execute_calculation()

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        calculation = Calculation(a, b, divide)
        Calculations.add_calculation(calculation)
        return calculation.execute_calculation()