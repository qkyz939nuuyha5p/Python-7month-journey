#  Project on ATM Simulator with Loop & Condition Logic
balance = 1000  # Starting balance

while True:
    print("\n==== ATM MENU ====")
    print("1. 💰 Deposit")
    print("2. 🏧 Withdraw")
    print("3. 📄 Check Balance")
    print("4. ❌ Exit")

    choice = input("Select an option (1-4): ")

    if choice == "1":
        amt = float(input("Enter amount to deposit: Rs. "))
        if amt > 0:
            balance += amt
            print(f"✅ Deposited Rs. {amt}. New balance: Rs. {balance}")
        else:
            print("❌ Invalid deposit amount.")
    
    elif choice == "2":
        amt = float(input("Enter amount to withdraw: Rs. "))
        if 0 < amt <= balance:
            balance -= amt
            print(f"✅ Withdrew Rs. {amt}. New balance: Rs. {balance}")
        else:
            print("❌ Insufficient balance or invalid amount.")
    
    elif choice == "3":
        print(f"📄 Your current balance is: Rs. {balance}")
    
    elif choice == "4":
        print("👋 Thank you for using the ATM. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please try again.")
