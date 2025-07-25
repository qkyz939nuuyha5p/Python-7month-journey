#mini project on read and display notes.
filename = "note.txt"
with open(filename,"r") as f:
    content = f.read()
print("\n📝 All Notes:\n")
print(content)