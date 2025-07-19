#mini project on  Enhanced File Reader with Error Handling
def file_reader():
    print("\nFile Reader with Error Handling")
    
    while True:
        filename = input("Enter filename to read (or 'quit' to exit): ")
        if filename.lower() == 'quit':
            break
            
        try:
            with open(filename, 'r') as f:
                print("\nFile Contents:")
                print(f.read())
                
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found!")
        except PermissionError:
            print(f"Error: No permission to read '{filename}'!")
        except UnicodeDecodeError:
            print("Error: Could not decode the file (might be a binary file)")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            
file_reader()