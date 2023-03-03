import re

colors = list()  #  list colors = new list();
cities = list()
animals = list()
colors.append("red")
cities.append("Durham")
animals.append("lemur")

print(f"type(colors): {type(colors)}")
print(f"type(colors).__name__: {type(colors).__name__}")

def spam():
    pass

print(f"type(spam): {type(spam)}")

x = 5
print(f"type(x): {type(x)}")

class Dog:
    def bark(self):
        print("Woof! Woof!")

d1 = Dog()
d2 = Dog()
d3 = Dog()
d1.bark()

x = list([1, 2, 3])
print(f"x: {x}")

rx = re.compile('^\s*\d*\.\d*\s*')  # class factory
print(f"type(rx): {type(rx)}")





