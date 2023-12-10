from abc import ABCMeta,abstractmethod

class animal(metaclass = ABCMeta ):
    def __init__(self, name, color):
        self._name = name 
        self._color = color
    
    @property
    def getName(self):
        return self._name
    
    @property
    def getColor(self):
        return self._color
    

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class dog(animal):
    def __init__(self, name, color,age):
        super().__init__(name,color)
        self._age = age
    def move(self):
        return "move dog"
    def eat(self):
        return "eat dog"
 
d = dog("dog","dog",22 )
print(d.move())
print(d.move())
