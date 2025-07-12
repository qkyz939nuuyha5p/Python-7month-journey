#The match statement is used to perform different actions based on different conditions.
month = int(input("enter the month"))
text = int(input("Enter the case number"))
match text:#by using match keyword we can use match case
    case 1:
        print("hello")
    case 2:
        print("hi")
    case 9 | 8 | 3 | 4 | 5:#this is know as combine value. which is seperated by |
        print("bye")
    case 10 | 11 | 12 | 13 if month == 10:#You can add if statements in the case evaluation as an extra condition-check:
        print("today is holiday!")
    case _:#we use underscore for defalult value 
        print("default")