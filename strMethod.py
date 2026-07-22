class Car:
    def __init__(self, name = "def", wheelSize = -1, length = -1 , breadth = -1):
        # passed default arguments def and -1
        self.name = name
        self.wheelSize = wheelSize
        self.length = length
        self.breadth = breadth

    def __str__(self):
        return f'''
Name: {self.name}
Wheel size: {self.wheelSize}
length: {self.length}
breadth: {self.breadth}'''

c0 = Car()
print(c0)
c1 = Car("Tesla", 19, 185.8, 72.8)
print(c1)