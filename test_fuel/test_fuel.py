import pytest
from fuel import gauge, convert

def test_convert():
    assert convert("999/1000") == 100
    assert convert("25/100") == 25
    assert convert("28/29") == 97
    assert convert("1/13") == 8
    assert convert("49/1000") == 5

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")

def test_x_greater_than_y():
    with pytest.raises(ValueError):
        convert("2/1")

def test_different_from_numbers():
    with pytest.raises(ValueError):
        convert("cat")
        convert("cat/cat")

def test_gauge():
    assert gauge(10) == "10%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"

