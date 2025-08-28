import pytest
from bank import Account

def test_initial_balance():
    acc = Account("123", 100)
    assert acc.get_balance() == 100

def test_deposit():
    acc = Account("123", 50)
    acc.deposit(100)
    assert acc.get_balance() == 150

def test_deposit_invalid():
    acc = Account("123")
    with pytest.raises(ValueError):
        acc.deposit(0)

def test_withdraw():
    acc = Account("123", 200)
    acc.withdraw(50)
    assert acc.get_balance() == 150

def test_withdraw_insufficient():
    acc = Account("123", 50)
    with pytest.raises(ValueError):
        acc.withdraw(100)

def test_get_balance():
    acc = Account("123", 500)
    assert acc.get_balance() == 500
