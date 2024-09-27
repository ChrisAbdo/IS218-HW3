from decimal import Decimal


# type hinting
def add(a: Decimal, b: Decimal) -> Decimal:
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    # division by zero exception
    if b == 0:
        raise Exception("Cannot divide by zero!")
    return a / b