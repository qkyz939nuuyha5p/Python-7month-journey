#mini project of login system with limited attemps using while loop
phone = "9867948018"
password = "parikshan123"
tries = 0

while tries < 3:
    phone_input = input("Phone number: ")
    pass_input = input("Password: ")
    
    if phone_input == phone and pass_input == password:
        print("Login Successful!")
        break
    else:
        print("Wrong Password or phone number!")
        tries += 1
else:
    print("Too many attempts. Access denied")