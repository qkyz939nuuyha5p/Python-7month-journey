# mini project on Vehicle → Car
class Vehicle:
    def start(self):
        print("🚗 Vehicle is starting...")

class Car(Vehicle):
    def start(self):
        super().start()
        print("🔑 Car engine started!")

print("\n===== Vehicle → Car =====")
c1 = Car()
c1.start()
