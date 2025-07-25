# mini project on Student Grade Calculator
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print(f"{self.name}'s Average: {self.average()}")

s1 = Student("Parikshan", [80, 90, 75])
s1.display()
