# mini project on Matrix Creator (Nested List Input)

rows = input("Enter number of rows:")
columns = input("Enter number of columns:")

matrix = []
for i in rows:
    rows = []
    for j in columns:
        val = int(input(f"Enter value for ({i},{j}): "))
        val.append(val)
    matrix.append(rows)

print("\nMatrix:")
for r in matrix:
    print(r)