class Animal:
    def sound(self):
        print("Animal sound")

class Cat(Animal):
    def sound(self):
        print("Meow")

c = Cat()
c.sound()

class Dog(Animal):
    def sound(self):
        print("Bark")

d = Dog()
d.sound()
