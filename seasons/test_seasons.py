import pytest
from seasons import life_in_minutes, validate_date_format
from datetime import date

def test_life_in_minutes():
    assert life_in_minutes("2024-07-10") == "Four hundred forty-six thousand, four hundred minutes"

def test_invalid_dates():
    with pytest.raises(ValueError):
        life_in_minutes("cat")
        life_in_minutes("February 6th, 1998")
        life_in_minutes("2010-11-31")
