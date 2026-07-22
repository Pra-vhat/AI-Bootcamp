class Parent:
    language = ['English']

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.language = Parent.language + ['Nepali']

c = Child()
print(c.language)