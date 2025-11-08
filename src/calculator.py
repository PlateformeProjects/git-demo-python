

def add(a: float, b: float) -> float:
    """Additionne deux nombres."""
    """Additionne deux nombres."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Soustrait b de a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiplie deux nombres."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divise a par b.
    
    Raises:
        ValueError: Si b est égal à 0.
    """
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b