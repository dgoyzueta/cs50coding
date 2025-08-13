import pytest
import project

def test_validate_ticker():
    # It checks probable inputs (NASDAQ ticker) from the user.
    assert project.validate_ticker("GOOGL") == True
    assert project.validate_ticker("GOOLG") == False
    assert project.validate_ticker("12345") == False
    assert project.validate_ticker("CAT12") == False

def test_get_closing_price():
    # It only tests for valid tickers because the input of a valid ticker is controlled in the program.
    assert isinstance(project.get_closing_price("GOOGL"), float) == True
    assert isinstance(project.get_closing_price("MSFT"), float) == True

def test_get_average_price_year():
    # It only tests for valid tickers because the input of a valid ticker is controlled in the program.
    assert isinstance(project.get_average_price_year("GOOGL"), float) == True
    assert isinstance(project.get_average_price_year("MSFT"), float) == True
