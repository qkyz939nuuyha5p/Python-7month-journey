#mini project on Read a File and Count Words
with open("user_data.txt", "r") as f:
    text = f.read()
    print("Word Count:", len(text.split()))
