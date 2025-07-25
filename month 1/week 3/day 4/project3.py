# mini project on Inverted Half Pyramid with Numbers
def inverted_half_pyramid(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

inverted_half_pyramid(5)
