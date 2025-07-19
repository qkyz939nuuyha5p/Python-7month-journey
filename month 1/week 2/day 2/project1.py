#mini project of Write User Info to File
name = input("Enter your name: ")
age = input("Enter your age: ")

with open("user_data.txt", "w") as f:
    f.write(f"Name: {name}\nAge: {age}")

f = open("user_data.txt")
print(f.read())
