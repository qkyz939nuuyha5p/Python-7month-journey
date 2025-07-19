# mini project on Animal Sounds Simulator
class Animal:
    def make_sound(self):
        print("Animal makes sound.")

class Dog(Animal):
    def make_sound(self):
        print("🐶 Dog barks.")

class Cat(Animal):
    def make_sound(self):
        print("🐱 Cat meows.")

class Cow(Animal):
    def make_sound(self):
        print("🐄 Cow moos.")

animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.make_sound()
