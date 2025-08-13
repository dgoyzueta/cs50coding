from plates import is_valid

def test_is_valid():
    assert is_valid("123456") == False
    assert is_valid("A1AAAA") == False
    assert is_valid("CSSSS90") == False
    assert is_valid("AAA22A") == False
    assert is_valid("0AAAAA") == False
    assert is_valid("A A.50") == False
    assert is_valid("CS50") == True
    assert is_valid("00CS50") == False
    assert is_valid("A11111") == False
    assert is_valid("A") == False
    assert is_valid("") == False
    assert is_valid("CS050") == False
    assert is_valid("AAA222") == True
    assert is_valid("*.)(&@") == False
    assert is_valid("AAAAAA") == True
    assert is_valid("123AAA") == False
    assert is_valid("Daniel") == True
    assert is_valid("AA****") == False



