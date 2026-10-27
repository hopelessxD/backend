class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: Rs.{amount}, Balance: Rs.{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
            return
        self.balance -= amount
        self.transactions.append(f"Withdrew: Rs.{amount}, Balance: Rs.{self.balance}")

    def __repr__(self):
        return f"Account(name='{self.name}', balance={self.balance})"

    def get_history(self):
        return self.transactions


if __name__ == "__main__":
    my_account = Account("Bob", 50)
    my_account.deposit(25)
    my_account.withdraw(100)  # Insufficient
    my_account.withdraw(10)
    print(my_account.get_history())
    # Expected Output: ['Deposited: 25', 'Withdrew: 10']
