import pytest
from numb3rs import validate

def test_numbers_in_range():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.255") == True
    assert validate("0.0.0.0") == True

def test_numbers_out_of_range():
    assert validate("0.0.0.1000") == False
    assert validate("256.0.0.0") == False
    assert validate("0.256.256.256") == False

def test_other_cases():
    assert validate("a.1.1.1") == False
    assert validate("cat") == False
    assert validate("1.1.1.1.1") == False
