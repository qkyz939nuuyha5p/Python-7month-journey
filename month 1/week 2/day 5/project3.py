# mini project on Animal → Dog → Puppy (Multi-Level Inheritance)
class Animal:
    def sound(self):
        print("🐾 Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("🐶 Dog barks")

class Puppy(Dog):
    def cute(self):
        print("🐕 Puppy is cute!")

print("\n===== Animal → Dog → Puppy =====")
p1 = Puppy()
p1.sound()
p1.cute()