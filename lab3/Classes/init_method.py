class Person:
    def __init__(self, name):
        self.name = name

p = Person("Anna")
print(p.name)

class Car:
    def __init__(self, brand):
        self.brand = brand

c = Car("BMW")
print(c.brand)

class Student:
    def __init__(self, age):
        self.age = age

s = Student(20)
print(s.age)

class Book:
    def __init__(self, title):
        self.title = title

b = Book("Math")
print(b.title)
