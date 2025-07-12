#in this file we write the mini project like age group classifier
name = input("Enter the name:")
age = int(input("Enter the age:"))
if age < 0:
    print("Age cannot be negative")
elif age < 13:
    print("He is child.")
elif age < 20:
    print("he is teenager")
elif age >= 20:
    print("he is adult")
else:
    print("Invalid number!")