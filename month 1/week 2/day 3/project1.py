#mini project on safe calculator:
def safe_calculator():
    print("Welcome to the Safe Calculator!")
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Choose operation (+, -, *, /): ")
            
            if operation == '+':
                print(f"Result: {num1 + num2}")
            elif operation == '-':
                print(f"Result: {num1 - num2}")
            elif operation == '*':
                print(f"Result: {num1 * num2}")
            elif operation == '/':
                try:
                    print(f"Result: {num1 / num2}")
                except ZeroDivisionError:
                    print("Error: Division by zero is not allowed!")
            else:
                print("Invalid operation selected!")
                
        except ValueError:
            print("Error: Please enter valid numbers!")
        
        cont = input("Continue? (y/n): ").lower()
        if cont != 'y':
            break

safe_calculator()