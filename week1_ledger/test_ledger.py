from ledger import Account
def test_initial_balance():
    acc = Account('Ram',1000)
    assert acc.name == 'Ram'
    assert acc.balance == 1000

def test_deposits():
    acc = Account('Bob',50)
    acc.deposit(100)
    assert acc.balance == 150

def test_insufficient_funds():
    acc = Account('hari',10)
    acc.withdraw(500)
    assert acc.balance == 10

def test_withdraw():
    acc = Account('gyan',400)
    acc.withdraw(100)
    assert acc.balance == 300


    