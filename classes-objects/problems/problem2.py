# Problem - 2
# -----------
# Create a base class Vehicle with a method start() that prints "Vehicle started".
# Create a derived class called Car that inherits from Vehicle and overrides the start() to print "Car started".


class Vehicle:
    def start(self):
        print("Vehicle started")
class Car(Vehicle):
    def start(self):
        print("Car started")

vehicle = Vehicle()
car = Car()

vehicle.start()
car.start()