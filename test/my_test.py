from app.calculations import BankAccount, add, divide, multiply, subtract
import pytest


@pytest.mark.parametrize(
    "num1, num2, expected", [(5, 3, 8), (4, 3, 7), (5, 6, 11), (500, 30, 530)]
)
def test_add(
    num1, num2, expected
):  # fundtions should be named test* and classes as Test*
    print("testing add function")  # to print this line use 'pytest -s' command
    # assert add(5, 3) == 8
    # assert add(4, 3) == 7
    # assert add(5, 6) == 11
    # assert add(500, 30) == 530
    assert add(num1, num2) == expected


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


def test_bank_set_initial_amount():
    bank_account = BankAccount(50)
    assert bank_account.get_balance() == 50


def test_bank_default_amount():
    bank_account = BankAccount()
    assert bank_account.get_balance() == 0


def test_bank_withdraw():
    account = BankAccount(100)
    account.withdraw(50)
    assert account.get_balance() == 50


def test_bank_deposit():
    account = BankAccount(100)
    account.deposit(50)
    assert account.get_balance() == 150


def test_bank_collect_interest():
    account = BankAccount(100)
    account.collect_interest()
    assert round(account.get_balance()) == 110
