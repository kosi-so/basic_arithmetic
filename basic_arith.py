
def add (x, y):
    """Add Function"""
    return x + y


def subtract (x, y):
    """Subtract Function"""
    return x - y


def multiply (x, y):
    """Multiply Function"""
    return x * y


def divide (x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError ("Real numbers are not divisible by zero")
    return x / y


def floor (x, y):
    """Floor Fuction"""
    return x // y


def power (x, y):
    """Divide Function"""
    return x ** y
