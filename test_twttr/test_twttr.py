from twttr import shorten

def test_shorten():
    assert shorten("Daniel") == "Dnl"
    assert shorten("") == ""
    assert shorten("ABC") == "BC"
    assert shorten("1A0") == "10"
    assert shorten("1.A") == "1."

