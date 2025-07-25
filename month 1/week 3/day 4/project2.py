# mini project on Number Pyramid using Function
def number_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

number_pyramid(5)
