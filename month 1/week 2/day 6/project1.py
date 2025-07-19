# mini project on Payment Method Simulation
class PaymentMethod:
    def process_payment(self, amount):
        print(f"Processing Rs.{amount}...")

class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        print(f"💳 Paid Rs.{amount} using Credit Card.")

class PayPal(PaymentMethod):
    def process_payment(self, amount):
        print(f"📧 Paid Rs.{amount} through PayPal.")

class BankTransfer(PaymentMethod):
    def process_payment(self, amount):
        print(f"🏦 Transferred Rs.{amount} via Bank Transfer.")

methods = [CreditCard(), PayPal(), BankTransfer()]
for method in methods:
    method.process_payment(1500)
