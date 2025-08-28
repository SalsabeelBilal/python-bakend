
import pytest
from calculator import add, divide, Calculator

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):  
        divide(5, 0)

def test_calculator_store_and_recall():
    calc = Calculator()
    calc.store(42)
    assert calc.recall() == 42
