#Create a Simple Calculator that takes two numbers and prints results using all arithmetic operators.
# Take two numbers as input
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Calculate and print results
print("\nResults:")
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)  # Rounds down to nearest integer
print("Modulus (Remainder):", a % b)  # Remainder after division
print("Exponent (Power):", a ** b)  # a raised to the power of b
print("Average:", (a + b) / 2)  # Fixed: Uses (a + b) instead of undefined 'sum'