#mini project on  Student Manager using oop
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll}")

# Testing the class
s1 = Student("Parikshan", 23)
s1.display_info()
