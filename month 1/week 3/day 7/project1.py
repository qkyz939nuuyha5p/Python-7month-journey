# mini project on  Bank Account Class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"💰 Deposited {amount}, Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"💸 Withdrawn {amount}, Balance: {self.balance}")
        else:
            print("❌ Insufficient funds")

acc = BankAccount("Parikshan")
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(400)
