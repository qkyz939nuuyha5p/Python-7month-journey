# see grade system using match-case
gpa = float(input("Enter GPA (0.0 to 4.0): "))

match gpa:
    case _ if gpa > 4.0 or gpa < 0:
        print("Invalid GPA")
    case _ if gpa >= 3.6:
        print("Grade: A+")
    case _ if gpa >= 3.2:
        print("Grade: A")
    case _ if gpa >= 2.8:
        print("Grade: B+")
    case _ if gpa >= 2.4:
        print("Grade: B")
    case _ if gpa >= 2.0:
        print("Grade: C+")
    case _ if gpa >= 1.6:
        print("Grade: C")
    case _ if gpa > 0:
        print("Grade: D")
    case _:
        print("Grade: Fail")
