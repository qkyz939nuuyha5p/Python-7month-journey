#mini project of Multiplication Table with Function
def print_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

num = int(input("Enter a number: "))
print_table(num)
