#mini project on bank 
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def display(self):
        print(f"👔 Manager {self.name} earns Rs.{self.salary}")

print("===== Employee → Manager =====")
m1 = Manager("Parikshan", 50000)
m1.display()