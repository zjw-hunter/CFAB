class person():
    def __init__(self, name):
        self.name = name
    
    def myNameIs(self):
        print("My name is: " , self.name )
    
class programmer(person):
    
    def __init__(self, name, favLang):
        self.favLang = favLang
        super().__init__(name)
    
    def myFavLangIs(self):
        print("My favorite language is: ", self.favLang)

class cook(person):
    
    def __init__(self, name, favFood):
        self.favFood = favFood
        super().__init__(name)

    def myFavFoodIs(self):
        print("My favorite food is: ", self.favFood)
        
class programmerCook(programmer, cook):
    pass
        
if __name__ == "__main__":
    zach = cook('zach', 'meat')
    jo = programmer('jo', 'python')
    print(type(jo))
    print(type(zach))
    #sue = programmerCook()
    