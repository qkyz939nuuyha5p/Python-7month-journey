#mini project on Append Notes to a Log File
note = input("Enter your daily note: ")

with open("log.txt", "a") as f:
    f.write(note + "\n")
print("Note saved!")
