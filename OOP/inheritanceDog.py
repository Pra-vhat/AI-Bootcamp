# the class defn below is inconvenient for every sound that a dog barks
'''
class Dog:
    species = "Canis familiaris"

    def __init__ (self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"
'''
    
# now the better class defn
class Dog:
    species = "Canis familiaris" # etymological meaning: the familiar canine

    def __init__ (self, name, age):
        self.name = name
        self.age = age
        # removed .breed method
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"


class breed1(Dog):
    pass

class breed2(Dog):
    pass

class breed3(Dog):
    pass

dog1 = breed1("Browney", 4)
dog2 = breed2("Whitey", 8)
dog3 = breed3("Arthur", 2)
