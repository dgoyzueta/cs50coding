import pytest
from working import convert

def test_valid_cases():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12:30 PM to 1:00 AM") == "12:30 to 01:00"

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("cat")
        convert("13:00 PM - 5:00 PM")

def test_invalid_time():
    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM")
        convert("8:60 AM to 5:00 PM")
