#we will make grading system of see using condition statement.
name = input("Enter the name of student:")
grade = float(input("Enter the grade of student:"))
if grade <= 1.6:
    print("fail")
elif grade <= 1.6:
    print("D")
elif grade <= 2.0:
    print("C")
elif grade <= 2.4:
    print("C+")
elif grade <=2.8:
    print("B")
elif grade <=3.2:
    print("B+")
elif grade <=3.6:
    print("A")
elif grade <=4.0:
    print("A+") 
else:
    print("invalid grade!")