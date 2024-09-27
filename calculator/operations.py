from decimal import Decimal


# type hinting for params and return value
def add(a: Decimal, b: Decimal) -> Decimal:
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    # division by zero exception
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b