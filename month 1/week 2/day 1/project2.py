#mini project of Check Even or Odd Using Function
def is_even(num):
    return num % 2 == 0

n = int(input("Enter a number: "))
if is_even(n):
    print("Even")
else:
    print("Odd")
