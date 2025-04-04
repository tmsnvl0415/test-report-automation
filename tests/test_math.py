# tests/test_math.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_subtract_zero():
    assert subtract(5, 0) == 5

def test_subtract_result_negative():
    assert subtract(3, 5) == -2
