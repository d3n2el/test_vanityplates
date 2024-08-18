from plates import is_valid
def test_num0():
    assert is_valid("CS50") == True
    assert is_valid("01dan") == False
    assert is_valid("CS05") == False

def test_num_placement():
    assert is_valid("CS50") == True
    assert is_valid("da10de") == False
    assert is_valid("dr69w") == False


def test_length():
    assert is_valid("ab") == True
    assert is_valid("a") == False
    assert is_valid("abcdfeffgg") == False
    assert is_valid("qwerty") == True

def test_firstletters():
    assert is_valid("da4") == True
    assert is_valid("#@djf") == False
    assert is_valid("$money") == False
    assert is_valid("9123") == False


def test_punctuation():
    assert is_valid("ehr!") == False
    assert is_valid("asw,50") == False
    assert is_valid(".asd") == False
    assert is_valid("aw.34,4") == False



