def add(num1: int, num2: int):
    return num1 + num2


def subtract(num1: int, num2: int):
    return num1 - num2


def multiply(num1: int, num2: int):
    return num1 * num2


def divide(num1: int, num2: int):
    return num1 / num2


class BankAccount:
    def __init__(self, starting_balance=0):
        self._balance = starting_balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def collect_interest(self):
        self._balance *= 1.1

    def get_balance(self):
        return self._balance