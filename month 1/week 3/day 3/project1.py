# mini project on Note Saver App (Text Editor in Terminal)
filename = "note.txt"
note = input("Note:")
with open(filename,"a") as f:
    f.write(note + "\n")
print("✅ Note saved to file.")