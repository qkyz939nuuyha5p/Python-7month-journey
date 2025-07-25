# mini project on Function to Print a Right-Angled Triangle
def right_triangle(n):
    for i in range(1, n + 1):
        print('*' * i)

rows = int(input("Enter number of rows: "))
right_triangle(rows)
