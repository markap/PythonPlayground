import random

class Animal(object):
    
    def __init__(self, name):
        self.name = name
    
    def run(self):
        print "%s %s is running" % (self.__class__.__name__, self.name)
        
    @staticmethod
    def default_print():
        print "static method"
        
class Dog(Animal):
    
    def run(self):
        super(Dog, self).run()
        print "I am a dog"
        
    @property
    def age(self):
        return random.randint(2, 5)
        
    


if __name__ == "__main__":
    animal = Animal("Default")
    animal.run()
    animal.default_print()
    Animal.default_print()
    
    dog = Dog("Husky")
    dog.run()
    print dog.age