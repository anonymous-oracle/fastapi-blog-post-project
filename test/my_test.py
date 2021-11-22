from app.calculations import add, divide, multiply, subtract


def test_add():  # fundtions should be named test* and classes as Test*
    print("testing add function")  # to print this line use 'pytest -s' command
    assert add(5, 3) == 8
    assert add(4, 3) == 7
    assert add(5, 6) == 11
    assert add(500, 30) == 530


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(5, 30) == -25
    assert subtract(55, 31) == 24
    assert subtract(1, 1) == 0


def test_multiply():
    assert multiply(5, 5) == 25
    assert multiply(6, 6) == 36
    assert multiply(7, 7) == 49


def test_divide():
    assert divide(1, 1) == 1
    assert divide(9, 3) == 3
    assert divide(5, 2) == 2.5
