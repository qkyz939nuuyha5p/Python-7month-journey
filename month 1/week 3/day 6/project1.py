#mini project on Basic Calculator (Using Functions)
def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b if b != 0 else "Error"

print("choose the operation +,-,*,/")
op = input("Enter the operator:")
x = float(input("Enter the value of a:"))
y = float(input("Enter the value of b:"))

if op == "+":
    print( "Result:",add(x,y))
elif op == "-":
    print( "Result:",sub(x,y))
elif op == "*":
    print( "Result:",mul(x,y))
elif op == "/":
    print( "Result:",div(x,y))