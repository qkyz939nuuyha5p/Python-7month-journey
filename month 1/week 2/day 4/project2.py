#mini project on Bank Account Simulator
class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Rs.{amount}. New balance: Rs.{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew Rs.{amount}. Remaining balance: Rs.{self.balance}")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print(f"Account Balance for {self.name}: Rs.{self.balance}")

# Testing
acc1 = Account("Parikshan")
acc1.deposit(5000)
acc1.withdraw(1500)
acc1.check_balance()
