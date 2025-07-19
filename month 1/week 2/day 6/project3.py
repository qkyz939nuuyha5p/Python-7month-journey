# mini project on Shape Area Calculator
class Shape:
    def area(self):
        print("Calculating area...")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"🟠 Circle Area: {3.14 * self.radius ** 2}")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f"🟥 Rectangle Area: {self.length * self.width}")

shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    shape.area()
