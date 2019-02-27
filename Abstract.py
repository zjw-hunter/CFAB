from abc import ABC, abstractmethod

class animal(ABC):
    
    @abstractmethod
    def call(self):
        pass
    
    @abstractmethod
    def __init__(self):
        pass

class bird(animal):
    
    def __init__(self, name):
        self.name = name
        
    def call(self):
        print("I'm a bird")
    

class eagle(bird):
    
    def __init__(self, name):
        super().__init__(name)
        
    def call(self):
        print("Screech!")
   
   
   
a = eagle('jon')
a.call()

b = bird('jack')
b.call()
print(b.name)
print(a.name)
