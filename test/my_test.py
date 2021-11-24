from app.calculations import BankAccount, add, divide, multiply, subtract
import pytest


@pytest.fixture  # to avoid code repititions
def zero_bank_account():
    return BankAccount()


@pytest.fixture
def bank_account():
    return BankAccount(50)


@pytest.mark.parametrize(
    "num1, num2, expected", [(5, 3, 8), (4, 3, 7), (5, 6, 11), (500, 30, 530)]
)
def test_add(
    num1, num2, expected
):  # fundtions should be named test* and classes as Test*
    # print("testing add function")  # to print this line use 'pytest -s' command
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


def test_bank_set_initial_amount(bank_account):
    assert bank_account.get_balance() == 50


def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.get_balance() == 0


def test_bank_withdraw(bank_account):
    bank_account.withdraw(50)
    assert bank_account.get_balance() == 0


def test_bank_deposit(bank_account):
    bank_account.deposit(50)
    assert bank_account.get_balance() == 100


def test_bank_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.get_balance()) == 55


@pytest.mark.parametrize(
    "deposit, withdraw, balance", [(200, 100, 100), (300, 150, 150), (500, 50, 450)]
)
def test_bank_transaction(zero_bank_account: BankAccount, deposit, withdraw, balance):
    zero_bank_account.deposit(200)
    zero_bank_account.withdraw(100)
    assert zero_bank_account.get_balance() == 100


def test_insufficient_funds(zero_bank_account):
    with pytest.raises(Exception):  # expects an exception to be raised
        zero_bank_account.withdraw(500)
