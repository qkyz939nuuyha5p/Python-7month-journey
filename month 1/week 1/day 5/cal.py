#mini project of calulater using match case 
a = float(input("a="))
b = float(input("b="))
cal = input("Enter the Operator:")
match cal:
    case '+':
        print("sum:",a+b)
    case '-':
        print("sub:",a-b)
    case '/':
        print("divide:",a/b)
    case '*':
        print("multiple:",a*b)
    case _:
        print("Invalid!")