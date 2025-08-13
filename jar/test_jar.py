from jar import Jar
import pytest

def test_init():
    jar = Jar(20)
    assert jar.capacity == 20
    assert jar.balance == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.capacity == 10
    assert jar.balance == 5

def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)
    jar.withdraw(5)
    assert jar.capacity == 5
    assert jar.balance == 0

def test_error_01():
    with pytest.raises(ValueError):
        jar = Jar(-5)

def test_error_02():
    with pytest.raises(ValueError):
        jar = Jar(5)
        jar.deposit(5)
        jar.withdraw(6)

def test_error_03():
    with pytest.raises(ValueError):
        jar = Jar(5)
        jar.deposit(100)
