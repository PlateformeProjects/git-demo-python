import pytest
from src.calculator import add, subtract, multiply, divide, factorial

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2

def test_multiply():
    assert multiply(4, 2) == 8
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(6, 3) == 2
    with pytest.raises(ValueError):
        divide(5, 0)
        
def test_factorial():
    assert factorial(5) == 120       
    assert factorial(12) == 479001600       
