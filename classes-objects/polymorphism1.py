# Create a class Animal with sound() that prints "Animal makes sound"
# Create another class dog which inherits from animal and overrides sound() that will print "Dog barks"
# Create another class bird which inherits from animal and overrides sound() that will print "Brids sing"

class animal:
    def sound(self):
        print("Animal makes sound")
class dog(animal):
    def sound(self):
        print("Dog barks")
class bird(animal):
    def sound(self):
        print("Birds sing")
    
Animal = animal()
Dog = dog()
Bird = bird()

Animal.sound()
Dog.sound()
Bird.sound()