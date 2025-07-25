# mini project on Write a List of Tasks to a File
tasks  = ["Complete Python","Push Code to Github","Finish the College Assingment"]
with open("tasks.txt","w") as f:
    for task in tasks:
        f.write(task + "\n")
print("✅ Tasks saved to tasks.txt")