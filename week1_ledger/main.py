from ledger import Account
from transaction import Transaction
name = input("Enter Your Name: ")
user_account = Account(name)
i = 1
while(i != 0):
    print("\n1) Deposit\n2) Withdraw\n3) History\n4) Quit")
    req = input("Select Required Service: ")
    match req:
        case '1':
            print(f"Current Balance: {user_account.balance}")
            amt = input("Enter amount: ")
            user_account.deposit(int(amt))
            print(f"New Balance: {user_account.balance}")
            
        case '2':
            print(f"Current Balance: {user_account.balance}")
            amt = input("Enter amount: ")
            user_account.withdraw(int(amt))
            print(f"New Balance: {user_account.balance}")
        case '3':
            print(user_account.get_history())
        case '4':
            i = 0
            print(f"Exited with balance: {user_account.balance}")
        case _:
            print("Invalid Input")
        
t = Transaction(50,"deposit")
print(t)