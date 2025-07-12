#day 4 learn if,else,elif,nested if....
a = 20
b = 30

if a > b:
    print("a is greater than b")
    if a > 10:#this is known as nested if. if we have if statement inside the if it known as nested if.
        print("a is greater than ten")
    else:
        print("a is not greater than ten")
elif a == b:
    print("a and b are equal")
else:
    print("b is greater than a")