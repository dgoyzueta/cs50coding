from bank import value

def test_value():
    assert value("Daniel, Hello!") == 100
    assert value("Hello, Daniel!") == 0
    assert value("Hi, Daniel") == 20
    assert value("hello Sir") == 0
    assert value("hi sir") == 20
    assert value("Should I say Hello or Hi?")
