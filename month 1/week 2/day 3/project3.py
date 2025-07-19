#mini project on  Robust Login System with Exception Handling.
class InvalidCredentialsError(Exception):
    pass

def login_system():
    print("\nSecure Login System")
    stored_username = "admin"
    stored_password = "password123"
    
    while True:
        try:
            username = input("Enter username: ")
            if not username.isalpha():
                raise TypeError("Username must contain only letters")
                
            password = input("Enter password: ")
            if len(password) < 8:
                raise ValueError("Password must be at least 8 characters")
                
            if username == stored_username and password == stored_password:
                print("Login successful!")
                break
            else:
                raise InvalidCredentialsError("Invalid username or password")
                
        except TypeError as te:
            print(f"Input Error: {str(te)}")
        except ValueError as ve:
            print(f"Input Error: {str(ve)}")
        except InvalidCredentialsError as ice:
            print(f"Authentication Error: {str(ice)}")
        except Exception as e:
            print(f"Unexpected Error: {str(e)}")
            
        retry = input("Try again? (y/n): ").lower()
        if retry != 'y':
            print("Goodbye!")
            break

login_system()