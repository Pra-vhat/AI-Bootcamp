class Employee:
    '''
    We make use of the .__init__() method to declare
    which attributes each instances of the class should have


    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

# access the class attributes

e1 = Employee("Raja", 11)
print(e1.name)
print(e1.age)

# use the __str__ dunder method
print(e1)
