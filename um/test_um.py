import pytest
from um import count

def test_valid_cases():
    assert count("Hello um, Doe um, Junior") == 2
    assert count("um...") == 1

def test_invalid_case():
    assert count("YUMMY") == 0
    assert count("YUM") == 0

def test_single_word():
    assert count("UM") == 1
