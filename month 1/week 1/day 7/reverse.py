#mini project of  Reverse a String using for loop
text = input("Enter text: ")
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print("Reversed:", reversed_text)
