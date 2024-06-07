from valid import validate

def test_format():
    assert validate('1.2.3.4') == True
    assert validate('1.2.3') == False
    assert validate('1.2') == False


def test_range():
    assert validate('255.255.255.255') == True
    assert validate('1000.255.255.255') == False
    assert validate('255.1000.255.255') == False
    assert validate('255.255.1000.255') == False
    assert validate('255.255.255.1000') == False


def test_alpha():
    assert validate('cat.54.dog.255') == False
    assert validate('lion') == False
